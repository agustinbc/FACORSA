# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dialogNewPedido.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(719, 567)
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 510, 701, 41))
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
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 681, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, 681, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.aceptarButton.setText(_translate("Dialog", "Aceptar"))
        self.cancelarButton.setText(_translate("Dialog", "Cancelar"))
        self.label.setText(_translate("Dialog", "Codigo"))
        self.label_2.setText(_translate("Dialog", "Fecha"))
        self.label_3.setText(_translate("Dialog", "Estado"))
        self.comboBox.setItemText(0, _translate("Dialog", "Pedido"))
        self.comboBox.setItemText(1, _translate("Dialog", "Viajando"))
        self.comboBox.setItemText(2, _translate("Dialog", "En depósito"))
        self.comboBox.setItemText(3, _translate("Dialog", "Retirado"))
        self.comboBox.setItemText(4, _translate("Dialog", "En fábrica"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

