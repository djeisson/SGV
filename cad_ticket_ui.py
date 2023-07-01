# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cad_ticket.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_cad_ticket(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(284, 196)
        Dialog.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(90, 60, 161, 20))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 47, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 47, 16))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 20, 161, 20))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(180, 150, 75, 23))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 100, 47, 16))
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(90, 100, 161, 22))
        self.comboBox.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 150, 75, 23))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Cadastro de Ticket", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"R$", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Numero", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Valor", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Cliente", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Salvar", None))
    # retranslateUi

