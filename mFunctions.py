from PyQt4 import QtGui


def open_file_(window):
    name = QtGui.QFileDialog.getOpenFileName(window, "Откройте текстовый файл")
    file = open(name, 'r', encoding="utf-8")
    with file:
        text = file.read()
        window.textEdit.setText(text)
