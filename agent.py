from PySide2.QtCore import QObject, Signal, Slot
import json


class Agent(QObject):
    """
    用于和JS进行数据交互的模型
    """

    send_data_pack = Signal(str)

    def __init__(self, dispatcher):
        super().__init__()
        self.dispatcher = dispatcher

    @Slot(str)
    def data_pack_received(self, data_pack):
        data_pack = json.loads(data_pack)
        self.dispatcher.dispatch(data_pack)
