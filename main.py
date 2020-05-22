import sys

from PyQt5.QtWidgets import QApplication

from src.application import App

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()
