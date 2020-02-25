# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dialogNewMaterial.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(241, 237)
        Dialog.setStyleSheet("#Dialog\n"
"{background-color: rgba(32,80,96,100);}\n"
"\n"
"QPushButton\n"
"{\n"
"color: white;\n"
"background-color: #27a9e3;\n"
"border-width: 0px;\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: #66c011;\n"
"}\n"
"QLabel {color: white;}\n"
"QLineEdite {border-radius: 3px;}")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 9, 221, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.codigoLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.codigoLabel.setObjectName("codigoLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.codigoLabel)
        self.codigoLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.codigoLineEdit.setObjectName("codigoLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.codigoLineEdit)
        self.nombreLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.nombreLabel.setObjectName("nombreLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nombreLabel)
        self.nombreComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.nombreComboBox.setObjectName("nombreComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nombreComboBox)
        self.qtyLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.qtyLabel.setObjectName("qtyLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.qtyLabel)
        self.qtyLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.qtyLineEdit.setObjectName("qtyLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.qtyLineEdit)
        
        self.colorLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.colorLabel.setObjectName("colorLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.colorLabel)
        self.colorComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.colorComboBox.setObjectName("colorComboBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.colorComboBox)
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 200, 221, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.aceptarButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aceptarButton.sizePolicy().hasHeightForWidth())
        self.aceptarButton.setSizePolicy(sizePolicy)
        self.aceptarButton.setMinimumSize(QtCore.QSize(0, 0))
        self.aceptarButton.setObjectName("aceptarButton")
        self.horizontalLayout.addWidget(self.aceptarButton)
        self.cancelarButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancelarButton.setObjectName("cancelarButton")
        self.horizontalLayout.addWidget(self.cancelarButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.codigoLabel.setText(_translate("Dialog", "Codigo"))
        self.nombreLabel.setText(_translate("Dialog", "Nombre"))
        self.qtyLabel.setText(_translate("Dialog", "Cantidad"))
        self.aceptarButton.setText(_translate("Dialog", "Aceptar"))
        self.colorLabel.setText(_translate("Dialog", "Estado"))
        self.cancelarButton.setText(_translate("Dialog", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

