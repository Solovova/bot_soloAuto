from PyQt5 import QtWidgets
from dialogObject.designDialogObject import Ui_Dialog # pylint: disable=no-name-in-module, import-error
import os

class DialogObject(QtWidgets.QDialog, Ui_Dialog):
    isOk = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)  

        self.btnOk.clicked.connect(self.clc_btnOk)
        self.btnCancel.clicked.connect(self.clc_btnCancel)

    def setData(self, f1, f2):
        self.lineEdit.setText(f1)
        self.lineEdit_2.setText(f2)

    def clc_btnOk(self):
        self.isOk = True
        print("ok")
        self.close()

    def clc_btnCancel(self):
        print("cancel")
        self.close()
