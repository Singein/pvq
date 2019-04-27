from PySide2.QtWidgets import QApplication
from render import Render
from PySide2.QtCore import Slot
import sys
import os
import time


class MainWindow(Render):
    def __init__(self):
        super().__init__()
        # self.ui.webEngineView.loadFinished.connect(self.send)

    # def send(self, ok):
    #     if ok:
    #         print('Load Finished!')
    #         self.ui.bt


def say_hello(data):
    print('Hello, %s' % data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.register_slots({
        'say_hello': say_hello
    }),
    w.show()
    sys.exit(app.exec_())
