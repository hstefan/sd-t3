# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app_gui.ui'
#
# Created: Fri Jun 29 06:57:40 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(592, 486)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lv_tweets = QtGui.QListWidget(self.centralwidget)
        self.lv_tweets.setGeometry(QtCore.QRect(10, 40, 571, 171))
        self.lv_tweets.setObjectName(_fromUtf8("lv_tweets"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 220, 571, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.le_address = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.le_address.setObjectName(_fromUtf8("le_address"))
        self.horizontalLayout_2.addWidget(self.le_address)
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.cb_mode = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.cb_mode.setObjectName(_fromUtf8("cb_mode"))
        self.cb_mode.addItem(_fromUtf8(""))
        self.cb_mode.addItem(_fromUtf8(""))
        self.cb_mode.addItem(_fromUtf8(""))
        self.cb_mode.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.cb_mode)
        self.bt_route = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.bt_route.setObjectName(_fromUtf8("bt_route"))
        self.horizontalLayout_2.addWidget(self.bt_route)
        self.wv_instructions = QtWebKit.QWebView(self.centralwidget)
        self.wv_instructions.setGeometry(QtCore.QRect(10, 260, 571, 200))
        self.wv_instructions.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.wv_instructions.setObjectName(_fromUtf8("wv_instructions"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 571, 25))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.le_user = QtGui.QLineEdit(self.widget)
        self.le_user.setObjectName(_fromUtf8("le_user"))
        self.horizontalLayout.addWidget(self.le_user)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.le_tweets_number = QtGui.QLineEdit(self.widget)
        self.le_tweets_number.setObjectName(_fromUtf8("le_tweets_number"))
        self.horizontalLayout.addWidget(self.le_tweets_number)
        self.bt_search = QtGui.QPushButton(self.widget)
        self.bt_search.setObjectName(_fromUtf8("bt_search"))
        self.horizontalLayout.addWidget(self.bt_search)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 592, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Endereço atual", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Método de viagem", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_mode.setItemText(0, QtGui.QApplication.translate("MainWindow", "Driving", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_mode.setItemText(1, QtGui.QApplication.translate("MainWindow", "Walking", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_mode.setItemText(2, QtGui.QApplication.translate("MainWindow", "Biciclying", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_mode.setItemText(3, QtGui.QApplication.translate("MainWindow", "Transit", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_route.setText(QtGui.QApplication.translate("MainWindow", "Route", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Tweets number", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_search.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
