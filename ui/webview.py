from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2 import QtCore, QtGui, QtWidgets


class Browser(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Browser")
        MainWindow.resize(975, 804)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.webEngineView = QWebEngineView(self.centralwidget)
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout.addWidget(self.webEngineView)
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setObjectName("btn")
        self.verticalLayout.addWidget(self.btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 975, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate(
            "MainWindow", "MainWindow", None, -1))
        self.btn.setText(QtWidgets.QApplication.translate(
            "MainWindow", "PushButton", None, -1))
