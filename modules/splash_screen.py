import math
from typing import Callable

from PySide6 import QtCore
from PySide6.QtGui import QColor
from PySide6.QtWidgets import *

from ui.ui_splashscreen import Ui_SplashScreen


class SplashScreen(QMainWindow):
    counter: int = 0

    def __init__(self,
                 callback: Callable,
                 automatic: bool = True,
                 allocated_label: str = "Launch",
                 unallocated_label: str = "Loading...") -> None:
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.callback = callback

        ##==> Set Default Values
        #################################################
        self.progressbar_set_val(0)
        self.ui.labelAllocated.setText(allocated_label)
        self.ui.labelUnallocated.setText(unallocated_label)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Set background to transparent

        ##==> APPLY DROP SHADOW EFFECT
        ######################################
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        ##==> QTIMER START
        ##################################
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.show()

        if automatic:
            self.timer.start(30)

    def progress(self, value=None):
        if self.counter <= 100:

            if value is None:
                self.counter += 1
            else:
                self.counter = value

            self.ui.labelPercentage.setText(
                "<p>"
                f"<span style=\" font-size:68pt;\">{math.floor(self.counter)}</span>"
                "<span style=\" font-size:58pt; vertical-align:super;\">%</span>"
                "</p>"
            )

        self.progressbar_set_val(self.counter)

        if self.counter >= 100:
            self.timer.stop()
            self.close()
            self.callback()

    def progressbar_set_val(self, value):
        progress = (100 - value) / 100.0
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        style = (
            "QFrame{"
            "border-radius: 150px;"
            "background-color: qconicalgradient("
            f"cx:0.5, cy:0.5, angle:90, stop:{stop_1} rgba(147, 130, 255, 0), stop:{stop_2} rgba(147, 130, 255, 255));"
            "}"
        )

        self.ui.circularProgress.setStyleSheet(style)
