# This Python file uses the following encoding: utf-8
import sys

from PySide2.QtCore import Slot
from PySide2.QtWidgets import (
    QApplication, QMainWindow, QGraphicsScene, QFileDialog, QMessageBox
)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from DicomLoader import DicomLoader

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

        self.ui.actionAbrir.triggered.connect(self.open_folder)

        # Carga de métodos para cada tipo de input
        self.ui.axialSlider.valueChanged.connect(self.update_axial_plane)
        self.ui.sagitalSlider.valueChanged.connect(self.update_sagital_plane)
        self.ui.coronalSlider.valueChanged.connect(self.update_coronal_plane)

        self.ui.axialSpinBox.valueChanged.connect(self.update_axial_plane)
        self.ui.sagitalSpinBox.valueChanged.connect(self.update_sagital_plane)
        self.ui.coronalSpinBox.valueChanged.connect(self.update_coronal_plane)

        self.ui.minDoubleSpinBox.valueChanged.connect(self.update_spectrum)
        self.ui.maxDoubleSpinBox.valueChanged.connect(self.update_spectrum)


    def _load_planes(self, path):
        # Se cargan las imágenes DICOM
        self.dcm = DicomLoader(path)

        # Límites espectrales
        self.min_spectrum = self.dcm.min
        self.max_spectrum = self.dcm.max

        # Se habilitan los elementos gráficos
        self._init_ui()

        # Se dibujan los planos
        self._draw_plane('axial', 0)
        self._draw_plane('sagital', 0)
        self._draw_plane('coronal', 0)


    def _init_ui(self):
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

        # Límites espectrales en el GUI
        self.ui.minLineEdit.setText(str(self.dcm.min))
        self.ui.maxLineEdit.setText(str(self.dcm.max))
        self.ui.minDoubleSpinBox.setRange(self.dcm.min, self.dcm.max)
        self.ui.maxDoubleSpinBox.setRange(self.dcm.min, self.dcm.max)

        self.ui.minDoubleSpinBox.setValue(self.dcm.min)
        self.ui.maxDoubleSpinBox.setValue(self.dcm.max)

        # Límites para cada plano
        axial_limit = len(self.dcm.slices) - 1
        sagital_limit, coronal_limit = self.dcm.img3d[0].shape

        # Cambio de límites para los sliders y spinbox
        self.ui.axialSlider.setRange(0, axial_limit)
        self.ui.sagitalSlider.setRange(0, sagital_limit - 1)
        self.ui.coronalSlider.setRange(0, coronal_limit - 1)

        self.ui.axialSpinBox.setRange(0, axial_limit)
        self.ui.sagitalSpinBox.setRange(0, sagital_limit - 1)
        self.ui.coronalSpinBox.setRange(0, coronal_limit - 1)


    def _draw_plane(self, plane: str, index: int) -> None:
        # Se obtiene la matriz de píxeles del corte indicado por index
        data = self.dcm.plane(plane, index)

        # Inicialización del canvas para mostrar el corte
        fig = Figure()
        canvas = FigureCanvas(fig)
        scene = QGraphicsScene()
        scene.addWidget(canvas)

        # Según el plano, se dibuja en su vista correspondiente
        match plane:
            case 'axial':
                self.ui.axialView.setScene(scene)
            case 'sagital':
                data = data.T
                self.ui.sagitalView.setScene(scene)
            case 'coronal':
                data = data.T
                self.ui.coronalView.setScene(scene)

        # Eliminación de bordes y labels de la imagen
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_axis_off()

        # Se muestra la imagen
        ax.imshow(data, cmap = 'gray', vmin=self.min_spectrum, vmax=self.max_spectrum)


    def _update_plane(self, plane: str, index: int) -> None:
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

    @Slot()
    def open_folder(self) -> None:
        path = QFileDialog.getExistingDirectory(
            self,
            'Seleccionar carpeta'
        ) + '/*'
        self._load_planes(path)


    @Slot()
    def update_spectrum(self) -> None:
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
    def update_axial_plane(self, index: int) -> None:
        self._update_plane('axial', index)


    @Slot()
    def update_sagital_plane(self, index: int) -> None:
        self._update_plane('sagital', index)


    @Slot()
    def update_coronal_plane(self, index: int) -> None:
        self._update_plane('coronal', index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
