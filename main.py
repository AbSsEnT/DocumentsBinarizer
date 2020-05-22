import os
import sys

import cv2
import numpy as np
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QMessageBox

import design
from src.documents_binarization import DocumentBinarizer


class App(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.document_binarizer = DocumentBinarizer()

        self.setupUi(self)
        self.showMaximized()
        self.setFixedSize(self.size())
        self.setWhatsThis("Nikita")
        self.btnBrowse.clicked.connect(self.__browse_image)
        self.btnBinarize.clicked.connect(self.__binarize_image)
        self.btnSave.clicked.connect(self.__save_image)
        self.btnQuit.clicked.connect(self.__quit_program)

    def closeEvent(self, event):
        result = QMessageBox.question(self, "Confirm Exit...", "Are you sure you want to exit ?",
                                      QMessageBox.Yes | QMessageBox.No)
        event.ignore()

        if result == QMessageBox.Yes:
            event.accept()

    @staticmethod
    def __quit_program():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Are you sure you want to exit?")
        msg.setWindowTitle("Confirm Exit...")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        result = msg.exec()

        if result == QMessageBox.Yes:
            QtCore.QCoreApplication.instance().quit()
        else:
            msg.close()

    def __browse_image(self):
        filename = QFileDialog.getOpenFileName(self, caption="Choose an image",
                                               filter="Image files (*.png *.jpg *.jpeg)")

        if filename[0] != '':
            self.image_path = filename[0]
            image = QPixmap(self.image_path)
            image = image.scaled(self.imgView.size(), QtCore.Qt.KeepAspectRatio)

            self.imgView.setPixmap(QPixmap(image))
            self.btnBinarize.setEnabled(True)
            self.btnSave.setEnabled(False)

    def __binarize_image_backend(self):
        self.binarized_image = self.document_binarizer.binarize(self.image_path)
        img = np.require(self.binarized_image, np.uint8, 'C')
        qbinarized_image = QtGui.QImage(img, int(img.shape[1]), int(img.shape[0]), QtGui.QImage.Format_Grayscale8)
        qbinarized_image = qbinarized_image.scaled(self.imgView.size(), QtCore.Qt.KeepAspectRatio)
        self.imgView.setPixmap(QPixmap(qbinarized_image))
        self.btnSave.setEnabled(True)
        self.__show_popup()

    def __binarize_image(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Start binarization?")
        msg.setWindowTitle("Confirm binarization...")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.btnBinarize.setEnabled(False)
        res = msg.exec()

        if res == QMessageBox.Ok:
            self.__binarize_image_backend()
        else:
            self.btnBinarize.setEnabled(True)
            msg.close()

    @staticmethod
    def __show_popup():
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText("The image was binarized successfully")

        msg.exec_()

    def __save_image(self):
        filepath, _ = QFileDialog.getSaveFileName(self, "Save Image", filter="Image files (*.png *.jpg *.jpeg)")

        if filepath == "":
            return

        cv2.imwrite(os.path.join(filepath), self.binarized_image)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()
