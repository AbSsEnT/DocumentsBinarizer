# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../../../../../../design.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1044, 695)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../etc/Screenshot from 2020-05-18 22-09-21.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWhatsThis("")
        MainWindow.setStyleSheet("background-color:rgb(220, 217, 203)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.imgView = QtWidgets.QLabel(self.centralwidget)
        self.imgView.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.imgView.setAlignment(QtCore.Qt.AlignCenter)
        self.imgView.setObjectName("imgView")
        self.verticalLayout.addWidget(self.imgView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBrowse.setObjectName("btnBrowse")
        self.horizontalLayout.addWidget(self.btnBrowse)
        self.btnBinarize = QtWidgets.QPushButton(self.centralwidget)
        self.btnBinarize.setEnabled(False)
        self.btnBinarize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnBinarize.setObjectName("btnBinarize")
        self.horizontalLayout.addWidget(self.btnBinarize)
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setEnabled(False)
        self.btnSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.btnQuit = QtWidgets.QPushButton(self.centralwidget)
        self.btnQuit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnQuit.setObjectName("btnQuit")
        self.horizontalLayout.addWidget(self.btnQuit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Document Binarizer v1.0.0"))
        self.imgView.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#4d4d4d;\">Choose an image</span></p></body></html>"))
        self.btnBrowse.setToolTip(_translate("MainWindow", "Choose an image to binarize"))
        self.btnBrowse.setText(_translate("MainWindow", "Choose image"))
        self.btnBinarize.setToolTip(_translate("MainWindow", "Start binarization"))
        self.btnBinarize.setText(_translate("MainWindow", "Binarize"))
        self.btnSave.setToolTip(_translate("MainWindow", "Save the image to the desired directory"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.btnQuit.setToolTip(_translate("MainWindow", "Quit the program"))
        self.btnQuit.setText(_translate("MainWindow", "Quit"))
