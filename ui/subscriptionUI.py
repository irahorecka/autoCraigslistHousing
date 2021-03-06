# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/subscriptionUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(493, 385)
        self.hours = QtWidgets.QComboBox(Dialog)
        self.hours.setGeometry(QtCore.QRect(200, 250, 91, 26))
        self.hours.setObjectName("hours")
        self.subscription_craigslist_header = QtWidgets.QLabel(Dialog)
        self.subscription_craigslist_header.setGeometry(QtCore.QRect(80, 40, 321, 81))
        self.subscription_craigslist_header.setText("")
        self.subscription_craigslist_header.setPixmap(
            QtGui.QPixmap("./ui/image/craigslist.png")
        )
        self.subscription_craigslist_header.setScaledContents(True)
        self.subscription_craigslist_header.setObjectName(
            "subscription_craigslist_header"
        )
        self.subscription_housing_header = QtWidgets.QLabel(Dialog)
        self.subscription_housing_header.setGeometry(QtCore.QRect(320, 100, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.subscription_housing_header.setFont(font)
        self.subscription_housing_header.setStyleSheet("font_color{rgb(204, 204, 204)}")
        self.subscription_housing_header.setScaledContents(False)
        self.subscription_housing_header.setObjectName("subscription_housing_header")
        self.subscription_sublabel = QtWidgets.QLabel(Dialog)
        self.subscription_sublabel.setGeometry(QtCore.QRect(80, 190, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.subscription_sublabel.setFont(font)
        self.subscription_sublabel.setStyleSheet("font_color{rgb(204, 204, 204)}")
        self.subscription_sublabel.setScaledContents(False)
        self.subscription_sublabel.setObjectName("subscription_sublabel")
        self.subscription_label = QtWidgets.QLabel(Dialog)
        self.subscription_label.setGeometry(QtCore.QRect(50, 160, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.subscription_label.setFont(font)
        self.subscription_label.setStyleSheet("font_color{rgb(204, 204, 204)}")
        self.subscription_label.setScaledContents(False)
        self.subscription_label.setObjectName("subscription_label")
        self.go = QtWidgets.QPushButton(Dialog)
        self.go.setGeometry(QtCore.QRect(190, 310, 113, 40))
        self.go.setObjectName("go")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Subscription"))
        self.subscription_housing_header.setText(_translate("Dialog", "Housing"))
        self.subscription_sublabel.setText(
            _translate(
                "Dialog", "Automated emails will be sent once per specified hour."
            )
        )
        self.subscription_label.setText(
            _translate("Dialog", "Would you like automated notifications?")
        )
        self.go.setText(_translate("Dialog", "Go"))
