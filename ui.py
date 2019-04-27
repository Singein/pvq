# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'webView.ui',
# licensing of 'webView.ui' applies.
#
# Created: Sat Apr 27 09:42:53 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2 import QtCore, QtGui, QtWidgets


class Browser(object):
    def setupUi(self, Form):
        Form.setObjectName("Browser")
        Form.resize(795, 624)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.webEngineView = QWebEngineView(Form)
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout.addWidget(self.webEngineView)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QtWidgets.QApplication.translate("Form", "Form", None, -1))
