# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(803, 595)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.coronalSpinBox = QSpinBox(self.centralwidget)
        self.coronalSpinBox.setObjectName(u"coronalSpinBox")
        self.coronalSpinBox.setEnabled(False)

        self.gridLayout_2.addWidget(self.coronalSpinBox, 6, 2, 1, 1)

        self.coronalSlider = QSlider(self.centralwidget)
        self.coronalSlider.setObjectName(u"coronalSlider")
        self.coronalSlider.setEnabled(False)
        self.coronalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.coronalSlider, 6, 1, 1, 1)

        self.axialSlider = QSlider(self.centralwidget)
        self.axialSlider.setObjectName(u"axialSlider")
        self.axialSlider.setEnabled(False)
        self.axialSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.axialSlider, 2, 1, 1, 1)

        self.sagitalSpinBox = QSpinBox(self.centralwidget)
        self.sagitalSpinBox.setObjectName(u"sagitalSpinBox")
        self.sagitalSpinBox.setEnabled(False)

        self.gridLayout_2.addWidget(self.sagitalSpinBox, 2, 5, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 3)

        self.coronalView = QGraphicsView(self.centralwidget)
        self.coronalView.setObjectName(u"coronalView")

        self.gridLayout_2.addWidget(self.coronalView, 5, 0, 1, 3)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 3, 0, 1, 6)

        self.axialView = QGraphicsView(self.centralwidget)
        self.axialView.setObjectName(u"axialView")

        self.gridLayout_2.addWidget(self.axialView, 1, 0, 1, 3)

        self.axialSpinBox = QSpinBox(self.centralwidget)
        self.axialSpinBox.setObjectName(u"axialSpinBox")
        self.axialSpinBox.setEnabled(False)

        self.gridLayout_2.addWidget(self.axialSpinBox, 2, 2, 1, 1)

        self.sagitalView = QGraphicsView(self.centralwidget)
        self.sagitalView.setObjectName(u"sagitalView")

        self.gridLayout_2.addWidget(self.sagitalView, 1, 3, 1, 3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 3, 1, 3)

        self.sagitalSlider = QSlider(self.centralwidget)
        self.sagitalSlider.setObjectName(u"sagitalSlider")
        self.sagitalSlider.setEnabled(False)
        self.sagitalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.sagitalSlider, 2, 4, 1, 1)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 2, 3, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.minLineEdit = QLineEdit(self.groupBox)
        self.minLineEdit.setObjectName(u"minLineEdit")
        self.minLineEdit.setEnabled(False)
        self.minLineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.minLineEdit)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9)

        self.maxLineEdit = QLineEdit(self.groupBox)
        self.maxLineEdit.setObjectName(u"maxLineEdit")
        self.maxLineEdit.setEnabled(False)
        self.maxLineEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.maxLineEdit)


        self.formLayout.setLayout(0, QFormLayout.SpanningRole, self.horizontalLayout)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.minDoubleSpinBox = QDoubleSpinBox(self.groupBox)
        self.minDoubleSpinBox.setObjectName(u"minDoubleSpinBox")
        self.minDoubleSpinBox.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.minDoubleSpinBox)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.maxDoubleSpinBox = QDoubleSpinBox(self.groupBox)
        self.maxDoubleSpinBox.setObjectName(u"maxDoubleSpinBox")
        self.maxDoubleSpinBox.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.maxDoubleSpinBox)


        self.gridLayout_2.addWidget(self.groupBox, 4, 3, 3, 3)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 3)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 6, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 803, 23))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
#if QT_CONFIG(shortcut)
        self.actionSalir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Plano axial", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Corte", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Plano sagital", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Corte", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Controlador espectral", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Rango espectral:", None))
        self.minLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.maxLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"L\u00edmite inferior:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"L\u00edmite superior:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Plano coronal", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Corte", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

