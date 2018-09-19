# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
import sys
import serial
from PyQt5.QtGui import *
import threading


class Ui_MainWindow(object):
    ser = serial.Serial()
    list_a = []
    list_b = []
    list_c = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 90, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 140, 54, 12))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(320, 80, 111, 22))

        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(320, 130, 111, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 180, 101, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 220, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 220, 54, 12))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 220, 54, 12))
        self.label_6.setObjectName("label_6")

        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(240, 200, 306, 192))
        self.tableView.setObjectName("tableView")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 410, 61, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 410, 71, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "关闭串口"))
        self.label.setText(_translate("MainWindow", "选择串口"))
        self.label_2.setText(_translate("MainWindow", "格式选择"))

        self.comboBox.setItemText(0, _translate("MainWindow", "COM1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "COM2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "COM3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "COM4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "COM5"))
        self.comboBox.setItemText(5, _translate("MainWindow", "COM6"))
        self.comboBox.setItemText(6, _translate("MainWindow", "COM7"))
        self.comboBox.setItemText(7, _translate("MainWindow", "COM8"))
        self.comboBox.setItemText(8, _translate("MainWindow", "COM9"))
        self.comboBox.setItemText(9, _translate("MainWindow", "COM10"))
        self.comboBox.setItemText(10, _translate("MainWindow", "COM11"))
        self.comboBox.setItemText(11, _translate("MainWindow", "COM12"))

        self.comboBox.activated[str].connect(self.onActivated)

        self.comboBox_2.activated[str].connect(self.onActivated1)

        self.pushButton_2.clicked.connect(self.Delete)
        self.pushButton.clicked.connect(self.Close)
        self.pushButton_3.clicked.connect(self.Drop)

        self.comboBox_2.setItemText(0, _translate("MainWindow", "Wiegand 26"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Wiegand 32/34"))

        self.label_3.setText(_translate("MainWindow", "读出的卡号列表"))

        self.pushButton_2.setText(_translate("MainWindow", "删除数据"))
        self.pushButton_3.setText(_translate("MainWindow", "全部删除"))

    def Delete(self):
        # 单行删除
        indexs = self.tableView.selectionModel().selection().indexes()
        if len(indexs) > 0:
            index = indexs[0]
            print(index.row())
            self.list_b.pop(index.row())
            self.list_a.pop(index.row())
            self.model.removeRows(index.row(), 1)

    def Drop(self):
        # 多行删除
        indexs = self.tableView.selectionModel().selection().indexes()
        for i in indexs:
            index = indexs[0]
            self.list_b.pop(index.row())
            self.list_a.pop(index.row())

            self.model.removeRows(index.row(), 1)

    def onActivated(self, text):
        print(text)
        self.ser.baudrate = 9600
        self.ser.port = text
        self.ser.open()
        print(self.ser.is_open)
        if True:
            print('打开成功')
            print(self.ser.is_open)
            self.t1 = threading.Thread(target=self.receive_data)
            self.t2 = threading.Thread(target=self.receive_data2)

        else:
            print("打开失败")

    def receive_data(self):
        print("线程韦根26开启")
        self.model = QStandardItemModel()

        self.model.setHorizontalHeaderLabels(['区号', '卡号', '16进制'])

        self.tableView.setModel(self.model)

        while (self.ser.isOpen()):

            q, w, e = self.ser.read(3)
            # a, q, w, e = self.ser.read(4)

            print(q, w, e)

            if q < 16:
                a = ''
                a += hex(q)
                a += hex(w)[0]
                a += hex(w)[2:]
                a += hex(e)[2:]
                a = a.upper()
                w = ''
                w = a[3:]
                w = int(w, 16)
            elif q >= 16:
                a = ''
                a += hex(q)
                a += hex(w)[2:]
                a += hex(e)[2:]
                a = a.upper()
                w = ''
                w = a[4:]
                w = int(w, 16)
            if e < 16:
                a = ''
                a += hex(q)
                a += hex(w)[2:4]
                a += hex(q)[0]
                a += hex(e)[2:]
                print(a)
                w = ''
                w = a[4:]
                w = int(w, 16)

            self.list_a.append(w)
            print(self.list_a)
            for i in self.list_a:
                if i not in self.list_b:
                    self.list_b.append(i)
                    self.model.appendRow([
                        QStandardItem("%s" % q),
                        QStandardItem("%s" % w),
                        QStandardItem("%s" % a),
                    ])

            print(self.list_b)

    def receive_data2(self):
        print("线程韦根34开启")
        self.model = QStandardItemModel()

        self.model.setHorizontalHeaderLabels(['区号', '卡号', '16进制'])

        self.tableView.setModel(self.model)

        while (self.ser.isOpen()):

            # q, w, e = self.ser.read(3)
            a, q, w, e = self.ser.read(4)

            if q < 16:
                a = ''
                a += hex(q)
                a += hex(w)[0]
                a += hex(w)[2:]
                a += hex(e)[2:]
                a = a.upper()
                w = ''
                w = a[3:]
                w = int(w, 16)
            elif q >= 16:
                a = ''
                a += hex(q)
                a += hex(w)[2:]
                a += hex(e)[2:]
                a = a.upper()
                w = ''
                w = a[4:]
                w = int(w, 16)
            if e < 16:
                a = ''
                a += hex(q)
                a += hex(w)[2:4]
                a += hex(q)[0]
                a += hex(e)[2:]
                print(a)
                w = ''
                w = a[4:]
                w = int(w, 16)

            self.list_a.append(w)
            print(self.list_a)
            for i in self.list_a:
                if i not in self.list_b:
                    self.list_b.append(i)
                    self.model.appendRow([
                        QStandardItem("%s" % q),
                        QStandardItem("%s" % w),
                        QStandardItem("%s" % a),
                    ])

            print(self.list_b)

    def Close(self):
        self.list_a.clear()
        self.list_b.clear()
        self.ser.close()

    def onActivated1(self, text):
        print(text)
        if text == "Wiegand 26":
            self.t1.start()


        elif text == "Wiegand 32/34":
            self.t2.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    formObj = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(formObj)
    formObj.show()
    sys.exit(app.exec_())
