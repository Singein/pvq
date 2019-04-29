from PySide2.QtWidgets import QApplication, QWidget, QMainWindow
from PySide2.QtCore import QUrl, QObject
from PySide2.QtWebChannel import QWebChannel
from PySide2.QtWebEngineWidgets import QWebEngineView
from ui.webview import Browser
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
        self.init_channel()
        self.slots = None

    def init_channel(self):
        self.ui.webEngineView.load(QUrl.fromLocalFile(index_html_path))
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
