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

    def setData(self,el):
        index = self.cbType.findText(el.type1)
        if index != -1:
            self.cbType.setCurrentIndex(index)

        self.txtName.setText(el.name)
        self.txtArea1.setText(el.area1)
        self.txtArea2.setText(el.area2)

    def clc_btnOk(self):
        self.isOk = True
        self.close()

    def clc_btnCancel(self):
        self.close()
