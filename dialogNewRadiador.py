# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dialogNewRadiador.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(241, 302)
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
        self.acceptFlag = 0 
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 9, 221, 251))
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
        self.rolloLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.rolloLabel.setObjectName("rolloLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rolloLabel)
        self.rolloComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.rolloComboBox.setObjectName("rolloComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.rolloComboBox)
        self.cantidadRolloLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.cantidadRolloLabel.setObjectName("cantidadRolloLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.cantidadRolloLabel)
        self.cantidadRolloLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.cantidadRolloLineEdit.setObjectName("cantidadRolloLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cantidadRolloLineEdit)
        self.tubosLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.tubosLabel.setObjectName("tubosLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.tubosLabel)
        self.tubosComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.tubosComboBox.setObjectName("tubosComboBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.tubosComboBox)
        self.cantidadTubosLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.cantidadTubosLabel.setObjectName("cantidadTubosLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.cantidadTubosLabel)
        self.cantidadTubosLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.cantidadTubosLineEdit.setObjectName("cantidadTubosLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cantidadTubosLineEdit)
        self.usaLateralesLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.usaLateralesLabel.setObjectName("usaLateralesLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.usaLateralesLabel)
        self.usaLateralesCheckBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.usaLateralesCheckBox.setObjectName("usaLateralesCheckBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.usaLateralesCheckBox)
        self.cantidadLateralesLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.cantidadLateralesLabel.setObjectName("cantidadLateralesLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.cantidadLateralesLabel)
        self.cantidadLateralesLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.cantidadLateralesLineEdit.setObjectName("cantidadLateralesLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.cantidadLateralesLineEdit)
        self.usaTurbuladoresLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.usaTurbuladoresLabel.setObjectName("usaTurbuladoresLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.usaTurbuladoresLabel)
        self.usaTurbuladoresCheckBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.usaTurbuladoresCheckBox.setObjectName("usaTurbuladoresCheckBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.usaTurbuladoresCheckBox)
        self.cantidadTurbuladoresLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.cantidadTurbuladoresLabel.setObjectName("cantidadTurbuladoresLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.cantidadTurbuladoresLabel)
        self.cantidadTurbuladoresLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.cantidadTurbuladoresLineEdit.setObjectName("cantidadTurbuladoresLineEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.cantidadTurbuladoresLineEdit)
        self.espesorLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.espesorLabel.setObjectName("espesorLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.espesorLabel)
        self.espesorLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.espesorLineEdit.setObjectName("espesorLineEdit")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.espesorLineEdit)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 260, 221, 31))
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
        self.connections()
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.codigoLabel.setText(_translate("Dialog", "Codigo"))
        self.rolloLabel.setText(_translate("Dialog", "Rollo"))
        self.cantidadRolloLabel.setText(_translate("Dialog", "Cantidad Rollo"))
        self.tubosLabel.setText(_translate("Dialog", "Tubos"))
        self.cantidadTubosLabel.setText(_translate("Dialog", "Cantidad Tubos"))
        self.usaLateralesLabel.setText(_translate("Dialog", "Usa laterales?"))
        self.cantidadLateralesLabel.setText(_translate("Dialog", "Cantidad laterales"))
        self.usaTurbuladoresLabel.setText(_translate("Dialog", "Usa turbuladores?"))
        self.cantidadTurbuladoresLabel.setText(_translate("Dialog", "Cantidad turbuladores"))
        self.espesorLabel.setText(_translate("Dialog", "Espesor"))
        self.aceptarButton.setText(_translate("Dialog", "Aceptar"))
        self.cancelarButton.setText(_translate("Dialog", "Cancelar"))

    def connections(self):
        self.aceptarButton.clicked.connect(self.accept)
        self.cancelarButton.clicked.connect(self.cancel)

    def accept(self):
        self.acceptFlag = 1

    def cancel(self):
        pass

    
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

