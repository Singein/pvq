from PySide2.QtWidgets import QApplication, QWidget, QMainWindow
from PySide2.QtCore import Signal, Slot, QUrl, QObject
from PySide2.QtWebChannel import QWebChannel
from PySide2.QtWebEngineWidgets import QWebEngineView
# from ui import Browser
from webview import Browser
from settings import index_html_path
from agent import Agent
import threading
import os


class RenderException(BaseException):
    pass


class Render(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Browser()
        self.ui.setupUi(self)
        self.ui.webEngineView.load(QUrl.fromLocalFile(index_html_path))
        self.init_channel()
        self.slots = None
        self.ui.btn.clicked.connect(self.send_signal)
        self.ui.webEngineView.loadFinished.connect(self.send)

    def send(self, ok):
        if ok:
            print('Load Finished!')
            print(os.getpid())
            # self.ui.btn.clicked.emit()
            self.agent.send_data_pack.emit(os.getpid())

    def init_channel(self):
        self.agent = Agent(self)
        channel = QWebChannel(self.ui.webEngineView.page())
        channel.registerObject("agent", self.agent)
        self.ui.webEngineView.page().setWebChannel(channel)

    def dispatch(self, data_pack):
        if self.slots is None:
            raise RenderException('slots is None')
        slot = data_pack['slot']
        data = data_pack['data']
        self.slots[slot](data)

    def register_slots(self, slots):
        self.slots = slots

    def send_signal(self):
        print(os.getpid())
        self.agent.send_data_pack.emit(str(os.getpid()))
