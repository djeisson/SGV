# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_venda.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_tela_venda(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(682, 447)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 47, 31))
        self.label.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.tableWidget = QTableWidget(Dialog)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 230, 661, 191))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(540, 20, 91, 31))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 19, 421, 31))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 47, 31))
        self.label_2.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 70, 151, 31))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(286, 70, 71, 31))
        self.label_3.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(380, 70, 151, 31))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 120, 91, 31))
        self.label_4.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")
        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(110, 120, 151, 31))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(110, 170, 151, 31))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 170, 255);")
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(380, 170, 151, 31))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")
        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(540, 170, 91, 31))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")
        self.lineEdit_5 = QLineEdit(Dialog)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(380, 120, 151, 31))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, 120, 91, 31))
        self.label_5.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Venda no terminal", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Produto", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"ID_PRODUTO", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"DESCRI\u00c7\u00c3O", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"VALOR_UNITARIO", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"QUANTIDADE", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"VALOR_FINAL", None));
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Buscar", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Valor", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Quantidade", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Valor final P.", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Encerar venda", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Cancelar ", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Limpar tela", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Ticket", None))
    # retranslateUi

