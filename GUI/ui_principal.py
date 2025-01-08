# -*- coding: utf-8 -*-
from PySide6 import QtWidgets
################################################################################
## Form generated from reading UI file 'principalHqxtgz.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QToolBar, QWidget)
from icone import img2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(704, 481)
        self.actionCadastrar = QAction(MainWindow)
        self.actionCadastrar.setObjectName(u"actionCadastrar")
        icon = QIcon()
        icon.addFile(u":/img2/icons8-decis\u00e3o-64.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionCadastrar.setIcon(icon)
        self.actionProcurar = QAction(MainWindow)
        self.actionProcurar.setObjectName(u"actionProcurar")
        icon1 = QIcon()
        icon1.addFile(u":/img2/icons8-cms-96.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionProcurar.setIcon(icon1)
        self.actionApagar = QAction(MainWindow)
        self.actionApagar.setObjectName(u"actionApagar")
        self.actionSelecionar = QAction(MainWindow)
        self.actionSelecionar.setObjectName(u"actionSelecionar")
        self.actionRditar = QAction(MainWindow)
        self.actionRditar.setObjectName(u"actionRditar")
        self.actionDesbloquear = QAction(MainWindow)
        self.actionDesbloquear.setObjectName(u"actionDesbloquear")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(18, 25, 671, 31))
        self.label.setStyleSheet(u"background-color: rgb(181, 181, 181);\n"
"border-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.label.setMargin(1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 30, 181, 16))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Segoe UI\";")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(510, 30, 49, 16))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 11pt \"Segoe UI\";")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 70, 671, 331))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 704, 22))
        self.menuArquivos = QMenu(self.menubar)
        self.menuArquivos.setObjectName(u"menuArquivos")
        self.menuEditar = QMenu(self.menubar)
        self.menuEditar.setObjectName(u"menuEditar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuArquivos.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menuArquivos.addAction(self.actionCadastrar)
        self.menuArquivos.addAction(self.actionProcurar)
        self.menuArquivos.addAction(self.actionApagar)
        self.menuEditar.addAction(self.actionSelecionar)
        self.menuEditar.addAction(self.actionRditar)
        self.menuEditar.addAction(self.actionDesbloquear)
        self.toolBar.addAction(self.actionProcurar)
        self.toolBar.addAction(self.actionCadastrar)
        self.toolBar.addAction(self.actionApagar)
        self.toolBar.addAction(self.actionRditar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionCadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
#if QT_CONFIG(tooltip)
        self.actionCadastrar.setToolTip(QCoreApplication.translate("MainWindow", u"Cadastrar pessoas no sistema", None))
#endif // QT_CONFIG(tooltip)
        self.actionProcurar.setText(QCoreApplication.translate("MainWindow", u"Procurar", None))
        self.actionApagar.setText(QCoreApplication.translate("MainWindow", u"Apagar", None))
        self.actionSelecionar.setText(QCoreApplication.translate("MainWindow", u"Selecionar", None))
        self.actionRditar.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.actionDesbloquear.setText(QCoreApplication.translate("MainWindow", u"Desbloquear", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Documento", None));
        self.menuArquivos.setTitle(QCoreApplication.translate("MainWindow", u"Arquivos", None))
        self.menuEditar.setTitle(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi


