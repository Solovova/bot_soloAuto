# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\designDialogObject.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 176)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.cbType = QtWidgets.QComboBox(Dialog)
        self.cbType.setObjectName("cbType")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.horizontalLayout_2.addWidget(self.cbType)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.txtName = QtWidgets.QLineEdit(Dialog)
        self.txtName.setObjectName("txtName")
        self.horizontalLayout_3.addWidget(self.txtName)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.txtArea1 = QtWidgets.QLineEdit(Dialog)
        self.txtArea1.setObjectName("txtArea1")
        self.horizontalLayout_4.addWidget(self.txtArea1)
        self.btnArea1 = QtWidgets.QPushButton(Dialog)
        self.btnArea1.setObjectName("btnArea1")
        self.horizontalLayout_4.addWidget(self.btnArea1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.txtArea2 = QtWidgets.QLineEdit(Dialog)
        self.txtArea2.setObjectName("txtArea2")
        self.horizontalLayout_5.addWidget(self.txtArea2)
        self.btnArea2 = QtWidgets.QPushButton(Dialog)
        self.btnArea2.setObjectName("btnArea2")
        self.horizontalLayout_5.addWidget(self.btnArea2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnOk = QtWidgets.QPushButton(Dialog)
        self.btnOk.setObjectName("btnOk")
        self.horizontalLayout.addWidget(self.btnOk)
        self.btnCancel = QtWidgets.QPushButton(Dialog)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Type:"))
        self.cbType.setItemText(0, _translate("Dialog", "Area"))
        self.cbType.setItemText(1, _translate("Dialog", "Text"))
        self.cbType.setItemText(2, _translate("Dialog", "Point"))
        self.label_2.setText(_translate("Dialog", "Name:"))
        self.label_3.setText(_translate("Dialog", "Area №1:"))
        self.btnArea1.setText(_translate("Dialog", "..."))
        self.label_4.setText(_translate("Dialog", "Area №2:"))
        self.btnArea2.setText(_translate("Dialog", "..."))
        self.btnOk.setText(_translate("Dialog", "Ok"))
        self.btnCancel.setText(_translate("Dialog", "Cancel"))
