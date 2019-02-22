from PyQt4 import QtGui
from PyQt4.QtGui import QApplication, QMainWindow
from mainWindow import Ui_MainWindow
from mFunctions import open_file_
from mSaveGenerate import save_generate_
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.open.clicked.connect(self.open_file)
        self.saveGenerate.clicked.connect(self.save_generate)

    def open_file(self):
        open_file_(self)

    def save_generate(self):
        save_generate_(self)


def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


main()

# app = QtGui.QApplication(sys.argv)
# MainWindow = QtGui.QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow)
# MainWindow.show()
# sys.exit(app.exec_())
