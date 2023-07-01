# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_about(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(521, 272)
        Dialog.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 461, 31))
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(85, 170, 255);\n"
"font: 75 12pt \"Terminal\";")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 60, 441, 151))
        self.label_2.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(85, 170, 255);\n"
"")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 220, 101, 31))
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 0, 0);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"About", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"   Sistema de gerenciamento de vendas", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"                                     Sistema desenvolvido por Djeisson Schneider", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Fechar", None))
    # retranslateUi

