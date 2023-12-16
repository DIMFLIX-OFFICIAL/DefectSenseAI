import sys, os
from typing import Union

from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import (QColor, QMouseEvent)
from PySide6.QtWidgets import *

from ui.ui_splashscreen import Ui_SplashScreen
from ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    dragPos: int
    path_to_file: Union[str, None] = None

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ##==> Удаление рамок и прозрачность фона
        ##################################################
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Set background to transparent

        ##==> Drag And Drop
        ##################################################
        self.ui.del_element_in_drag_end_drop.clicked.connect(self.delete_file_in_drag_and_drop)
        self.ui.el_in_drag_and_drop.hide()

        self.ui.drag_and_drop.setAcceptDrops(True)
        self.ui.drag_and_drop.dragEnterEvent = self.drag_and_drop_ev_enter
        self.ui.drag_and_drop.dropEvent = self.drag_and_drop_ev_drop
        self.ui.drag_and_drop.dragLeaveEvent = lambda e: self.change_focus_in_drag_and_drop(False)

        ##==> Кнопки главного окна и перемещение окна
        ################################################
        self.ui.header.mouseMoveEvent = self.move_window
        self.ui.Title.mouseMoveEvent = self.move_window
        self.ui.close_btn.clicked.connect(self.close)
        self.ui.minimize_btn.clicked.connect(self.showMinimized)



    def delete_file_in_drag_and_drop(self):
        self.path_to_file = None
        self.ui.filename.setText("")
        self.ui.el_in_drag_and_drop.hide()

    def change_focus_in_drag_and_drop(self, is_active, color="#4C446D"):
        if is_active:
            self.ui.drag_and_drop.setStyleSheet(
                self.ui.drag_and_drop.styleSheet() + f"background-color: {color};"
            )
        else:
            self.ui.drag_and_drop.setStyleSheet(
                self.ui.drag_and_drop.styleSheet().replace(f"background-color: {color};", "")
            )

    def drag_and_drop_ev_enter(self, event):
        self.change_focus_in_drag_and_drop(True)
        event.accept() if event.mimeData().hasUrls() else event.ignore()

    def drag_and_drop_ev_drop(self, event):
        for url in event.mimeData().urls():
            self.change_focus_in_drag_and_drop(False)
            self.path_to_file = url.toLocalFile()
            self.ui.filename.setText(os.path.basename(url.toLocalFile()))
            self.ui.el_in_drag_and_drop.show()

    def move_window(self, event: QMouseEvent):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()


class SplashScreen(QMainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.counter = 0
        self.jumper = 0

        self.progressbar_set_val(0)  # Set Default Value for Progress Bar

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
        self.timer.start(15)

        self.show()

    def progress(self):
        value = self.counter

        if value > self.jumper:
            self.ui.labelPercentage.setText(
                "<p>"
                f"<span style=\" font-size:68pt;\">{self.jumper}</span>"
                "<span style=\" font-size:58pt; vertical-align:super;\">%</span>"
                "</p>"
            )
            self.jumper += 1

        self.progressbar_set_val(value)

        if self.counter > 100:
            self.timer.stop()
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()

        self.counter += 0.5  # INCREASE COUNTER

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


if __name__ == "__main__":
    app = QApplication()
    window = SplashScreen()
    sys.exit(app.exec())
