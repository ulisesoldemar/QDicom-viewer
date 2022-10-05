# This Python file uses the following encoding: utf-8
import pydicom
import numpy as np
import glob

class InvalidDICOM(Exception):
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.message = 'Archivo no válido'
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.filename}'


class DICOMNotFound(Exception):
    def __str__(self):
        return 'No se encontraron archivos DICOM válidos'


class DicomLoader:
    def __init__(self, path: str) -> None:
        # Carga de archivos
        files = []
        try:
            for fname in glob.glob(path, recursive=False):
                files.append(pydicom.dcmread(fname))
        except pydicom.errors.InvalidDicomError:
            raise InvalidDICOM(fname)

        if not len(files):
            raise DICOMNotFound

        # Se saltan los archivos sin SliceLocation (ej. scout views)
        self.slices = []
        skipcount = 0
        for f in files:
            if hasattr(f, 'SliceLocation'):
                self.slices.append(f)
            else:
                skipcount += 1

        # Orden correcto de los cortes
        self.slices = sorted(self.slices, key=lambda x: x.InstanceNumber)

        # Relación de aspecto, asumiendo que todos los cortes tienen
        # el mismo spacing y thickness
        self.ps = self.slices[0].PixelSpacing
        self.st = self.slices[0].SliceThickness
        self.ax_aspect = self.ps[1]/self.ps[0]
        self.sag_aspect = self.ps[1]/self.st
        self.cor_aspect = self.st/self.ps[0]

        # Creación de la matriz 3D
        y, x = self.slices[0].pixel_array.shape
        z = len(self.slices)
        img_shape = (y, x, z)
        self.img3d = np.zeros(img_shape)

        # Se rellena la matriz 3D con los píxeles de cada corte
        # y se aplica una regresión lineal para mejorar la calidad de la
        # imagen
        for i, s in enumerate(self.slices):
            img2d = s.pixel_array
            m = s.RescaleSlope
            b = s.RescaleIntercept
            img2d = m * img2d + b
            self.img3d[:, :, i] = img2d

        # Valor mínimo y máximo del espectro
        self.min = self.img3d.min()
        self.max = self.img3d.max()


    def plane(self, plane: str, slice_index: int) -> np.ndarray:
        match plane:
            case 'axial':
                return self.img3d[:, :, slice_index]
            case 'sagital':
                return self.img3d[:, slice_index, :].T
            case 'coronal':
                return self.img3d[slice_index, :, :].T


    def anonymize(self, override: bool=True) -> None:
        pass
