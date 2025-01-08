# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginUebACO.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
from icone import img

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(378, 300)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 40, 241, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 80, 41, 16))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 130, 41, 16))
        self.lineEdit_nome = QLineEdit(Dialog)
        self.lineEdit_nome.setObjectName(u"lineEdit_nome")
        self.lineEdit_nome.setGeometry(QRect(100, 80, 151, 22))
        self.lineEdit_senha = QLineEdit(Dialog)
        self.lineEdit_senha.setObjectName(u"lineEdit_senha")
        self.lineEdit_senha.setGeometry(QRect(100, 130, 151, 22))
        self.lineEdit_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 190, 75, 24))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(210, 190, 75, 24))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 240, 211, 31))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(260, 60, 81, 111))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialogx", u"Tela de login", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"SISTEMA DE CADASTRO DE FUNCION\u00c1RIOS", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nome", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Senha", None))
        self.lineEdit_nome.setPlaceholderText(QCoreApplication.translate("Dialog", u"Nome de usu\u00e1rio", None))
        self.lineEdit_senha.setPlaceholderText(QCoreApplication.translate("Dialog", u"Senha", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Conectar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700; color:#000071;\">Esqueceu sua senha?</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/img/icons8-pele-de-engenheiro-tipo-1-96.png\"/></p></body></html>", None))
    # retranslateUi

