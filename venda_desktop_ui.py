# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'venda_desktop.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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

class Ui_venda_desktop(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(444, 242)
        Dialog.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 200, 121, 23))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 170, 255);")
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(340, 200, 75, 23))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(250, 20, 161, 61))
        self.pushButton_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 61, 21))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 61, 21))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 140, 61, 21))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 100, 61, 21))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(250, 100, 61, 21))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 20, 113, 20))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(90, 60, 113, 20))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(90, 100, 113, 20))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(90, 140, 113, 20))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_5 = QLineEdit(Dialog)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(300, 100, 113, 20))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_6 = QLineEdit(Dialog)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(302, 140, 111, 20))
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(250, 140, 41, 21))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Nova venda", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Salvar Venda", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Buscar", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Descri\u00e7\u00e3o", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Valor", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Quantidade", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Tipo", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Ticket", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Usuario", None))
    # retranslateUi

