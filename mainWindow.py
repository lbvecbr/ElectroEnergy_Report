# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(798, 616)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1, 11, 791, 551))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(0)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtGui.QTextEdit(self.widget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.open = QtGui.QPushButton(self.widget)
        self.open.setObjectName(_fromUtf8("open"))
        self.horizontalLayout.addWidget(self.open)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.saveGenerate = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveGenerate.sizePolicy().hasHeightForWidth())
        self.saveGenerate.setSizePolicy(sizePolicy)
        self.saveGenerate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.saveGenerate.setObjectName(_fromUtf8("saveGenerate"))
        self.horizontalLayout.addWidget(self.saveGenerate)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.File = QtGui.QMenu(self.menubar)
        self.File.setObjectName(_fromUtf8("File"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.Open = QtGui.QAction(MainWindow)
        self.Open.setObjectName(_fromUtf8("Open"))
        self.Save = QtGui.QAction(MainWindow)
        self.Save.setObjectName(_fromUtf8("Save"))
        self.Exit = QtGui.QAction(MainWindow)
        self.Exit.setObjectName(_fromUtf8("Exit"))
        self.File.addAction(self.Open)
        self.File.addAction(self.Save)
        self.File.addAction(self.Exit)
        self.menubar.addAction(self.File.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Создание внутреннего отчета по Электроэнергии", None))
        self.label.setText(_translate("MainWindow", "Создание отчета по Электроэнергии", None))
        self.open.setText(_translate("MainWindow", "Открыть", None))
        self.saveGenerate.setText(_translate("MainWindow", "Сохранить и Сгенерировать", None))
        self.File.setTitle(_translate("MainWindow", "Файл", None))
        self.Open.setText(_translate("MainWindow", "Открыть", None))
        self.Open.setStatusTip(_translate("MainWindow", "Открыть", None))
        self.Open.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.Save.setText(_translate("MainWindow", "Сохранить", None))
        self.Save.setStatusTip(_translate("MainWindow", "Сохранить", None))
        self.Save.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.Exit.setText(_translate("MainWindow", "Выход", None))
        self.Exit.setStatusTip(_translate("MainWindow", "Выход", None))
        self.Exit.setShortcut(_translate("MainWindow", "Ctrl+C", None))
