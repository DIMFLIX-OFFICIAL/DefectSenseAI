import time

from PySide6.QtCore import Signal, QThread


class Worker(QThread):
    middle_result = Signal(int)
    end_working = Signal(list)

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(101):
            self.middle_result.emit(i)
            time.sleep(0.015)

        self.end_working.emit(["asjdhasd", "1231opjsaod", "9486jashfgsdgf"])
