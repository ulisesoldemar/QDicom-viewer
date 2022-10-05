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
        MainWindow.resize(800, 600)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.sagitalView = QGraphicsView(self.centralwidget)
        self.sagitalView.setObjectName(u"sagitalView")

        self.gridLayout_2.addWidget(self.sagitalView, 1, 2, 1, 2)

        self.sagitalSlider = QSlider(self.centralwidget)
        self.sagitalSlider.setObjectName(u"sagitalSlider")
        self.sagitalSlider.setEnabled(False)
        self.sagitalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.sagitalSlider, 2, 2, 1, 1)

        self.sagitalSpinBox = QSpinBox(self.centralwidget)
        self.sagitalSpinBox.setObjectName(u"sagitalSpinBox")
        self.sagitalSpinBox.setEnabled(False)

        self.gridLayout_2.addWidget(self.sagitalSpinBox, 2, 3, 1, 1)

        self.coronalSpinBox = QSpinBox(self.centralwidget)
        self.coronalSpinBox.setObjectName(u"coronalSpinBox")
        self.coronalSpinBox.setEnabled(False)

        self.gridLayout_2.addWidget(self.coronalSpinBox, 5, 1, 1, 1)

        self.axialSlider = QSlider(self.centralwidget)
        self.axialSlider.setObjectName(u"axialSlider")
        self.axialSlider.setEnabled(False)
        self.axialSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.axialSlider, 2, 0, 1, 1)

        self.axialSpinBox = QSpinBox(self.centralwidget)
        self.axialSpinBox.setObjectName(u"axialSpinBox")
        self.axialSpinBox.setEnabled(False)

        self.gridLayout_2.addWidget(self.axialSpinBox, 2, 1, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)

        self.axialView = QGraphicsView(self.centralwidget)
        self.axialView.setObjectName(u"axialView")

        self.gridLayout_2.addWidget(self.axialView, 1, 0, 1, 2)

        self.coronalSlider = QSlider(self.centralwidget)
        self.coronalSlider.setObjectName(u"coronalSlider")
        self.coronalSlider.setEnabled(False)
        self.coronalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.coronalSlider, 5, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)

        self.coronalView = QGraphicsView(self.centralwidget)
        self.coronalView.setObjectName(u"coronalView")

        self.gridLayout_2.addWidget(self.coronalView, 4, 0, 1, 2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.maxDoubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.maxDoubleSpinBox.setObjectName(u"maxDoubleSpinBox")
        self.maxDoubleSpinBox.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.maxDoubleSpinBox)

        self.minDoubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.minDoubleSpinBox.setObjectName(u"minDoubleSpinBox")
        self.minDoubleSpinBox.setEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.minDoubleSpinBox)


        self.gridLayout_2.addLayout(self.formLayout, 4, 2, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 3, 2, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Plano coronal", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Plano axial", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Plano sagital", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"M\u00ednimo", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"M\u00e1ximo", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Controlador espectral", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

