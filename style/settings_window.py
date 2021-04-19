# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(428, 276)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 431, 271))
        self.frame.setStyleSheet(u"QFrame{\n"
"	border: 2px solid #434965;\n"
"	border-radius: 7px;\n"
"	background-color: #2A2F41;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 70, 391, 41))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setFocusPolicy(Qt.ClickFocus)
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 7px;\n"
"}")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(20, 120, 391, 41))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setFocusPolicy(Qt.ClickFocus)
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 7px;\n"
"}")
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_3.setClearButtonEnabled(False)
        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(220, 210, 191, 41))
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	border-radius: 7px;\n"
"	background-color: #595F76;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #50566E;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #434965;\n"
"}")
        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(20, 210, 191, 41))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	border-radius: 7px;\n"
"	background-color: #595F76;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #50566E;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #434965;\n"
"}")
        self.lineEdit_1 = QLineEdit(self.frame)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setGeometry(QRect(20, 20, 391, 41))
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setFocusPolicy(Qt.ClickFocus)
        self.lineEdit_1.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 7px;\n"
"}")
        self.lineEdit_1.setAlignment(Qt.AlignCenter)
        self.lineEdit_1.setClearButtonEnabled(False)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 170, 191, 31))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-size: 14px;")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 170, 191, 31))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-size: 14px;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"\u0421\u0442\u0440\u0430\u043d\u0430", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438 \u0432\u044b\u0439\u0442\u0438", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.lineEdit_1.setText("")
        self.lineEdit_1.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u0438\u043a\u043d\u0435\u0439\u043c", None))
        self.label.setText("")
        self.label_2.setText("")
    # retranslateUi

