# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list_user.ui'
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
        Form.resize(321, 281)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 321, 271))
        self.frame.setStyleSheet(u"QFrame{\n"
"	border: 2px solid #434965;\n"
"	border-radius: 7px;\n"
"	background-color: #2A2F41;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(280, 10, 31, 31))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	border-radius: 7px;\n"
"	background-color: #2A2F41;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #50566E;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #434965;\n"
"}")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 271, 31))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-size: 16px;")
        self.listWidget = QListWidget(self.frame)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 50, 301, 211))
        self.listWidget.setFont(font1)
        self.listWidget.setTabletTracking(False)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setStyleSheet(u"QListWidget {\n"
"	font-size:15px;\n"
"	background-color: #2C313C;\n"
"	color: white;\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"	padding-top: 6px;\n"
"}\n"
"")
        self.listWidget.setFrameShape(QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QFrame.Raised)
        self.listWidget.setLineWidth(1)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.listWidget.setAutoScroll(True)
        self.listWidget.setTabKeyNavigation(False)
        self.listWidget.setProperty("showDropIndicator", True)
        self.listWidget.setDragDropOverwriteMode(False)
        self.listWidget.setAlternatingRowColors(False)
        self.listWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.listWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.listWidget.setMovement(QListView.Static)
        self.listWidget.setFlow(QListView.TopToBottom)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setResizeMode(QListView.Fixed)
        self.listWidget.setLayoutMode(QListView.SinglePass)
        self.listWidget.setViewMode(QListView.ListMode)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setWordWrap(True)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setSortingEnabled(False)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"x", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439 \u0447\u0430\u0442\u0430", None))
    # retranslateUi

