# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(361, 546)
        MainWindow.setMinimumSize(QSize(3, 0))
        MainWindow.setMaximumSize(QSize(391, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(391, 546))
        self.centralwidget.setMaximumSize(QSize(391, 546))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 5, 361, 541))
        self.frame.setMinimumSize(QSize(3, 3))
        self.frame.setMaximumSize(QSize(3213, 16777215))
        self.frame.setStyleSheet(u"QFrame{\n"
"	border-radius: 7px;\n"
"	background-color: #17212B;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(5, 500, 306, 36))
        font = QFont()
        font.setFamily(u"Sans Serif")
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setAcceptDrops(True)
        self.lineEdit.setStyleSheet(u"background-color: #2C313C;\n"
"font-size: 15px;\n"
"padding: 0px 5px;\n"
"border-radius: 3px;\n"
"color: #fff;")
        self.lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit.setClearButtonEnabled(True)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(315, 500, 41, 36))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	border-radius: 7px;\n"
"	background-color: #595F76;\n"
"	font-size: 22px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #50566E;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #434965;\n"
"}")
        self.listWidget = QListWidget(self.frame)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(5, 40, 351, 456))
        font2 = QFont()
        font2.setBold(False)
        font2.setWeight(50)
        self.listWidget.setFont(font2)
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
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 361, 36))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	background-color: #2C313C;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 5, 31, 26))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	border-radius: 5px;\n"
"	background-color: #595F76;\n"
"	font-size: 22px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #50566E;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #434965;\n"
"}")
        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(50, 5, 136, 26))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	border-radius: 5px;\n"
"	background-color: #595F76;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #50566E;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #434965;\n"
"}")
        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(335, 10, 16, 16))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButton_5.setFont(font3)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	border: none;\n"
"	background-color: #f73643;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #d63a44;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color: #EA2F4E;\n"
"}")
        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(310, 10, 16, 16))
        self.pushButton_4.setFont(font3)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	border: none;\n"
"	background-color: #47fc65;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #49cc5f;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	color: #EA2F4E;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u27a4", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u2699", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.pushButton_5.setText("")
        self.pushButton_4.setText("")
    # retranslateUi

