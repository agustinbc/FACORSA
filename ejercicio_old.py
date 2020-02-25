# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ejercicio.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql, QtPrintSupport
import dialogNewRadiador, dialogNewMaterial, dialogNewInventarioSobr, dialogNewInventarioLote, dialogNewPedido, dialogActualizePedido
import sqlite3
import datetime
import calendar
import pandas as pd
import pdfkit
from win32api import GetSystemMetrics

WIDTH = GetSystemMetrics(0)-20
HEIGHT = GetSystemMetrics(1)-80

months = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago",
            "Sep", "Oct", "Nov", "Dic"]

def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)

class customSqlTableModel(QtSql.QSqlTableModel):
    def __init__(self, parent=None, *args):
        QtSql.QSqlTableModel.__init__(self, parent, *args)

    def data(self, item, role):
        if role == QtCore.Qt.BackgroundRole:
            if QtSql.QSqlTableModel.data(self, self.index(item.row(), 4), QtCore.Qt.DisplayRole) == "Disponible":
                return QtGui.QBrush(QtGui.QColor.fromRgb(29,182, 246))
            elif QtSql.QSqlTableModel.data(self, self.index(item.row(), 4), QtCore.Qt.DisplayRole) == "En cuenta":
                return QtGui.QBrush(QtGui.QColor.fromRgb(174, 213, 81))
            elif QtSql.QSqlTableModel.data(self, self.index(item.row(), 4), QtCore.Qt.DisplayRole) == "Reservado":
                return QtGui.QBrush(QtGui.QColor.fromRgb(234, 189, 190))
        return QtSql.QSqlTableModel.data(self, item, role)

class Ui_MainWindow(object):

    #####################

    #Initialize UI

    ####################
    def setupUi(self, MainWindow):


        #Main window

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(int(1024/1024*WIDTH), int(800/800*HEIGHT))
        MainWindow.setStyleSheet("#centralwidget { background-color: \n"
        "qlineargradient(spread:reflect, x1:0.5, y1:0, x2:0, y2:0,\n"
        "stop:0 rgba(91, 204, 233, 75), stop:1 rgba(32, 80, 96,\n"
        "50)); }\n"
        "#topPanel { background-color:\n"
        "qlineargradient(spread:reflect, x1:0.5, y1:0, x2:0, y2:0,\n"
        "stop:0 rgba(0, 0, 233, 100), stop:1 rgba(0, 0, 96,\n"
        "100)); }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralWidget \n"
        "{ background: rgba(32, 80, 96, 100); }\n"
        "#topPanel_2 \n"
        "{background-color:\n"
        "qlineargradient(spread:reflect, x1:0.5, y1:0, x2:0, y2:0,\n"
        "stop:0 rgba(0, 204, 233, 75), stop:1 rgba(0, 80, 96,\n"
        "75)); }\n"
        "#loginForm\n"
        "{\n"
        "background: rgba(0, 0, 0, 80);\n"
        "border-radius: 8px;\n"
        "}\n"
        "QPushButton\n"
        "{\n"
        "color: white;\n"
        "background-color: #27a9e3;\n"
        "border-width: 0px;\n"
        "border-radius: 3px;\n"
        "}\n"
        "\n"
        "QPushButton:hover \n"
        "\n"
        "{ background-color: #66c011; }\n"
        "\n"
        "QLabel { color: white; }\n"
        "QLineEdit { border-radius: 3px; }\n"
        "QPushButton:disabled {background-color: #ffffff;}")

        #Initialize DB

        self.databaseInit()

        #Login Screen

        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")

        #Stacked Widgets for different pages

        self.stackedWidgets = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidgets.setEnabled(True)
        self.stackedWidgets.setAutoFillBackground(False)
        self.stackedWidgets.setStyleSheet("#loginWidget {background :rgba(255, 255, 198, 0);}")
        self.stackedWidgets.setObjectName("stackedWidgets")

        #Login Screen

        self.loginWidget = QtWidgets.QWidget()
        self.loginWidget.setObjectName("loginWidget")
        self.loginScreenLayout = QtWidgets.QVBoxLayout(self.loginWidget)
        self.loginScreenLayout.setContentsMargins(-1, 1, -1, -1)
        self.loginScreenLayout.setObjectName("loginScreenLayout")
        self.topPanel_2 = QtWidgets.QWidget(self.loginWidget)
        self.topPanel_2.setObjectName("topPanel_2")
        self.topPanel = QtWidgets.QHBoxLayout(self.topPanel_2)
        self.topPanel.setObjectName("topPanel")
        self.currentDateTime = QtWidgets.QLabel(self.topPanel_2)
        self.currentDateTime.setObjectName("currentDateTime")
        self.topPanel.addWidget(self.currentDateTime)
        #spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        #self.topPanel.addItem(spacerItem)
        #self.pushButton = QtWidgets.QPushButton(self.topPanel_2)
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        #self.pushButton.setSizePolicy(sizePolicy)
        #self.pushButton.setMinimumSize(QtCore.QSize(55, 55))
        #self.pushButton.setText("")
        #self.pushButton.setObjectName("pushButton")
        #self.topPanel.addWidget(self.pushButton)
        #self.pushButton_2 = QtWidgets.QPushButton(self.topPanel_2)
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        #self.pushButton_2.setSizePolicy(sizePolicy)
        #self.pushButton_2.setMinimumSize(QtCore.QSize(55, 55))
        #self.pushButton_2.setStyleSheet("border-image: url(:/icons/questionIcon.png) stretch stretch 0 0 0 0")
        #self.pushButton_2.setText("")
        #self.pushButton_2.setObjectName("pushButton_2")
        #self.topPanel.addWidget(self.pushButton_2)
        self.loginScreenLayout.addWidget(self.topPanel_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.loginScreenLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo = QtWidgets.QLabel(self.loginWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(750, 150))
        self.logo.setStyleSheet("background-image:url(:/images/logo.png)")
        self.logo.setText("")
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.horizontalLayout_3.addWidget(self.logo)
        self.loginScreenLayout.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.loginScreenLayout.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.loginForm = QtWidgets.QWidget(self.loginWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginForm.sizePolicy().hasHeightForWidth())
        self.loginForm.setSizePolicy(sizePolicy)
        self.loginForm.setMinimumSize(QtCore.QSize(350, 200))
        self.loginForm.setStyleSheet("#loginForm { border: 1px solid; }")
        self.loginForm.setObjectName("loginForm")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.loginForm)
        self.verticalLayout_2.setContentsMargins(35, 35, 35, 35)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.loginForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(56, 25))
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.loginLineEdit = QtWidgets.QLineEdit(self.loginForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginLineEdit.sizePolicy().hasHeightForWidth())
        self.loginLineEdit.setSizePolicy(sizePolicy)
        self.loginLineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.loginLineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.loginLineEdit.setObjectName("lineEdit")
        self.loginLineEdit.setCursorPosition(0)
        self.horizontalLayout_6.addWidget(self.loginLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.loginForm)
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.passLineEdit = QtWidgets.QLineEdit(self.loginForm)
        self.passLineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.passLineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.passLineEdit.setObjectName("lineEdit_2")
        self.passLineEdit.setEchoMode(2)
        self.horizontalLayout_5.addWidget(self.passLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.loginButton = QtWidgets.QPushButton(self.loginForm)
        self.loginButton.setEnabled(True)
        self.loginLineEdit.returnPressed.connect(self.openMainTabWidget)
        self.passLineEdit.returnPressed.connect(self.openMainTabWidget)
        self.loginButton.clicked.connect(self.openMainTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout_2.addWidget(self.loginButton)
        self.horizontalLayout_4.addWidget(self.loginForm)
        self.loginScreenLayout.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.loginScreenLayout.addItem(spacerItem4)
        self.stackedWidgets.addWidget(self.loginWidget)


        # Admin page - with tabs

        self.adminPage = QtWidgets.QWidget()
        self.adminPage.setEnabled(True)
        self.verticalLayoutWidgetAdmin = QtWidgets.QWidget(self.adminPage)
        self.verticalLayoutWidgetAdmin.setGeometry(QtCore.QRect(int(-1/1024*WIDTH), int(-1/800*HEIGHT), int(1021/1024*WIDTH), int(771/800*HEIGHT)))
        self.verticalLayoutWidgetAdmin.setObjectName("verticalLayoutWidget")
        self.verticalLayoutAdmin = QtWidgets.QVBoxLayout(self.verticalLayoutWidgetAdmin)
        self.verticalLayoutAdmin.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutAdmin.setObjectName("verticalLayoutAdmin")

        # User page - with tabs


        self.userPage = QtWidgets.QWidget()
        self.userPage.setEnabled(True)
        self.verticalLayoutWidgetUser = QtWidgets.QWidget(self.userPage)
        self.verticalLayoutWidgetUser.setGeometry(QtCore.QRect(int(-1/1024*WIDTH), int(-1/800*HEIGHT), int(1021/1024*WIDTH), int(771/800*HEIGHT)))
        self.verticalLayoutWidgetUser.setObjectName("verticalLayoutWidgetUser")
        self.verticalLayoutUser = QtWidgets.QVBoxLayout(self.verticalLayoutWidgetUser)
        self.verticalLayoutUser.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutUser.setObjectName("verticalLayoutUser")


        #Tab widgets

        self.tabWidgetAdmin = QtWidgets.QTabWidget(self.verticalLayoutWidgetAdmin)
        self.tabWidgetAdmin.setObjectName("tabWidget")
        self.tabWidgetAdmin.setStyleSheet("QTabBar:tab { background-color: #5e35b1; \n"
                                    " color: white; \n"
                                    " width: 221 px;} \n "
                                    "QTabBar:tab:hover  {background-color: #66c011;}\n"
                                    "QTabBar:tab:selected {background-color: #27a9e3;}\n    "
                                    "QTabWidget { background-color: #b2ebf2 ; }\n"
                                    "#bomTab { background-color: #b2ebf2;}\n"
                                    "#pedidosTab { background-color: #b2ebf2;}\n"
                                    "#planCompraTab { background-color: #b2ebf2;}\n"
                                    "#prodPlanTab { background-color: #b2ebf2;}\n"
                                    "#usersTab { background-color: #b2ebf2;}\n"
                                    "#inventarioTab { background-color: #b2ebf2;}")
        self.tabWidgetAdmin.setObjectName("adminPage")

        

        self.tabWidgetUser = QtWidgets.QTabWidget(self.verticalLayoutWidgetUser)
        self.tabWidgetUser.setObjectName("tabWidgetUser")
        self.tabWidgetUser.setStyleSheet("QTabBar:tab { background-color: #5e35b1; \n"
                                    " color: white; \n"
                                    " width: 665 px;} \n "
                                    "QTabBar:tab:hover  {background-color: #66c011;}\n"
                                    "QTabBar:tab:selected {background-color: #27a9e3;}\n    "
                                    "QTabWidget { background-color: #b2ebf2 ; }\n"
                                    "#bomTab { background-color: #b2ebf2;}\n"
                                    "#pedidosTab { background-color: #b2ebf2;}\n"
                                    "#planCompraTab { background-color: #b2ebf2;}\n"
                                    "#prodPlanTab { background-color: #b2ebf2;}\n"
                                    "#usersTab { background-color: #b2ebf2;}\n"
                                    "#inventarioTab { background-color: #b2ebf2;}")
        self.tabWidgetUser.setObjectName("userPage")

        #BOM Tab

        self.bomTab = QtWidgets.QWidget()
        self.bomTab.setObjectName("bomTab")

        self.horizontalLayoutWidgetBOM = QtWidgets.QWidget(self.bomTab)
        self.horizontalLayoutWidgetBOM.setGeometry(QtCore.QRect(int(10/1024*WIDTH), int(670/800*HEIGHT), int(991/1024*WIDTH), int(80/800*HEIGHT)))
        self.horizontalLayoutWidgetBOM.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutBOM = QtWidgets.QHBoxLayout(self.horizontalLayoutWidgetBOM)
        self.horizontalLayoutBOM.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutBOM.setObjectName("horizontalLayout")
        self.pushButtonNuevoBOM = QtWidgets.QPushButton(self.horizontalLayoutWidgetBOM)
        self.pushButtonNuevoBOM.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonNuevoBOM.clicked.connect(self.addNewBOM)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonNuevoBOM.setFont(font)
        self.pushButtonNuevoBOM.setObjectName("pushButtonNuevoBOM")
        self.horizontalLayoutBOM.addWidget(self.pushButtonNuevoBOM)
        self.pushButtonEliminarBOM = QtWidgets.QPushButton(self.horizontalLayoutWidgetBOM)
        self.pushButtonEliminarBOM.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonEliminarBOM.clicked.connect(self.deleteBOM)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonEliminarBOM.setFont(font)
        self.pushButtonEliminarBOM.setObjectName("pushButtonEliminarBOM")
        self.horizontalLayoutBOM.addWidget(self.pushButtonEliminarBOM)

        # Tablas de materiales y radiadores
        self.tabsListaDeMateriales = QtWidgets.QTabWidget(self.bomTab)
        self.tabsListaDeMateriales.setGeometry(QtCore.QRect(int(10/1024*WIDTH), int(50/800*HEIGHT), int(991/1024*WIDTH), int(635/800*HEIGHT)))
        self.tabsListaDeMateriales.setObjectName("tabsListaDeMateriales")
        self.tabsListaDeMateriales.setStyleSheet("QTabBar:tab { background-color: #5e35b1; \n"
                                    " color: white; \n"
                                    " width: 650 px;} \n "
                                    "QTabBar:tab:hover  {background-color: #66c011;}\n"
                                    "QTabBar:tab:selected {background-color: #27a9e3;}"
                                    "QTabWidget { background-color: #b2ebf2 ; }\n"
                                    "#bomTab { background-color: #b2ebf2;}")
        self.tabMateriales = QtWidgets.QWidget()
        self.tabMateriales.setObjectName("tabMateriales")
        self.tableMateriales = QtWidgets.QTableView(self.tabMateriales)
        self.tableMateriales.setGeometry(QtCore.QRect(0, 0, int(985/1024*WIDTH), int(600/800*HEIGHT)))
        self.tableMateriales.setShowGrid(True)
        self.tableMateriales.setObjectName("tableMateriales")
        self.tableMateriales.setModel(self.filteredModelTableMats)
        self.tableMateriales.setAlternatingRowColors(True)
        self.tableMateriales.setColumnHidden(0, True)
        self.tableMateriales.verticalHeader().setVisible(False)
        self.tableMateriales.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableMateriales.setSortingEnabled(True)
        self.tableMateriales.sortByColumn(2, 0)
        header = self.tableMateriales.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        for i in range(1,6):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        self.tabsListaDeMateriales.addTab(self.tabMateriales, "Materiales")

        self.tabRadiadores = QtWidgets.QWidget()
        self.tabRadiadores.setObjectName("tabRadiadores")
        self.tableBOM = QtWidgets.QTableView(self.tabRadiadores)
        self.tableBOM.setGeometry(QtCore.QRect(0, 0, int(985/1024*WIDTH), int(600/800*HEIGHT)))
        self.tableBOM.setShowGrid(True)
        self.tableBOM.setObjectName("tableBOM")
        self.tableBOM.setModel(self.filteredModelTableRad)
        self.tableBOM.setAlternatingRowColors(True)
        self.tableBOM.setColumnHidden(0, True)
        self.tableBOM.verticalHeader().setVisible(False)
        self.tableBOM.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableBOM.setSortingEnabled(True)
        self.tableBOM.sortByColumn(1, 0)
        header = self.tableBOM.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        for i in range(1,11):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        self.tabsListaDeMateriales.addTab(self.tabRadiadores, "Radiadores")

        
        

        self.modelDialogCode = QtSql.QSqlQueryModel()
        self.modelDialogCode.setQuery("SELECT code FROM Materiales")
        self.codigoBOMComboBox = QtWidgets.QComboBox(self.bomTab)
        self.codigoBOMComboBox.setGeometry(QtCore.QRect(int(10/1024*WIDTH), int(10/800*HEIGHT), int(980/1024*WIDTH), int(25/800*HEIGHT)))
        self.codigoBOMComboBox.setEditable(True)
        self.codigoBOMComboBox.setModel(self.modelDialogCode)

        self.codigoBOMComboBox.currentTextChanged.connect(self.filteredModelTableMats.setFilterRegExp)
        self.codigoBOMComboBox.currentTextChanged.connect(self.filteredModelTableRad.setFilterRegExp)
        
        #self.tabWidgetAdmin.addTab(self.bomTab, "Lista de materiales")
        #self.tabWidgetUser.addTab(self.bomTab, "Lista de materiales")

        #Production plan tab

        
        #self.modelDialogCode = QtSql.QSqlQueryModel()
        #self.modelDialogCode.setQuery("SELECT code FROM Materiales")
        #self.codigoBOMComboBox = QtWidgets.QComboBox(self.bomTab)
        #self.codigoBOMComboBox.setGeometry(QtCore.QRect(10, 10, 980, 25))
        #self.codigoBOMComboBox.setEditable(True)
        #self.codigoBOMComboBox.setModel(self.modelDialogCode)

        #self.codigoBOMComboBox.currentTextChanged.connect(self.filteredModelTableMats.setFilterRegExp)

        self.prodPlanTab = QtWidgets.QWidget()
        self.prodPlanTab.setObjectName("prodPlanTab")
        self.tableProdPlan = QtWidgets.QTableView(self.prodPlanTab)
        self.tableProdPlan.setGeometry(QtCore.QRect(int(10/1024*WIDTH), int(50/800*HEIGHT), int(990/1024*WIDTH), int(685/800*HEIGHT)))
        self.tableProdPlan.setShowGrid(True)
        self.tableProdPlan.setObjectName("tableProdPlan")
        self.tableProdPlan.setModel(self.filteredProdPlan)
        self.tableProdPlan.setAlternatingRowColors(True)
        self.tableProdPlan.setColumnHidden(0, True)
        self.tableProdPlan.verticalHeader().setVisible(False)
        self.tableProdPlan.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableProdPlan.setSortingEnabled(True)
        self.tableProdPlan.sortByColumn(1, 0)
        header = self.tableProdPlan.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        for i in range(1,10):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        self.tableProdPlan.setObjectName("tableProdPlan")

        self.codigoProdPlanComboBox = QtWidgets.QComboBox(self.prodPlanTab)
        self.codigoProdPlanComboBox.setGeometry(QtCore.QRect(int(10/1024*WIDTH), int(10/800*HEIGHT), int(990/1024*WIDTH), int(25/800*HEIGHT)))
        
        query = QtSql.QSqlQueryModel()
        query.setQuery("SELECT code FROM Radiadores")
        self.codigoProdPlanComboBox.setModel(query)
        self.codigoProdPlanComboBox.setEditable(True)

        self.codigoProdPlanComboBox.currentTextChanged.connect(self.filteredProdPlan.setFilterRegExp)


        #Inventory tab

        self.inventarioTab = QtWidgets.QWidget()
        self.inventarioTab.setObjectName("inventarioTab")
        
        self.codigoInventarioComboBox = QtWidgets.QComboBox(self.inventarioTab)
        self.codigoInventarioComboBox.setGeometry(QtCore.QRect(int(10/1024*WIDTH), int(10/800*HEIGHT), int(980/1024*WIDTH), int(25/800*HEIGHT)))
        self.codigoInventarioComboBox.setEditable(True)
        self.codigoInventarioComboBox.setModel(self.modelDialogCode)

        self.codigoInventarioComboBox.currentTextChanged.connect(self.filteredTableInvSobr.setFilterRegExp)
        self.codigoInventarioComboBox.currentTextChanged.connect(self.filteredTableInvLote.setFilterRegExp)


        
        self.horizontalLayoutWidgetInventario = QtWidgets.QWidget(self.inventarioTab)
        self.horizontalLayoutWidgetInventario.setGeometry(QtCore.QRect(int(10/1024*WIDTH), int(670/800*HEIGHT), int(991/1024*WIDTH), int(80/800*HEIGHT)))
        self.horizontalLayoutWidgetInventario.setObjectName("horizontalLayoutWidgetInventario")
        self.horizontalLayoutInventario = QtWidgets.QHBoxLayout(self.horizontalLayoutWidgetInventario)
        self.horizontalLayoutInventario.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutInventario.setObjectName("horizontalLayout")
        self.pushButtonNuevoInventario = QtWidgets.QPushButton(self.horizontalLayoutWidgetInventario)
        self.pushButtonNuevoInventario.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonNuevoInventario.clicked.connect(self.addNewInventario)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonNuevoInventario.setFont(font)
        self.pushButtonNuevoInventario.setObjectName("pushButtonNuevoInventario")
        self.horizontalLayoutInventario.addWidget(self.pushButtonNuevoInventario)
        self.pushButtonEliminarInventario = QtWidgets.QPushButton(self.horizontalLayoutWidgetInventario)
        self.pushButtonEliminarInventario.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonEliminarInventario.clicked.connect(self.deleteInventario)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonEliminarInventario.setFont(font)
        self.pushButtonEliminarInventario.setObjectName("pushButtonEliminarInventario")
        self.horizontalLayoutInventario.addWidget(self.pushButtonEliminarInventario)

        self.tabsInventarios = QtWidgets.QTabWidget(self.inventarioTab)
        self.tabsInventarios.setGeometry(QtCore.QRect(int(10/1024*WIDTH), int(50/800*HEIGHT), int(991/1024*WIDTH), int(611/800*HEIGHT)))
        self.tabsInventarios.setObjectName("tabsInventarios")
        self.tabsInventarios.setStyleSheet("QTabBar:tab { background-color: #5e35b1; \n"
                                    " color: white; \n"
                                    " width: 650 px;} \n "
                                    "QTabBar:tab:hover  {background-color: #66c011;}\n"
                                    "QTabBar:tab:selected {background-color: #27a9e3;}"
                                    "QTabWidget { background-color: #b2ebf2 ; }\n"
                                    "#bomTab { background-color: #b2ebf2;}")
        self.tabLote = QtWidgets.QWidget()
        self.tabLote.setObjectName("tabLote")
        self.tableLote = QtWidgets.QTableView(self.tabLote)
        self.tableLote.setGeometry(QtCore.QRect(0, 0, int(985/1024*WIDTH), int(585/800*HEIGHT)))
        self.tableLote.setShowGrid(True)
        self.tableLote.setObjectName("tableMateriales")
        self.tableLote.setModel(self.filteredTableInvLote)
        self.tableLote.setAlternatingRowColors(True)
        self.tableLote.setColumnHidden(0, True)
        self.tableLote.verticalHeader().setVisible(False)
        self.tableLote.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableLote.setSortingEnabled(True)
        self.tableLote.sortByColumn(2, 0)
        header = self.tableLote.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        for i in range(1,3):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        self.tabsInventarios.addTab(self.tabLote, "Lote completo")

        self.tabSobrantes = QtWidgets.QWidget()
        self.tabSobrantes.setObjectName("tabSobrantes")
        self.tableSobrantes = QtWidgets.QTableView(self.tabSobrantes)
        self.tableSobrantes.setGeometry(QtCore.QRect(0, 0, int(985/1024*WIDTH), int(585/800*HEIGHT)))
        self.tableSobrantes.setShowGrid(True)
        self.tableSobrantes.setObjectName("tableSobrantes")
        self.tableSobrantes.setModel(self.filteredTableInvSobr)
        self.tableSobrantes.setAlternatingRowColors(True)
        self.tableSobrantes.setColumnHidden(0, True)
        self.tableSobrantes.verticalHeader().setVisible(False)
        self.tableSobrantes.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableSobrantes.setSortingEnabled(True)
        self.tableSobrantes.sortByColumn(1, 0)
        header = self.tableSobrantes.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        for i in range(1,5):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        self.tabsInventarios.addTab(self.tabSobrantes, "Sobrantes")
        
        #self.tabWidgetAdmin.addTab(self.inventarioTab, "Inventario")
        #self.tabWidgetUser.addTab(self.inventarioTab, "Inventario")

        #Seguimiento tab

        self.pedidosTab = QtWidgets.QWidget()
        self.pedidosTab.setObjectName("pedidosTab")
        self.tableSeguim = QtWidgets.QTableView(self.pedidosTab)
        self.tableSeguim.setGeometry(QtCore.QRect(int(10/1024*WIDTH), int(70/800*HEIGHT), int(991/1024*WIDTH), int(611/800*HEIGHT)))
        self.tableSeguim.setObjectName("tableSeguim")
        self.tableSeguim.setModel(self.pedidosFilteredOnPedidoCode)
        self.tableSeguim.setAlternatingRowColors(True)
        self.tableSeguim.setColumnHidden(0, True)
        self.tableSeguim.verticalHeader().setVisible(False)
        self.tableSeguim.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableSeguim.setSortingEnabled(True)
        self.tableSeguim.sortByColumn(1, 0)
        header = self.tableSeguim.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        for i in range(1,11):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

            
        self.horizontalLayoutWidgetPedidos = QtWidgets.QWidget(self.pedidosTab)
        self.horizontalLayoutWidgetPedidos.setGeometry(QtCore.QRect(int(10/1024*WIDTH), int(670/800*HEIGHT), int(991/1024*WIDTH), int(80/800*HEIGHT)))
        self.horizontalLayoutWidgetPedidos.setObjectName("horizontalLayoutWidgetPedidos")
        self.horizontalLayoutPedidos = QtWidgets.QHBoxLayout(self.horizontalLayoutWidgetPedidos)
        self.horizontalLayoutPedidos.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutPedidos.setObjectName("horizontalLayout")
        self.pushButtonNuevoPedidos = QtWidgets.QPushButton(self.horizontalLayoutWidgetPedidos)
        self.pushButtonNuevoPedidos.setMinimumSize(QtCore.QSize(0, 50))
        #self.pushButtonNuevoPedidos.clicked.connect(self.addNewPedidos)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonNuevoPedidos.setFont(font)
        self.pushButtonNuevoPedidos.setObjectName("pushButtonNuevoInventario")
        self.pushButtonNuevoPedidos.clicked.connect(self.addNewPedidos)
        self.horizontalLayoutPedidos.addWidget(self.pushButtonNuevoPedidos)

        self.pushButtonEliminarPedidos = QtWidgets.QPushButton(self.horizontalLayoutWidgetPedidos)
        self.pushButtonEliminarPedidos.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonEliminarPedidos.clicked.connect(self.deletePedidos)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonEliminarPedidos.setFont(font)
        self.pushButtonEliminarPedidos.setObjectName("pushButtonEliminarInventario")
        self.horizontalLayoutPedidos.addWidget(self.pushButtonEliminarPedidos)

        self.pushButtonActualizarPedidos = QtWidgets.QPushButton(self.horizontalLayoutWidgetPedidos)
        self.pushButtonActualizarPedidos.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonActualizarPedidos.clicked.connect(self.actualizePedidos)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonActualizarPedidos.setFont(font)
        self.pushButtonActualizarPedidos.setObjectName("pushButtonEliminarInventario")
        self.horizontalLayoutPedidos.addWidget(self.pushButtonActualizarPedidos)

        
        
        self.modelCodeCode = QtSql.QSqlQueryModel()
        self.modelCodeCode.setQuery("SELECT code FROM Materiales")
        self.codigoPedidosComboBox = QtWidgets.QComboBox(self.pedidosTab)
        self.codigoPedidosComboBox.setGeometry(QtCore.QRect(int(10/1024*WIDTH), int(10/800*HEIGHT), int(475/1024*WIDTH), int(25/800*HEIGHT)))
        self.codigoPedidosComboBox.setEditable(True)
        self.codigoPedidosComboBox.setModel(self.modelCodeCode)

        self.codigoPedidosComboBox.currentTextChanged.connect(self.pedidosFilteredOnCode.setFilterRegExp)
        
        self.modelPedidoCode = QtSql.QSqlQueryModel()
        self.modelPedidoCode.setQuery("SELECT DISTINCT p_code FROM Pedidos")
        self.pedidoPedidosComboBox = QtWidgets.QComboBox(self.pedidosTab)
        self.pedidoPedidosComboBox.setGeometry(QtCore.QRect(int(510/1024*WIDTH), int(10/800*HEIGHT), int(475/1024*WIDTH), int(25/800*HEIGHT)))
        self.pedidoPedidosComboBox.setEditable(True)
        self.pedidoPedidosComboBox.setModel(self.modelPedidoCode)

        self.pedidoPedidosComboBox.currentTextChanged.connect(self.pedidosFilteredOnPedidoCode.setFilterRegExp)

        #self.tabWidgetUser.addTab(self.pedidosTab, "Seguimiento de pedidos")

        #Buying plan tab

        self.planCompraTab = QtWidgets.QWidget()
        self.planCompraTab.setObjectName("planCompraTab")

        self.tableWidgetPlanCompra = QtWidgets.QTableWidget(self.planCompraTab)
        self.tableWidgetPlanCompra.setGeometry(QtCore.QRect(int(10/1024*WIDTH), int(50/800*HEIGHT), int(750/1024*WIDTH), int(250/800*HEIGHT)))
        
        self.nombreCompraComboBox = QtWidgets.QComboBox(self.planCompraTab)
        self.nombreCompraComboBox.setGeometry(QtCore.QRect(int(10/1024*WIDTH), int(10/800*HEIGHT), int(480/1024*WIDTH), int(25/800*HEIGHT)))
        self.nombreCompraComboBox.setEditable(True)
        self.modelDialogName = QtSql.QSqlQueryModel()
        self.modelDialogName.setQuery("SELECT DISTINCT name FROM Materiales")
        self.nombreCompraComboBox.setModel(self.modelDialogName)     
        self.nombreCompraComboBox.currentTextChanged.connect(self.populateCodigoCompraComboBox)

        self.modelDialogCode = QtSql.QSqlQueryModel()
        self.modelDialogCode.setQuery("SELECT code FROM Materiales WHERE name = 'Rollo' ".format(self.nombreCompraComboBox.currentText()))
        self.codigoCompraComboBox = QtWidgets.QComboBox(self.planCompraTab)
        self.codigoCompraComboBox.setGeometry(QtCore.QRect(int(510/1024*WIDTH), int(10/800*HEIGHT), int(480/1024*WIDTH), int(25/800*HEIGHT)))
        self.codigoCompraComboBox.setEditable(True)
        self.codigoCompraComboBox.setModel(self.modelDialogCode)
        self.codigoCompraComboBox.currentTextChanged.connect(self.populateTablaPlanCompras)

        
        self.tableWidgetPlanCompra.setRowCount(11)
        self.tableWidgetPlanCompra.setColumnCount(9)
        self.tableWidgetPlanCompra.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        self.tableWidgetPlanCompra.setItem(0,0, QtWidgets.QTableWidgetItem("Req. Bruto"))
        self.tableWidgetPlanCompra.setItem(1,0, QtWidgets.QTableWidgetItem("Pend. Ingreso"))
        self.tableWidgetPlanCompra.setItem(2,0, QtWidgets.QTableWidgetItem("Pedido"))
        self.tableWidgetPlanCompra.setItem(3,0, QtWidgets.QTableWidgetItem("Viajando"))
        self.tableWidgetPlanCompra.setItem(4,0, QtWidgets.QTableWidgetItem("Deposito Fiscal"))
        self.tableWidgetPlanCompra.setItem(5,0, QtWidgets.QTableWidgetItem("Retirado"))
        self.tableWidgetPlanCompra.setItem(6,0, QtWidgets.QTableWidgetItem("En fábrica"))
        self.tableWidgetPlanCompra.item(2,0).setTextAlignment(3)
        self.tableWidgetPlanCompra.item(3,0).setTextAlignment(3)
        self.tableWidgetPlanCompra.item(4,0).setTextAlignment(3)
        self.tableWidgetPlanCompra.item(5,0).setTextAlignment(3)
        self.tableWidgetPlanCompra.item(6,0).setTextAlignment(3)
        self.tableWidgetPlanCompra.setItem(7,0, QtWidgets.QTableWidgetItem("Inventario"))
        self.tableWidgetPlanCompra.setItem(8,0, QtWidgets.QTableWidgetItem("Req. Netos"))
        self.tableWidgetPlanCompra.setItem(9,0, QtWidgets.QTableWidgetItem("Ing. planificados"))
        self.tableWidgetPlanCompra.setItem(10,0, QtWidgets.QTableWidgetItem("Emision de pedidos"))
        
        #self.tableWidgetPlanCompra.cellDoubleClicked.connect(self.doubleClickedOnPendiente)

        self.tableWidgetMaterial = QtWidgets.QTableWidget(self.planCompraTab)
        self.tableWidgetMaterial.setGeometry(QtCore.QRect(int(770/1024*WIDTH), int(50/800*HEIGHT), int(220/1024*WIDTH), int(250/800*HEIGHT)))
        self.tableWidgetMaterial.setRowCount(6)
        self.tableWidgetMaterial.setColumnCount(2)
        
        self.tableWidgetMaterial.verticalHeader().setVisible(False)
        self.tableWidgetMaterial.setAlternatingRowColors(True)

        header = self.tableWidgetMaterial.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        for i in range(2):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        self.rowsHidden = 0
        
        self.pushButtonObtenerProdPlan = QtWidgets.QPushButton(self.planCompraTab)
        self.pushButtonObtenerProdPlan.setGeometry(QtCore.QRect(int(10/1024*WIDTH), int(330/800*HEIGHT), int(980/1024*WIDTH), int(25/800*HEIGHT)))
        self.pushButtonObtenerProdPlan.clicked.connect(self.generatePlanDeCompras)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonObtenerProdPlan.setFont(font)
        self.pushButtonObtenerProdPlan.setObjectName("pushButtonObtenerProdPlan")
        #   self.planCompraTab.addWidget(self.pushButtonObtenerProdPlan)


        
        #self.tabWidgetUser.addTab(self.planCompraTab, "")

        #Users tab

        self.usersTab = QtWidgets.QWidget()
        self.usersTab.setObjectName("usersTab")
        self.tableUsers = QtWidgets.QTableView(self.usersTab)
        self.tableUsers.setGeometry(QtCore.QRect(int(10/1024*WIDTH), int(10/800*HEIGHT), int(985/1024*WIDTH), int(635/800*HEIGHT)))
        self.tableUsers.setShowGrid(True)
        self.tableUsers.setObjectName("tableUsers")
        self.tableUsers.setModel(self.modelTableUsers)
        self.tableUsers.setAlternatingRowColors(True)
        self.tableUsers.setColumnHidden(0, True)
        self.tableUsers.verticalHeader().setVisible(False)
        self.tableUsers.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableUsers.setSortingEnabled(True)
        self.tableUsers.sortByColumn(1, 0)
        header = self.tableUsers.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        for i in range(1,4):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

            

        self.horizontalLayoutWidgetUsers = QtWidgets.QWidget(self.usersTab)
        self.horizontalLayoutWidgetUsers.setGeometry(QtCore.QRect(int(10/1024*WIDTH), int(670/800*HEIGHT), int(991/1024*WIDTH), int(80/800*HEIGHT)))
        self.horizontalLayoutWidgetUsers.setObjectName("horizontalLayoutWidgetUsers")
        self.horizontalLayoutUsers = QtWidgets.QHBoxLayout(self.horizontalLayoutWidgetUsers)
        self.horizontalLayoutUsers.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutUsers.setObjectName("horizontalLayout")
        self.pushButtonNuevoUsers = QtWidgets.QPushButton(self.horizontalLayoutWidgetUsers)
        self.pushButtonNuevoUsers.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonNuevoUsers.clicked.connect(self.addNewUser)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonNuevoUsers.setFont(font)
        self.pushButtonNuevoUsers.setObjectName("pushButtonNuevoUsers")
        self.horizontalLayoutUsers.addWidget(self.pushButtonNuevoUsers)
        self.pushButtonEliminarUsers = QtWidgets.QPushButton(self.horizontalLayoutWidgetUsers)
        self.pushButtonEliminarUsers.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButtonEliminarUsers.clicked.connect(self.deleteUser)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonEliminarUsers.setFont(font)
        self.pushButtonEliminarUsers.setObjectName("pushButtonEliminarUsers")
        self.horizontalLayoutUsers.addWidget(self.pushButtonEliminarUsers)

        self.verticalLayoutAdmin.addWidget(self.tabWidgetAdmin)
        self.verticalLayoutUser.addWidget(self.tabWidgetUser)
        self.stackedWidgets.addWidget(self.adminPage)
        self.stackedWidgets.addWidget(self.userPage)
        self.verticalLayout.addWidget(self.stackedWidgets)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidgets.setCurrentIndex(0)
        self.tabWidgetAdmin.setCurrentIndex(0)
        
        self.populateTablaPlanCompras()
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #self.generatePlanDeCompras()
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FACORSA"))
        self.currentDateTime.setText(_translate("MainWindow", datetime.date.today().strftime("%m/%d/%Y, %H:%M:%S")))
        self.label.setText(_translate("MainWindow", "Usuario"))
        self.label_2.setText(_translate("MainWindow", "Contraseña"))
        self.loginButton.setText(_translate("MainWindow", "Entrar"))
        #self.pushButtonMaterial.setText(_translate("MainWindow", "Material"))
        #self.pushButtonRadiador.setText(_translate("MainWindow", "Radiador"))
        self.pushButtonNuevoBOM.setText(_translate("MainWindow", "Nuevo"))
        self.pushButtonEliminarBOM.setText(_translate("MainWindow", "Eliminar"))
        self.pushButtonNuevoUsers.setText(_translate("MainWindow", "Nuevo"))
        self.pushButtonEliminarUsers.setText(_translate("MainWindow", "Eliminar"))
        self.pushButtonObtenerProdPlan.setText(_translate("MainWindow", "Generar Plan de Compras"))
        self.tabWidgetAdmin.setTabText(self.tabWidgetAdmin.indexOf(self.bomTab), _translate("MainWindow", "Lista de materiales"))
        self.tabWidgetAdmin.setTabText(self.tabWidgetUser.indexOf(self.bomTab), _translate("MainWindow", "Lista de materiales"))
        self.tabWidgetAdmin.setTabText(self.tabWidgetAdmin.indexOf(self.prodPlanTab), _translate("MainWindow", "Plan de Producción"))
        self.pushButtonNuevoInventario.setText(_translate("MainWindow", "Nuevo"))
        self.pushButtonEliminarInventario.setText(_translate("MainWindow", "Eliminar"))
        self.tabWidgetAdmin.setTabText(self.tabWidgetAdmin.indexOf(self.inventarioTab), _translate("MainWindow", "Inventario"))
        self.tabWidgetAdmin.setTabText(self.tabWidgetAdmin.indexOf(self.pedidosTab), _translate("MainWindow", "Seguimiento de pedidos"))
        self.tabWidgetAdmin.setTabText(self.tabWidgetUser.indexOf(self.pedidosTab), _translate("MainWindow", "Seguimiento de pedidos"))
        self.tabWidgetAdmin.setTabText(self.tabWidgetAdmin.indexOf(self.planCompraTab), _translate("MainWindow", "Plan de compra"))
        self.tabWidgetAdmin.setTabText(self.tabWidgetAdmin.indexOf(self.usersTab), _translate("MainWindow", "Gestionar usuarios"))
        self.pushButtonNuevoPedidos.setText(_translate("MainWindow", "Nuevo"))
        self.pushButtonEliminarPedidos.setText(_translate("MainWindow", "Eliminar"))
        self.pushButtonActualizarPedidos.setText(_translate("MainWindow", "Actualizar"))

    def openMainTabWidget(self):
        
        query = QtSql.QSqlQueryModel()
        user = self.loginLineEdit.text()
        password = self.passLineEdit.text()
        #print(user)
        query.setQuery("SELECT * FROM Usuarios WHERE user = '{}'".format(user))
        if query.record(0).value(0) == None:
            msg = QtWidgets.QMessageBox()
            msg.setText("Error")
            msg.setInformativeText('No se encontró el usuario')
            msg.setWindowTitle("Error")
            msg.exec_()

        elif password != query.record(0).value(2):
            msg = QtWidgets.QMessageBox()
            msg.setText("Error")
            msg.setInformativeText('Contraseña incorrecta')
            msg.setWindowTitle("Error")
            msg.exec_()

        elif query.record(0).value(3) == 'gerente':
            self.stackedWidgets.setCurrentIndex(1)
            self.tabWidgetAdmin.addTab(self.inventarioTab, "Inventario")
            self.tabWidgetAdmin.addTab(self.bomTab, 'Lista de materiales')
            self.tabWidgetAdmin.addTab(self.prodPlanTab, "Plan de produccion")
            self.tabWidgetAdmin.addTab(self.pedidosTab, "Seguimiento de pedidos")
            self.tabWidgetAdmin.addTab(self.planCompraTab, "Generar plan de compra")
            self.tabWidgetAdmin.addTab(self.usersTab, "Gestionar usuarios")

        elif query.record(0).value(3) == 'operario':            
            self.stackedWidgets.setCurrentIndex(2)
            self.tabWidgetUser.addTab(self.inventarioTab, "Inventario")
            self.tabWidgetUser.addTab(self.bomTab, 'Lista de materiales')

    def databaseInit(self):

        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('db.db')
        self.modelTableRads = QtSql.QSqlTableModel()
        self.query = QtSql.QSqlQuery()
        self.modelTableRads.setTable('Radiadores')
        self.modelTableRads.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.modelTableRads.select()


        self.modelTableRads.setHeaderData(1, QtCore.Qt.Horizontal, "Código")
        self.modelTableRads.setHeaderData(2, QtCore.Qt.Horizontal, "Rollo")
        self.modelTableRads.setHeaderData(3, QtCore.Qt.Horizontal, "Cant")
        self.modelTableRads.setHeaderData(4, QtCore.Qt.Horizontal, "Tubo")
        self.modelTableRads.setHeaderData(5, QtCore.Qt.Horizontal, "Cant")
        self.modelTableRads.setHeaderData(6, QtCore.Qt.Horizontal, "Usa Lat?")
        self.modelTableRads.setHeaderData(7, QtCore.Qt.Horizontal, "Cant Lat")
        self.modelTableRads.setHeaderData(8, QtCore.Qt.Horizontal, "Usa Turb?")
        self.modelTableRads.setHeaderData(9, QtCore.Qt.Horizontal, "Cant")
        self.modelTableRads.setHeaderData(10, QtCore.Qt.Horizontal, "Espesor")

        
        self.modelTableMats = QtSql.QSqlTableModel()
        self.modelTableMats.setTable('Materiales')
        self.modelTableMats.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.modelTableMats.select()

        self.filteredModelTableMats = QtCore.QSortFilterProxyModel()
        self.filteredModelTableMats.setSourceModel(self.modelTableMats)
        self.filteredModelTableMats.setFilterKeyColumn(1)

        self.filteredModelTableRad = QtCore.QSortFilterProxyModel()
        self.filteredModelTableRad.setSourceModel(self.modelTableRads)
        self.filteredModelTableRad.setFilterKeyColumn(1)


        self.modelTableMats.setHeaderData(1, QtCore.Qt.Horizontal, "Código")
        self.modelTableMats.setHeaderData(2, QtCore.Qt.Horizontal, "Nombre")
        self.modelTableMats.setHeaderData(3, QtCore.Qt.Horizontal, "Tiempo de suministro")
        self.modelTableMats.setHeaderData(4, QtCore.Qt.Horizontal, "Stock de seguridad")
        self.modelTableMats.setHeaderData(5, QtCore.Qt.Horizontal, "Lote minimo")
        self.modelTableMats.setHeaderData(6, QtCore.Qt.Horizontal, "Nivel")
        self.modelTableMats.setHeaderData(7, QtCore.Qt.Horizontal, "Unidad de medida")


        self.modelTableInvLote = QtSql.QSqlTableModel()
        self.modelTableInvLote.setTable('InventarioLote')
        self.modelTableInvLote.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.modelTableInvLote.select()

        self.modelTableInvLote.setHeaderData(1, QtCore.Qt.Horizontal, "Código")
        self.modelTableInvLote.setHeaderData(2, QtCore.Qt.Horizontal, "Cantidad")

        
        self.modelTableInvSobr = customSqlTableModel()
        self.modelTableInvSobr.setTable('InventarioSobrantes')
        self.modelTableInvSobr.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.modelTableInvSobr.select()

        self.modelTableInvSobr.setHeaderData(1, QtCore.Qt.Horizontal, "Código")
        self.modelTableInvSobr.setHeaderData(2, QtCore.Qt.Horizontal, "Nombre")
        self.modelTableInvSobr.setHeaderData(3, QtCore.Qt.Horizontal, "Cantidad")
        self.modelTableInvSobr.setHeaderData(4, QtCore.Qt.Horizontal, "Estado")

        
        self.filteredTableInvSobr = QtCore.QSortFilterProxyModel()
        self.filteredTableInvSobr.setSourceModel(self.modelTableInvSobr)
        self.filteredTableInvSobr.setFilterKeyColumn(1)

        self.filteredTableInvLote = QtCore.QSortFilterProxyModel()
        self.filteredTableInvLote.setSourceModel(self.modelTableInvLote)
        self.filteredTableInvLote.setFilterKeyColumn(1)

        
        self.modelTableProdPlan = QtSql.QSqlTableModel()
        self.modelTableProdPlan.setTable('PlanProduccion')
        self.modelTableProdPlan.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.modelTableProdPlan.select()

        
        self.modelTableProdPlan.setHeaderData(1, QtCore.Qt.Horizontal, "Código")
        self.modelTableProdPlan.setHeaderData(2, QtCore.Qt.Horizontal, months[datetime.date.today().month-1]+", "+"{}".format(datetime.date.today().year))
        self.modelTableProdPlan.setHeaderData(3, QtCore.Qt.Horizontal, months[add_months(datetime.date.today(),1).month-1]+", "+str(add_months(datetime.date.today(),1).year))
        self.modelTableProdPlan.setHeaderData(4, QtCore.Qt.Horizontal, months[add_months(datetime.date.today(),2).month-1]+", "+str(add_months(datetime.date.today(),2).year))
        self.modelTableProdPlan.setHeaderData(5, QtCore.Qt.Horizontal, months[add_months(datetime.date.today(),3).month-1]+", "+str(add_months(datetime.date.today(),3).year))
        self.modelTableProdPlan.setHeaderData(6, QtCore.Qt.Horizontal, months[add_months(datetime.date.today(),4).month-1]+", "+str(add_months(datetime.date.today(),4).year))
        self.modelTableProdPlan.setHeaderData(7, QtCore.Qt.Horizontal, months[add_months(datetime.date.today(),5).month-1]+", "+str(add_months(datetime.date.today(),5).year))
        self.modelTableProdPlan.setHeaderData(8, QtCore.Qt.Horizontal, months[add_months(datetime.date.today(),6).month-1]+", "+str(add_months(datetime.date.today(),6).year))
        self.modelTableProdPlan.setHeaderData(9, QtCore.Qt.Horizontal, months[add_months(datetime.date.today(),7).month-1]+", "+str(add_months(datetime.date.today(),7).year))


        self.filteredProdPlan = QtCore.QSortFilterProxyModel()
        self.filteredProdPlan.setSourceModel(self.modelTableProdPlan)
        self.filteredProdPlan.setFilterKeyColumn(1)

        self.modelTablePedidos = QtSql.QSqlTableModel()
        self.modelTablePedidos.setTable('Pedidos')
        self.modelTablePedidos.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.modelTablePedidos.select()


        
        self.modelTablePedidos.setHeaderData(1, QtCore.Qt.Horizontal, "Nombre")
        self.modelTablePedidos.setHeaderData(2, QtCore.Qt.Horizontal, "Código")
        self.modelTablePedidos.setHeaderData(3, QtCore.Qt.Horizontal, "Cantidad")
        self.modelTablePedidos.setHeaderData(4, QtCore.Qt.Horizontal, "Cód. pedido")
        self.modelTablePedidos.setHeaderData(5, QtCore.Qt.Horizontal, "Estado")
        self.modelTablePedidos.setHeaderData(6, QtCore.Qt.Horizontal, "F. pedido")
        self.modelTablePedidos.setHeaderData(7, QtCore.Qt.Horizontal, "F. viajando")
        self.modelTablePedidos.setHeaderData(8, QtCore.Qt.Horizontal, "F. Depósito")
        self.modelTablePedidos.setHeaderData(9, QtCore.Qt.Horizontal, "F. Retirado")
        self.modelTablePedidos.setHeaderData(10, QtCore.Qt.Horizontal, "F. Ingreso")

        self.pedidosFilteredOnCode = QtCore.QSortFilterProxyModel()
        self.pedidosFilteredOnCode.setSourceModel(self.modelTablePedidos)
        self.pedidosFilteredOnCode.setFilterKeyColumn(2)

        self.pedidosFilteredOnPedidoCode = QtCore.QSortFilterProxyModel()
        self.pedidosFilteredOnPedidoCode.setSourceModel(self.pedidosFilteredOnCode)
        self.pedidosFilteredOnPedidoCode.setFilterKeyColumn(4)

        self.modelTableUsers = QtSql.QSqlTableModel()
        self.modelTableUsers.setTable('Usuarios')      
        self.modelTableUsers.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.modelTableUsers.select()

        self.modelTableUsers.setHeaderData(1, QtCore.Qt.Horizontal, "Usuario")
        self.modelTableUsers.setHeaderData(2, QtCore.Qt.Horizontal, "Contraseña")
        self.modelTableUsers.setHeaderData(3, QtCore.Qt.Horizontal, "Tipo")

    def addNewBOM(self):
        if self.tabsListaDeMateriales.currentIndex() == 1:

            self.dialog = QtWidgets.QDialog()
            self.dialog.ui = dialogNewRadiador.Ui_Dialog()
            self.dialog.ui.setupUi(self.dialog)

            modelDialogBOMRollo = QtSql.QSqlQueryModel()
            modelDialogBOMRollo.setQuery("SELECT code FROM Materiales WHERE name = 'Rollo'")
            modelDialogBOMTubo = QtSql.QSqlQueryModel()
            modelDialogBOMTubo.setQuery("SELECT code FROM Materiales WHERE name = 'Tubo'")
            self.dialog.ui.rolloComboBox.setModel(modelDialogBOMRollo)
            self.dialog.ui.tubosComboBox.setModel(modelDialogBOMTubo)
            self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.dialog.ui.aceptarButton.clicked.connect(self.acceptDialogNewRadiador)
            self.dialog.ui.cancelarButton.clicked.connect(self.dialog.reject)
            self.dialog.exec_()
        elif self.tabsListaDeMateriales.currentIndex() == 0:
            

            self.dialog = QtWidgets.QDialog()
            self.dialog.ui = dialogNewMaterial.Ui_Dialog()
            self.dialog.ui.setupUi(self.dialog)

            modelDialogBOMName = QtSql.QSqlQueryModel()
            modelDialogBOMName.setQuery("SELECT DISTINCT name FROM Materiales")
            self.dialog.ui.nombreComboBox.setModel(modelDialogBOMName)
            self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.dialog.ui.aceptarButton.clicked.connect(self.acceptDialogNewMaterial)
            self.dialog.ui.cancelarButton.clicked.connect(self.dialog.reject)
            self.dialog.exec_()

    def addNewInventario(self):
        if self.tabsInventarios.currentIndex() == 0:

            self.dialog = QtWidgets.QDialog()
            self.dialog.ui = dialogNewInventarioLote.Ui_Dialog()
            self.dialog.ui.setupUi(self.dialog)

            #modelDialogNombre = QtSql.QSqlQueryModel()
            #modelDialogNombre.setQuery("SELECT DISTINCT name FROM Materiales")
            #self.dialog.ui.nombreComboBox.setModel(modelDialogNombre)
            self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.dialog.ui.aceptarButton.clicked.connect(self.acceptDialogNewInventarioLote)
            self.dialog.ui.cancelarButton.clicked.connect(self.dialog.reject)
            self.dialog.exec_()

        elif self.tabsInventarios.currentIndex() == 1:
            

            self.dialog = QtWidgets.QDialog()
            self.dialog.ui = dialogNewInventarioSobr.Ui_Dialog()
            self.dialog.ui.setupUi(self.dialog)

            modelDialogBOMName = QtSql.QSqlQueryModel()
            modelDialogBOMName.setQuery("SELECT DISTINCT name FROM Materiales")
            self.dialog.ui.nombreComboBox.setModel(modelDialogBOMName)

            modelDialogColor = QtSql.QSqlQueryModel()
            modelDialogColor.setQuery("SELECT DISTINCT color FROM InventarioSobrantes")
            self.dialog.ui.colorComboBox.setModel(modelDialogColor)
            self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.dialog.ui.aceptarButton.clicked.connect(self.acceptDialogNewInventarioSobr)
            self.dialog.ui.cancelarButton.clicked.connect(self.dialog.reject)
            self.dialog.exec_()

    def deleteBOM(self):
        
        if self.tabsListaDeMateriales.currentIndex() == 1:
            model = self.filteredModelTableRad
            indices = self.tableBOM.selectionModel().selectedRows() 
            for index in sorted(indices):
                model.removeRow(index.row())

            self.modelTableRads.select()

        elif self.tabsListaDeMateriales.currentIndex() == 0:
            model = self.filteredModelTableMats
            indices = self.tableMateriales.selectionModel().selectedRows() 
            for index in sorted(indices):
                model.removeRow(index.row())

            self.modelTableMats.select()

    def deleteInventario(self):

        if self.tabsInventarios.currentIndex() == 1:
            model = self.filteredTableInvLote
            indices = self.tableLote.selectionModel().selectedRows()
            for index in sorted(indices):
                model.removeRow(index.row())
            
            self.modelTableInvLote.select()

    
        elif self.tabsInventarios.currentIndex() == 0:
            model = self.filteredTableInvSobr
            indices = self.tableSobrantes.selectionModel().selectedRows()
            for index in sorted(indices):
                model.removeRow(index.row())
            
            self.modelTableInvSobr.select()

    def addNewPedidos(self):
        
        self.dialog = QtWidgets.QDialog()
        self.dialog.ui = dialogNewPedido.Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        
        modelDialogCode = QtSql.QSqlQueryModel()
        modelDialogCode.setQuery("SELECT code FROM Materiales")
    
        self.dialog.ui.tableWidget.setColumnCount(3)
        self.dialog.ui.tableWidget.setRowCount(modelDialogCode.rowCount())
        self.dialog.ui.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Código"))
        self.dialog.ui.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Cant. sugerida"))
        self.dialog.ui.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Cant. final"))

        
        rows_list = []

        for name in range(self.nombreCompraComboBox.count()):
            
            self.nombreCompraComboBox.setCurrentIndex(name)

            for codigo in range(self.codigoCompraComboBox.count()):

                self.codigoCompraComboBox.setCurrentIndex(codigo)
                

                nombreText = self.nombreCompraComboBox.currentText()
                codigoText = self.codigoCompraComboBox.currentText()
                emisionPedido = self.tableWidgetPlanCompra.item(10,1).text()
                reqBruto = self.tableWidgetPlanCompra.item(0,4).text()
                reqNeto = self.tableWidgetPlanCompra.item(8,4).text()
                inventario = self.tableWidgetPlanCompra.item(7,4).text()
                pendienteIngreso = self.tableWidgetPlanCompra.item(1,4).text()

                modelDialogCode.setQuery("SELECT id FROM Materiales WHERE code = '{}'".format(codigoText))

                self.dialog.ui.tableWidget.setItem(modelDialogCode.record(0).value(0), 0, QtWidgets.QTableWidgetItem("{}".format(codigoText) ))
                self.dialog.ui.tableWidget.setItem(modelDialogCode.record(0).value(0), 1, QtWidgets.QTableWidgetItem("{}".format(emisionPedido)))
                self.dialog.ui.tableWidget.setItem(modelDialogCode.record(0).value(0), 2, QtWidgets.QTableWidgetItem("{}".format(emisionPedido)))

        
        self.dialog.ui.tableWidget.verticalHeader().setVisible(False)
        self.dialog.ui.tableWidget.setAlternatingRowColors(True)
        
        header = self.dialog.ui.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        for i in range(3):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        

        #self.dialog.ui.nombreComboBox.setModel(modelDialogNombre)
        self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialog.ui.aceptarButton.clicked.connect(self.acceptDialogNewPedido)
        self.dialog.ui.cancelarButton.clicked.connect(self.dialog.reject)
        self.dialog.exec_()

    def deletePedidos(self):
        
        model = self.modelTablePedidos
        indices = self.tableSeguim.selectionModel().selectedRows()
        for index in sorted(indices):
            model.removeRow(index.row())
        
        self.modelTablePedidos.select()

    def actualizePedidos(self):
      
        self.dialog = QtWidgets.QDialog()
        self.dialog.ui = dialogActualizePedido.Ui_Dialog()
        self.dialog.ui.setupUi(self.dialog)
        
        modelDialogComboBox = QtSql.QSqlQueryModel()
        modelDialogComboBox.setQuery("SELECT DISTINCT p_code FROM Pedidos")

        self.dialog.ui.comboBox_2.setModel(modelDialogComboBox)
        pCode = self.dialog.ui.comboBox_2.currentText()

        self.modelDialogPedido = QtSql.QSqlQueryModel()
        self.modelDialogPedido.setQuery("SELECT * FROM Pedidos WHERE p_code = '{}'".format(pCode))
    
        self.dialog.ui.tableWidget.setColumnCount(3)
        self.dialog.ui.tableWidget.setRowCount(self.modelDialogPedido.rowCount())
        self.dialog.ui.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Código"))
        self.dialog.ui.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Cantidad"))
        self.dialog.ui.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Estado"))

        
        self.dialog.ui.tableWidget.setAlternatingRowColors(True)
        self.dialog.ui.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

        header = self.dialog.ui.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        for i in range(3):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        for i in range(self.modelDialogPedido.rowCount()):
            
            self.dialog.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem("{}".format(self.modelDialogPedido.record(i).value(2))))
            self.dialog.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem("{}".format(self.modelDialogPedido.record(i).value(3))))
            self.dialog.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem("{}".format(self.modelDialogPedido.record(i).value(5))))


        hayAlgunoEnDeposito = 0 
        for idx in range(self.modelDialogPedido.rowCount()):
        	#print(self.modelDialogPedido.record(idx).value(5))
        	if self.modelDialogPedido.record(idx).value(5) == 'En depósito':
        		hayAlgunoEnDeposito = 1


       	if hayAlgunoEnDeposito:
        	self.dialog.ui.label_2.setText('En depósito')
        else:
        	self.dialog.ui.label_2.setText('{}'.format(self.modelDialogPedido.record(0).value(5)))
        
        self.dialog.ui.tableWidget.verticalHeader().setVisible(False)
        self.dialog.ui.tableWidget.setAlternatingRowColors(True)
        
        header = self.dialog.ui.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        for i in range(3):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        
        if self.dialog.ui.label_2.text() == 'En depósito':
            self.dialog.ui.aceptarButton_2.setEnabled(True)
        else:
            self.dialog.ui.aceptarButton_2.setEnabled(False)

        #self.dialog.ui.nombreComboBox.setModel(modelDialogNombre)
        self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.dialog.ui.comboBox_2.currentTextChanged.connect(self.renewTableWidget)
        self.dialog.ui.aceptarButton.clicked.connect(self.acceptDialogActualizePedido)
        self.dialog.ui.aceptarButton_2.clicked.connect(self.retirarDialogPedido)
        self.dialog.ui.cancelarButton.clicked.connect(self.dialog.reject)
        self.dialog.exec_()

    def renewTableWidget(self, text):

        self.modelDialogPedido.setQuery("SELECT * FROM Pedidos WHERE p_code = '{}'".format(text))
        for i in range(self.modelDialogPedido.rowCount()):
            
            self.dialog.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem("{}".format(self.modelDialogPedido.record(i).value(2))))
            self.dialog.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem("{}".format(self.modelDialogPedido.record(i).value(3))))
            self.dialog.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem("{}".format(self.modelDialogPedido.record(i).value(5))))

        hayAlgunoEnDeposito = 0
        for idx in range(self.modelDialogPedido.rowCount()):
        	#print(self.modelDialogPedido.record(idx).value(5))
        	if self.modelDialogPedido.record(idx).value(5) == 'En depósito':
        		hayAlgunoEnDeposito = 1


       	if hayAlgunoEnDeposito:
        	self.dialog.ui.label_2.setText('En depósito')
        else:
        	self.dialog.ui.label_2.setText('{}'.format(self.modelDialogPedido.record(0).value(5)))
        

        if self.dialog.ui.label_2.text() == 'En depósito':
            self.dialog.ui.aceptarButton_2.setEnabled(True)
        else:
            self.dialog.ui.aceptarButton_2.setEnabled(False)

    def acceptDialogActualizePedido(self):

        if self.dialog.ui.label_2.text() == 'En depósito':
            rows =  set()
            for idx in self.dialog.ui.tableWidget.selectedIndexes():
                rows.add(idx.row())
            


            query = QtSql.QSqlQuery()

            for row in rows:
                query.exec("UPDATE Pedidos SET state = '{}' WHERE code = '{}' AND p_code = '{}'".format(self.dialog.ui.comboBox.currentText(), self.dialog.ui.tableWidget.item(row, 0).text(), self.dialog.ui.comboBox_2.currentText()))

        else:
        	
            query = QtSql.QSqlQuery()

            
            query.exec("UPDATE Pedidos SET state = '{}' WHERE p_code = '{}'".format(self.dialog.ui.comboBox.currentText(), self.dialog.ui.comboBox_2.currentText()))


        self.modelTablePedidos.select()

        self.dialog.reject()
        
    def retirarDialogPedido(self):

        rows =  set()
        for idx in self.dialog.ui.tableWidget.selectedIndexes():
            rows.add(idx.row())
        
        query = QtSql.QSqlQuery()
        for row in rows:
            pass
            #print(query.exec("UPDATE Pedidos SET state = 'Retirado' WHERE code = '{}' AND p_code = '{}'".format(self.dialog.ui.tableWidget.item(row, 0).text(),
                                                                                                                #self.dialog.ui.comboBox_2.currentText())))  
                                                                    
        self.modelTablePedidos.select()

        self.dialog.reject()

    def addNewUser(self):
        
        row = self.modelTableUsers.rowCount()
        record = self.modelTableUsers.record()
        record.setValue('user', "Usuario {}".format(row))
        record.setValue('pass', "Contraseña")
        record.setValue('type', 'operario')
        self.modelTableUsers.insertRecord(row, record)
        self.modelTableUsers.select()

    def deleteUser(self):
        
        model = self.modelTableUsers
        indices = self.tableUsers.selectionModel().selectedRows()
        for index in sorted(indices):
            model.removeRow(index.row())
        
        self.modelTableUsers.select()

    def acceptDialogNewRadiador(self):
          
        codigo = self.dialog.ui.codigoLineEdit.text()
        rollo = self.dialog.ui.rolloComboBox.currentText()
        rolloQty = self.dialog.ui.cantidadRolloLineEdit.text()
        tubo = self.dialog.ui.tubosComboBox.currentText()
        tuboQty = self.dialog.ui.cantidadTubosLineEdit.text()

        if self.dialog.ui.usaLateralesCheckBox.isChecked():
            usesLat = "si"
        else:
            usesLat = "no"

        latQty = self.dialog.ui.cantidadLateralesLineEdit.text()

        if self.dialog.ui.usaTurbuladoresCheckBox.isChecked():
            usesTurb = "si"
        else:
            usesTurb = "no"

        turbQty = self.dialog.ui.cantidadTurbuladoresLineEdit.text()
        espesor = self.dialog.ui.espesorLineEdit.text()

        row = self.modelTableRads.rowCount()
        record = self.modelTableRads.record()
        record.setValue('code', codigo)
        record.setValue('alum_id', rollo)
        record.setValue('alum_qty', rolloQty)
        record.setValue('tube_id', tubo)
        record.setValue('tube_qty', tuboQty)
        record.setValue('uses_lat', usesLat)
        record.setValue('lat_qty', latQty)
        record.setValue('uses_turb', usesTurb)
        record.setValue('turb_qty', turbQty)
        record.setValue('espesor', espesor)
        self.modelTableRads.insertRecord(row, record)
        self.modelTableRads.select()

        row = self.modelTableProdPlan.rowCount()
        record = self.modelTableProdPlan.record()
        record.setValue('code', codigo)
        record.setValue('month1', 0)
        record.setValue('month2', 0)
        record.setValue('month3', 0)
        record.setValue('month4', 0)
        record.setValue('month5', 0)
        record.setValue('month6', 0)
        record.setValue('month7', 0)
        record.setValue('month8', 0)
        self.modelTableProdPlan.insertRecord(row, record)
        self.modelTableProdPlan.select()

        self.dialog.reject()
    
    def acceptDialogNewMaterial(self):
          
        codigo = self.dialog.ui.codigoLineEdit.text()
        nombre = self.dialog.ui.nombreComboBox.currentText()
        tiempo = self.dialog.ui.tiempoLineEdit.text()
        stock = self.dialog.ui.stockLineEdit.text()
        lote = self.dialog.ui.loteLineEdit.text()
        nivel = self.dialog.ui.nivelLineEdit.text()
        unidad = self.dialog.ui.unidadLineEdit.text()

        row = self.modelTableMats.rowCount()
        record = self.modelTableMats.record()
        record.setValue('code', codigo)
        record.setValue('name', nombre)
        record.setValue('sumTime', tiempo)
        record.setValue('secStock', stock)
        record.setValue('loteNum', lote)
        record.setValue('level', nivel)
        record.setValue('unit', unidad)
        self.modelTableMats.insertRecord(row, record)
        self.modelTableMats.select()

        self.dialog.reject()

    def acceptDialogNewInventarioLote(self):

        codigo = self.dialog.ui.codigoLineEdit.text()
        #nombre = self.dialog.ui.nombreComboBox.currentText()
        cantidad = self.dialog.ui.qtyLineEdit.text()

        row = self.modelTableInvLote.rowCount()
        record = self.modelTableInvLote.record()
        record.setValue('code', codigo)
        #record.setValue('name', nombre)
        record.setValue('qty', cantidad)
        self.modelTableInvLote.insertRecord(row, record)
        self.modelTableInvLote.select()
        
        self.dialog.reject()

    def acceptDialogNewInventarioSobr(self):

        codigo = self.dialog.ui.codigoLineEdit.text()
        nombre = self.dialog.ui.nombreComboBox.currentText()
        cantidad = self.dialog.ui.qtyLineEdit.text()
        color = self.dialog.ui.colorComboBox.currentText()

        row = self.modelTableInvSobr.rowCount()
        record = self.modelTableInvSobr.record()
        record.setValue('code', codigo)
        record.setValue('name', nombre)
        record.setValue('qty', cantidad)
        record.setValue('color', color)
        self.modelTableInvSobr.insertRecord(row, record)
        self.modelTableInvSobr.select()
        
        self.dialog.reject()

    def acceptDialogNewPedido(self):
        for i in range(1, self.dialog.ui.tableWidget.rowCount()):

            if self.dialog.ui.tableWidget.item(i, 1) is not None and self.dialog.ui.tableWidget.item(i, 0) is not None:
                if float(self.dialog.ui.tableWidget.item(i, 1).text()):


                    record = self.modelTablePedidos.record()
                    row = self.modelTablePedidos.rowCount()
                    
                    p_code = self.dialog.ui.lineEdit.text()
                    date_p = self.dialog.ui.lineEdit_2.text()
                    code = self.dialog.ui.tableWidget.item(i, 0).text()
                    qty = self.dialog.ui.tableWidget.item(i,2).text()
                    state = self.dialog.ui.comboBox.currentText()
                    
                    query = QtSql.QSqlQueryModel()
                    query.setQuery("SELECT name FROM Materiales WHERE code = '{}'".format(code))

                    name = query.record(0).value(0)

                    record.setValue('name', name)
                    record.setValue('code', code)
                    record.setValue('p_code', p_code)  
                    record.setValue('qty', qty)
                    record.setValue('state', state)
                    record.setValue('date_p', date_p)

                    #print(p_code, date_p, code, qty, name)

                    self.modelTablePedidos.insertRecord(row, record)
                    self.modelTablePedidos.select()

                    self.dialog.reject()

    def populateCodigoCompraComboBox(self):
        
        self.modelDialogCode.setQuery("SELECT code FROM Materiales WHERE name = '{}' ".format(self.nombreCompraComboBox.currentText()))
        self.codigoCompraComboBox.setModel(self.modelDialogCode)

    def populateTablaPlanCompras(self):
        
        names = ['alum_id', 'tube_id']
        code = self.codigoCompraComboBox.currentText()
        qtys = ['alum_qty', 'tube_qty']
        nameReal = self.nombreCompraComboBox.currentText()

        self.tableWidgetMaterial.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Lote mínimo"))
        self.tableWidgetMaterial.setItem(0,0, QtWidgets.QTableWidgetItem("Stock mínimo"))
        self.tableWidgetMaterial.setItem(1,0, QtWidgets.QTableWidgetItem("Pedido"))
        self.tableWidgetMaterial.setItem(2,0, QtWidgets.QTableWidgetItem("Viajando"))
        self.tableWidgetMaterial.setItem(3,0, QtWidgets.QTableWidgetItem("En depósito"))
        self.tableWidgetMaterial.setItem(4,0, QtWidgets.QTableWidgetItem("Retirado"))
        self.tableWidgetMaterial.setItem(5,0, QtWidgets.QTableWidgetItem("En fábrica"))

        for i in range(8):
            self.tableWidgetPlanCompra.setHorizontalHeaderItem(i+1, 
                QtWidgets.QTableWidgetItem(months[add_months(datetime.date.today(),i).month-1]+", "+str(add_months(datetime.date.today(),i).year)))

        if self.nombreCompraComboBox.currentIndex() < 2:

            name = names[self.nombreCompraComboBox.currentIndex()]
            qty = qtys[self.nombreCompraComboBox.currentIndex()]
            queryGetCodes = QtSql.QSqlQueryModel()
            queryGetCodes.setQuery("SELECT code, {} FROM Radiadores WHERE {} = '{}'".format(qty, name, code))

            monthlyValue = [0]*8

            for i in range(queryGetCodes.rowCount()):
                codeInst = queryGetCodes.record(i).value(0) 
                qtyInst = queryGetCodes.record(i).value(1) 
                queryGetQty = QtSql.QSqlQueryModel()
                queryGetQty.setQuery("SELECT * FROM PlanProduccion WHERE code = '{}'".format(codeInst))
                for j in range(8):
                    #print(queryGetQty.record(0).value(j+2), codeInst, qtyInst)
                    monthlyValue[j] += (float(queryGetQty.record(0).value(j+2))*float(qtyInst))
                
            for i in range(8):
        
                self.tableWidgetPlanCompra.setItem(0, i+1, 
                       QtWidgets.QTableWidgetItem("{}".format(monthlyValue[i])))

            self.tableWidgetPlanCompra.setHorizontalHeaderItem(0, 
                    QtWidgets.QTableWidgetItem(nameReal +" "+ code))


            self.tableWidgetPlanCompra.verticalHeader().setVisible(False)
            self.tableWidgetPlanCompra.setAlternatingRowColors(True)
            
            header = self.tableWidgetPlanCompra.horizontalHeader()       
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            for i in range(9):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        if self.nombreCompraComboBox.currentIndex() >= 2:
            
            monthlyValue = [0]*8

            nameReal = self.nombreCompraComboBox.currentText()
            qty = 2
            codeInst = self.codigoCompraComboBox.currentText()[-4:]
            queryGetQty = QtSql.QSqlQueryModel()
            queryGetQty.setQuery("SELECT * FROM PlanProduccion WHERE code = '{}'".format(codeInst))
            
            if queryGetQty.record(0).value(2) is None:
                return None
            for j in range(8):
                monthlyValue[j] += (float(queryGetQty.record(0).value(j+2))*float(2))
              
            for i in range(8):
        
                self.tableWidgetPlanCompra.setItem(0, i+1, 
                       QtWidgets.QTableWidgetItem("{}".format(monthlyValue[i])))

            self.tableWidgetPlanCompra.setHorizontalHeaderItem(0, 
                    QtWidgets.QTableWidgetItem(nameReal +" "+ code))


            self.tableWidgetPlanCompra.verticalHeader().setVisible(False)
            self.tableWidgetPlanCompra.setAlternatingRowColors(True)
            
            header = self.tableWidgetPlanCompra.horizontalHeader()       
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            for i in range(9):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        if True: #Armo pedidos
            
            queryGetPedidos = QtSql.QSqlQueryModel()
            queryGetPedidos.setQuery("SELECT * FROM Pedidos WHERE code = '{}'".format(code))
            
            pedidosQty = 0
            viajandoQty = 0
            depositoQty = 0
            retiradoQty = 0
            enFabricaQty = 0
            pendienteIngresoLista = [0]*8

            for i in range(queryGetPedidos.rowCount()):
                mes = int(queryGetPedidos.record(i).value(6).split('/')[1])
                año = int(queryGetPedidos.record(i).value(6).split('/')[2])
                currentMes = datetime.date.today().month
                currentAño = datetime.date.today().year
                #print(mes,'/',año,'-',currentMes,'/',currentAño)


                if año == currentAño:
                    if currentMes-mes <= 3:                    
                        pendienteIngresoLista[-currentMes + mes + 3] += float(queryGetPedidos.record(i).value(3))
                
                elif año < currentAño:
                    if currentMes+12-mes <= 3:
                        pendienteIngresoLista[-currentMes + 12 + mes + 3] += float(queryGetPedidos.record(i).value(3))

                if queryGetPedidos.record(i).value(5) == 'Pedido':
                    pedidosQty += float(queryGetPedidos.record(i).value(3))
                elif queryGetPedidos.record(i).value(5) == 'Viajando':
                    viajandoQty += float(queryGetPedidos.record(i).value(3))
                elif queryGetPedidos.record(i).value(5) == 'En depósito':
                    depositoQty += float(queryGetPedidos.record(i).value(3))
                elif queryGetPedidos.record(i).value(5) == 'Retirado':
                    retiradoQty += float(queryGetPedidos.record(i).value(3))
                elif queryGetPedidos.record(i).value(5) == 'En fábrica':
                    enFabricaQty += float(queryGetPedidos.record(i).value(3))

            #totalQty = enFabricaQty
            
            for i in range(8):
                self.tableWidgetPlanCompra.setItem(1, i+1, 
                    QtWidgets.QTableWidgetItem("{}".format(pendienteIngresoLista[i])))
            
            self.tableWidgetPlanCompra.setItem(2, 1, 
                    QtWidgets.QTableWidgetItem("{}".format(pedidosQty)))
            self.tableWidgetPlanCompra.setItem(3, 1, 
                    QtWidgets.QTableWidgetItem("{}".format(viajandoQty)))
            self.tableWidgetPlanCompra.setItem(4, 1, 
                    QtWidgets.QTableWidgetItem("{}".format(depositoQty)))
            self.tableWidgetPlanCompra.setItem(5, 1, 
                    QtWidgets.QTableWidgetItem("{}".format(retiradoQty)))
            self.tableWidgetPlanCompra.setItem(6, 1, 
                    QtWidgets.QTableWidgetItem("{}".format(enFabricaQty)))
            self.tableWidgetPlanCompra.setItem(1, 1, 
                    QtWidgets.QTableWidgetItem("{}".format(enFabricaQty)))
                    
            self.tableWidgetMaterial.setItem(1, 1, 
                    QtWidgets.QTableWidgetItem("{}".format(pedidosQty)))
            self.tableWidgetMaterial.setItem(2, 1, 
                    QtWidgets.QTableWidgetItem("{}".format(viajandoQty)))
            self.tableWidgetMaterial.setItem(3, 1, 
                    QtWidgets.QTableWidgetItem("{}".format(depositoQty)))
            self.tableWidgetMaterial.setItem(4, 1, 
                    QtWidgets.QTableWidgetItem("{}".format(retiradoQty)))
            self.tableWidgetMaterial.setItem(5, 1, 
                    QtWidgets.QTableWidgetItem("{}".format(enFabricaQty)))

        if True: #Busco inventarios
            inventarioQty = 0

            query = QtSql.QSqlQueryModel()
            query.setQuery("SELECT * FROM InventarioSobrantes WHERE code = '{}'".format(code))

            for i in range(query.rowCount()):
                if query.record(i).value(4) != 'Reservado':
                    inventarioQty += query.record(i).value(3)

            self.tableWidgetPlanCompra.setItem(7,1,
                    QtWidgets.QTableWidgetItem("{}".format(inventarioQty)))

            inventarioList = [0]*9
            reqNetos = [0]*9
            query = QtSql.QSqlQueryModel()
            query.setQuery("SELECT loteNum, secStock FROM Materiales WHERE code = '{}'".format(code))
            loteMin = query.record(0).value(0)
            secStock = query.record(0).value(1)
            for i in range(1,9):
                
                reqBrutos = float(self.tableWidgetPlanCompra.item(0,i).text())
                pendIngreso = float(self.tableWidgetPlanCompra.item(1,i).text())
                if i == 1:
                    inventario = float(self.tableWidgetPlanCompra.item(7,i).text())
                else:
                    inventario = inventarioList[i]

                if inventario<0:
                    inventario=0
                if i<8:
                    inventarioList[i+1] = inventario + pendIngreso - reqBrutos
                reqNetos[i] = reqBrutos - inventario - pendIngreso
                if reqNetos[i]:
                    reqNetos[i]+=secStock

                if i<8:
                    if inventarioList[i+1]>0:
                        self.tableWidgetPlanCompra.setItem(7, i+1, QtWidgets.QTableWidgetItem("{}".format(inventarioList[i+1])))
                    else:
                        self.tableWidgetPlanCompra.setItem(7, i+1, QtWidgets.QTableWidgetItem("{}".format(0)))

                self.tableWidgetPlanCompra.setItem(8,i,QtWidgets.QTableWidgetItem("{}".format(reqNetos[i])))

        if True: #Ing. Planif.
            #print(loteMin, secStock)
            self.tableWidgetMaterial.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("{}".format(loteMin)))
            self.tableWidgetMaterial.setItem(0,1, QtWidgets.QTableWidgetItem("{}".format(secStock)))
            for i in range(1,9):
                reqNeto = float(self.tableWidgetPlanCompra.item(8,i).text())
                if loteMin:
                    if reqNeto > loteMin:
                        self.tableWidgetPlanCompra.setItem(9, i, QtWidgets.QTableWidgetItem("{}".format(reqNeto)))
                    elif reqNeto < loteMin and reqNeto > 0:
                        self.tableWidgetPlanCompra.setItem(9, i, QtWidgets.QTableWidgetItem("{}".format(loteMin)))
                    elif reqNeto <= 0:
                        self.tableWidgetPlanCompra.setItem(9, i, QtWidgets.QTableWidgetItem("{}".format(0)))

            for i in range(1,6):
                #print(self.tableWidgetPlanCompra.item(9,i+3).text())
                if (self.tableWidgetPlanCompra.item(9,i+3) == None) or (self.tableWidgetPlanCompra.item(9,i+3) == 0):
                    self.tableWidgetPlanCompra.setItem(10, i, QtWidgets.QTableWidgetItem('{}'.format(0)))
                    #self.tableWidgetPlanCompra.setItem(9, i, QtWidgets.QTableWidgetItem('{}'.format(0)))
                else:
                    ingTres = float(self.tableWidgetPlanCompra.item(9,i+3).text())
                    self.tableWidgetPlanCompra.setItem(10, i, QtWidgets.QTableWidgetItem('{}'.format(ingTres)))


        
        self.tableWidgetPlanCompra.hideRow(2)
        self.tableWidgetPlanCompra.hideRow(3)
        self.tableWidgetPlanCompra.hideRow(4)
        self.tableWidgetPlanCompra.hideRow(5)
        self.tableWidgetPlanCompra.hideRow(6)
        #self.doubleClickedOnPendiente(1,0)
        
    def generatePlanDeCompras(self):

        #pedido = pd.DataFrame(columns = ['nombre', 'codigo', 'Req Bruto', 'Pend Ingreso', 'Inventario', 'Req Neto', 'Emision Pedido'])

        rows_list = []


        pesosMes1Rollo = 0
        pesosMes2Rollo = 0
        pesosMes3Rollo = 0

        pesosMes1Tubo = 0
        pesosMes2Tubo = 0
        pesosMes3Tubo = 0

        unidadesMes1 = 0
        unidadesMes2 = 0
        unidadesMes3 = 0

        for name in range(self.nombreCompraComboBox.count()):
            
            self.nombreCompraComboBox.setCurrentIndex(name)

            for codigo in range(self.codigoCompraComboBox.count()):

                self.codigoCompraComboBox.setCurrentIndex(codigo)
                

                nombreText = self.nombreCompraComboBox.currentText()
                codigoText = self.codigoCompraComboBox.currentText()
                emisionPedidoMes1 = self.tableWidgetPlanCompra.item(10,1).text()
                emisionPedidoMes2 = self.tableWidgetPlanCompra.item(10,2).text()
                emisionPedidoMes3 = self.tableWidgetPlanCompra.item(10,3).text()

                if self.nombreCompraComboBox.currentText() == 'Rollo':
                	pesosMes1Rollo += float(emisionPedidoMes1)
                	pesosMes2Rollo += float(emisionPedidoMes2)
                	pesosMes3Rollo += float(emisionPedidoMes3)

               	elif self.nombreCompraComboBox.currentText() == 'Tubo':
                	pesosMes1Tubo += float(emisionPedidoMes1)
                	pesosMes2Tubo += float(emisionPedidoMes2)
                	pesosMes3Tubo += float(emisionPedidoMes3)

                elif self.nombreCompraComboBox.currentText() == 'Placa':

                    unidadesMes1 += float(emisionPedidoMes1)/2.
                    unidadesMes2 += float(emisionPedidoMes2)/2.
                    unidadesMes3 += float(emisionPedidoMes3)/2.
           

                #reqBruto = self.tableWidgetPlanCompra.item(0,4).text()
                #reqNeto = self.tableWidgetPlanCompra.item(8,4).text()
                #inventario = self.tableWidgetPlanCompra.item(7,4).text()
                #pendienteIngreso = self.tableWidgetPlanCompra.item(1,4).text()

                diccionario = {'Nombre': nombreText, 'Código': codigoText, 'Mes 1': int(float(emisionPedidoMes1)), 'Mes 2': int(float(emisionPedidoMes2)), 'Mes 3': int(float(emisionPedidoMes3))}
                #print(diccionario)
                if diccionario['Mes 1'] > 0 or diccionario['Mes 2'] > 0 or diccionario['Mes 3'] > 0: 
                    rows_list.append(diccionario)

        diccionario1 = {"Mes": 1,
                "Peso Rollos": "{} ({}%)".format(pesosMes1Rollo, round(pesosMes1Rollo/6620*100)), 
                "Peso Tubos": "{} ({}%)".format(pesosMes1Tubo, round(pesosMes1Tubo/6620*100)), 
                "Radiadores": "{} ({}%)".format(unidadesMes1, round(unidadesMes1/8500*100))}
        diccionario2 = {"Mes":2,
                "Peso Rollos": "{} ({}%)".format(pesosMes2Rollo, round(pesosMes2Rollo/6620*100)), 
                "Peso Tubos": "{} ({}%)".format(pesosMes2Tubo, round(pesosMes2Tubo/6620*100)), 
                "Radiadores": "{} ({}%)".format(unidadesMes2, round(unidadesMes2/8500*100))}
        diccionario3 = {"Mes":3,
                "Peso Rollos": "{} ({}%)".format(pesosMes3Rollo, round(pesosMes3Rollo/6620*100)), 
                "Peso Tubos": "{} ({}%)".format(pesosMes3Tubo, round(pesosMes3Tubo/6620*100)), 
                "Radiadores": "{} ({}%)".format(unidadesMes3, round(unidadesMes3/8500*100))}

        #print('Peso Mes 1 Rollo: {}'.format(pesosMes1Rollo), 'Peso Mes 1 Tubos: {}'.format(pesosMes1Tubo), 'Unidades Mes 1: {}'.format(unidadesMes1))

        columnas = ['Nombre', 'Código', 'Mes 1', 'Mes 2', 'Mes 3']
        pedido = pd.DataFrame(rows_list)
        pedido = pedido[columnas]

        lista_dicc = []
        lista_dicc.append(diccionario1)
        lista_dicc.append(diccionario2)
        lista_dicc.append(diccionario3)
        contenedores = pd.DataFrame(lista_dicc)



        with open('planPedido.html', 'w') as file:
        	file.write(contenedores.to_html(index=False, justify = "center") + pedido.to_html(index=False, justify = "center"))

        doc = QtGui.QTextDocument()
        location = "planPedido.html"
        html = open(location).read()
        doc.setHtml(html)

        printer = QtPrintSupport.QPrinter()
        
        filename = QtWidgets.QFileDialog.getSaveFileName()
        print(filename)
        printer.setOutputFileName(filename[0]+'.pdf')
        printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
        printer.setPageSize(QtPrintSupport.QPrinter.A4)
        printer.setPageMargins(15, 15, 15, 15, QtPrintSupport.QPrinter.Millimeter)

        doc.print_(printer)






    def find(self, text, column=1):

        model = self.tableBOM.model()
        start = model.index(0, column)
        matches = model.match(
            start, QtCore.Qt.DisplayRole,
            text, 1, QtCore.Qt.MatchContains)
        if matches:
            index = matches[0]
            print(matches[0].data())
            # index.row(), index.column()
            self.tableBOM.selectionModel().select(
                index, QtCore.QItemSelectionModel.Select)

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

