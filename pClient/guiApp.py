from PyQt5 import QtWidgets
from dialogObject.dialogObject import DialogObject
import designMain
import os

class GuiApp(QtWidgets.QMainWindow, designMain.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.btnObjectsAdd.clicked.connect(self.clc_btnObjectsAdd)
        self.btnObjectsEdit.clicked.connect(self.clc_btnObjectsEdit)
        self.btnObjectsDelete.clicked.connect(self.clc_btnObjectsDelete)
    
    def clc_btnObjectsAdd(self):
        print("add")
        dlg = DialogObject()
        dlg.setData("tt1","tt2")
        # dlg.setWindowTitle("HELLO!")
        dlg.exec_()
        print(dlg.isOk)


        # rowPosition = self.tableWidget.rowCount()
        # self.tableWidget.insertRow(rowPosition)
        # self.tableWidget.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem("text1"))
        # self.tableWidget.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem("text2"))

    def clc_btnObjectsEdit(self):
        print("edit")

    def clc_btnObjectsDelete(self):
        print("del")