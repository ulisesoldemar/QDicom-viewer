# This Python file uses the following encoding: utf-8
import sys

from PySide2.QtCore import Slot
from PySide2.QtWidgets import (
    QApplication, QMainWindow, QGraphicsScene, QFileDialog, QMessageBox
)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from DicomLoader import DicomLoader, InvalidDICOM, DICOMNotFound

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Se conectan las acciones de apertura y cierre
        self.ui.actionCarpeta.triggered.connect(self.open_folder)
        self.ui.actionSalir.triggered.connect(self.close)


    def __enable_inputs(self) -> None:
        # Se habilitan los sliders después de cargar las imágenes
        self.ui.axialSlider.setEnabled(True)
        self.ui.sagitalSlider.setEnabled(True)
        self.ui.coronalSlider.setEnabled(True)

        # Se habilitan los spinbox después de cargar las imágenes
        self.ui.axialSpinBox.setEnabled(True)
        self.ui.sagitalSpinBox.setEnabled(True)
        self.ui.coronalSpinBox.setEnabled(True)

        # Se habilitan los float spinbox después de cargar las imágenes
        self.ui.minDoubleSpinBox.setEnabled(True)
        self.ui.maxDoubleSpinBox.setEnabled(True)


    def __set_spectrum_limits(self) -> None:
        # Límites espectrales en el GUI
        self.ui.minLineEdit.setText(str(self.dcm.min))
        self.ui.maxLineEdit.setText(str(self.dcm.max))
        self.ui.minDoubleSpinBox.setRange(self.dcm.min, self.dcm.max)
        self.ui.maxDoubleSpinBox.setRange(self.dcm.min, self.dcm.max)

        self.ui.minDoubleSpinBox.setValue(self.dcm.min)
        self.ui.maxDoubleSpinBox.setValue(self.dcm.max)


    def __set_plane_limits(self) -> None:
        # Límites para cada plano
        y, x, z = self.dcm.shape

        # Cambio de límites para los sliders y spinbox
        self.ui.axialSlider.setRange(0, z-1)
        self.ui.sagitalSlider.setRange(0, x-1)
        self.ui.coronalSlider.setRange(0, y-1)

        self.ui.axialSpinBox.setRange(0, z-1)
        self.ui.sagitalSpinBox.setRange(0, x-1)
        self.ui.coronalSpinBox.setRange(0, y-1)


    def __connect_ui_components(self) -> None:
        # Se conectan los slider a los spinbox de los planos
        self.ui.axialSlider.valueChanged.connect(self.ui.axialSpinBox.setValue)
        self.ui.sagitalSlider.valueChanged.connect(self.ui.sagitalSpinBox.setValue)
        self.ui.coronalSlider.valueChanged.connect(self.ui.coronalSpinBox.setValue)

        # Se usa una función anónima para conectar con el método de tipo slot
        self.ui.axialSpinBox.valueChanged.connect(
            lambda index: self.update_plane('axial', index)
        )
        self.ui.sagitalSpinBox.valueChanged.connect(
            lambda index: self.update_plane('sagital', index)
        )
        self.ui.coronalSpinBox.valueChanged.connect(
            lambda index: self.update_plane('coronal', index)
        )

        # Se conectan los spinbox espectrales al método de actualización
        self.ui.minDoubleSpinBox.valueChanged.connect(self.update_spectrum)
        self.ui.maxDoubleSpinBox.valueChanged.connect(self.update_spectrum)


    def _load_planes(self, path) -> None:
        print('load_planes')
        # Se cargan las imágenes DICOM
        try:
            self.dcm = DicomLoader(path)
        except (InvalidDICOM, DICOMNotFound) as e:
            QMessageBox.critical(self, 'Error', f'{str(e)}')
            return

        # Límites espectrales
        self.min_spectrum = self.dcm.min
        self.max_spectrum = self.dcm.max

        # Se habilitan los elementos gráficos
        self.__enable_inputs()
        self.__set_spectrum_limits()
        self.__set_plane_limits()
        self.__connect_ui_components()

        # Se dibujan los planos
        self._draw_plane('axial', 0)
        self._draw_plane('sagital', 0)
        self._draw_plane('coronal', 0)

        QMessageBox.information(
            self,
            'Archivos cargados',
            f'Se cargaron {len(self.dcm.slices)} archivos'
        )


    def _draw_plane(self, plane: str, index: int) -> None:
        print('draw_plane')
        # Se obtiene la matriz de píxeles del corte indicado por index
        data = self.dcm.plane(plane, index)

        # Inicialización del canvas para mostrar el corte
        fig = Figure(figsize=plt.figaspect(data)/2)
        canvas = FigureCanvas(fig)
        scene = QGraphicsScene()
        scene.addWidget(canvas)

        # Según el plano, se dibuja en su vista correspondiente
        match plane:
            case 'axial':
                self.ui.axialView.setScene(scene)
            case 'sagital':
                self.ui.sagitalView.setScene(scene)
            case 'coronal':
                self.ui.coronalView.setScene(scene)

        # Eliminación de bordes y labels de la imagen
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_axis_off()

        # Se muestra la imagen
        ax.imshow(data, cmap = 'gray', vmin=self.min_spectrum, vmax=self.max_spectrum)


    @Slot()
    def open_folder(self) -> None:
        print('open_folder')
        path = QFileDialog.getExistingDirectory(
            self,
            'Seleccionar carpeta'
        ) + '/*'
        self._load_planes(path)


    @Slot()
    def update_spectrum(self) -> None:
        print('update_spectrum')
        # Valores de actualización de la ventana espectro
        self.min_spectrum = self.ui.minDoubleSpinBox.value()
        self.max_spectrum = self.ui.maxDoubleSpinBox.value()

        # Se limita el valor mínimo y el máximo para que no
        # suceda min > max
        self.ui.minDoubleSpinBox.setMaximum(self.max_spectrum)
        self.ui.maxDoubleSpinBox.setMinimum(self.min_spectrum)

        # Se recupera el index actual
        axial_index = self.ui.axialSpinBox.value()
        sagital_index = self.ui.sagitalSpinBox.value()
        coronal_index = self.ui.coronalSpinBox.value()

        # Se redibuja el plano con la nueva resolución espectral
        self._draw_plane('axial', axial_index)
        self._draw_plane('sagital', sagital_index)
        self._draw_plane('coronal', coronal_index)


    @Slot()
    def update_plane(self, plane: str, index: int) -> None:
        print('Update plane')
        try:
            # Se dibuja el corte en el plano seleccionado
           self._draw_plane(plane, index)
           # Modificación de los valores del slider/spinbox según el plano
           match plane:
               case 'axial':
                   self.ui.axialSlider.setValue(index)
                   self.ui.axialSpinBox.setValue(index)
               case 'sagital':
                   self.ui.sagitalSlider.setValue(index)
                   self.ui.sagitalSpinBox.setValue(index)
               case 'coronal':
                   self.ui.coronalSlider.setValue(index)
                   self.ui.coronalSpinBox.setValue(index)

        # En caso de no haber abierto la carpeta
        except AttributeError as e:
            print(e)
            QMessageBox.critical(
                self, 'Error', 'No hay archivos seleccionados.'
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
