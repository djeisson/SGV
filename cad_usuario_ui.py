# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cad_usuario.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_cad_usuario(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(377, 289)
        Form.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 40, 45, 151))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.label_4)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.label_3)

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(80, 40, 281, 151))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.lineEdit_4 = QLineEdit(self.layoutWidget1)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.lineEdit_4)

        self.lineEdit_3 = QLineEdit(self.layoutWidget1)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.lineEdit_3)

        self.layoutWidget2 = QWidget(Form)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 230, 341, 25))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.layoutWidget2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.layoutWidget2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"color:rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.layoutWidget3 = QWidget(Form)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 200, 341, 20))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.layoutWidget3)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.layoutWidget3)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.layoutWidget3)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_2.addWidget(self.radioButton_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Cadastro de Usuario", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nome", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Usuario", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"CPF", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Senha", None))
        self.lineEdit_3.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Salvar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"ADM", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"USER", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"ADM/USER", None))
    # retranslateUi

