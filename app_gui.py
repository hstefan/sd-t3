# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app_gui.ui'
#
# Created: Fri Jun 29 13:56:12 2012
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
        MainWindow.resize(405, 519)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.le_user = QtGui.QLineEdit(self.centralwidget)
        self.le_user.setObjectName(_fromUtf8("le_user"))
        self.horizontalLayout.addWidget(self.le_user)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.le_tweets_number = QtGui.QSpinBox(self.centralwidget)
        self.le_tweets_number.setMinimum(1)
        self.le_tweets_number.setMaximum(100)
        self.le_tweets_number.setProperty("value", 15)
        self.le_tweets_number.setObjectName(_fromUtf8("le_tweets_number"))
        self.horizontalLayout.addWidget(self.le_tweets_number)
        self.bt_search = QtGui.QPushButton(self.centralwidget)
        self.bt_search.setObjectName(_fromUtf8("bt_search"))
        self.horizontalLayout.addWidget(self.bt_search)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lv_tweets = QtGui.QListWidget(self.centralwidget)
        self.lv_tweets.setObjectName(_fromUtf8("lv_tweets"))
        self.verticalLayout.addWidget(self.lv_tweets)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.le_address = QtGui.QLineEdit(self.centralwidget)
        self.le_address.setObjectName(_fromUtf8("le_address"))
        self.horizontalLayout_2.addWidget(self.le_address)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.cb_mode = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_mode.sizePolicy().hasHeightForWidth())
        self.cb_mode.setSizePolicy(sizePolicy)
        self.cb_mode.setObjectName(_fromUtf8("cb_mode"))
        self.cb_mode.addItem(_fromUtf8(""))
        self.cb_mode.addItem(_fromUtf8(""))
        self.cb_mode.addItem(_fromUtf8(""))
        self.cb_mode.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.cb_mode)
        self.bt_route = QtGui.QPushButton(self.centralwidget)
        self.bt_route.setObjectName(_fromUtf8("bt_route"))
        self.horizontalLayout_3.addWidget(self.bt_route)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.lv_directions = QtGui.QListWidget(self.centralwidget)
        self.lv_directions.setObjectName(_fromUtf8("lv_directions"))
        self.verticalLayout.addWidget(self.lv_directions)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Username:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Tweets to load:", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_search.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Endereço atual:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Método de viagem:", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_mode.setItemText(0, QtGui.QApplication.translate("MainWindow", "Driving", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_mode.setItemText(1, QtGui.QApplication.translate("MainWindow", "Walking", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_mode.setItemText(2, QtGui.QApplication.translate("MainWindow", "Biciclying", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_mode.setItemText(3, QtGui.QApplication.translate("MainWindow", "Transit", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_route.setText(QtGui.QApplication.translate("MainWindow", "Route", None, QtGui.QApplication.UnicodeUTF8))

