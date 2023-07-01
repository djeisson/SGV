# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cad_produtos.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_cad_produtos(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 249)
        Form.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.actionLitro = QAction(Form)
        self.actionLitro.setObjectName(u"actionLitro")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 71, 21))
        self.label.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 20, 291, 21))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 71, 21))
        self.label_2.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 60, 91, 21))
        self.label_3.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 100, 71, 21))
        self.label_4.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 100, 91, 21))
        self.label_5.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(90, 100, 81, 21))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(300, 100, 81, 21))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_5 = QLineEdit(Form)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(300, 60, 81, 21))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 140, 71, 21))
        self.label_7.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(200, 140, 81, 21))
        self.label_8.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 180, 281, 51))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(90, 60, 81, 22))
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(90, 140, 81, 22))
        self.comboBox_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.comboBox_3 = QComboBox(Form)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(300, 140, 81, 22))
        self.comboBox_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Cadastro de Produtos", None))
        self.actionLitro.setText(QCoreApplication.translate("Form", u"Litro", None))
        self.label.setText(QCoreApplication.translate("Form", u"Descri\u00e7\u00e3o", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Unidade", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Quantidade", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Custo", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Valor Venda", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"R$", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"R$", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Form", u"Estoque inicial", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Grupo", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Sub. Grupo", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Salvar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Litro", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Lata", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Unidade", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"Ma\u00e7o", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"Geral", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("Form", u"Geral", None))

    # retranslateUi

