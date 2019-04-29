from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Slot
from render import Render
import sys
import os
import time


class MainWindow(Render):
    def __init__(self):
        super().__init__()
        self.init_connection()

    def init_connection(self):
        self.ui.btn.clicked.connect(self.btn_clicked)
        # 这里我在初始化的时候直接调用一次 btn的click()方法，模拟点击操作
        # 注意观察JS的输出
        self.ui.btn.click()

    @Slot()
    def btn_clicked(self):
        print('Button Clicked!')
        self.agent.send_data_pack.emit('Hello From PySide ~')
        print('Signal Sended!')


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
