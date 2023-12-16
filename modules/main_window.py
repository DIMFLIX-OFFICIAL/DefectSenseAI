import functools
import os
from typing import Union

from PySide6 import QtCore
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QMouseEvent, QIcon, QFont
from PySide6.QtWidgets import *

from modules.splash_screen import SplashScreen
from modules.worker import Worker
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

        ##==> Старт обработки
        ################################################
        self.ui.StartAIBtn.clicked.connect(self.start_ai_working)
        self.ui.BackBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

    def start_ai_working(self):

        def end_ai_working():
            self.ui.stackedWidget.setCurrentIndex(1)
            self.show()

        self.splashscreen = SplashScreen(
            lambda: end_ai_working(),
            automatic=False,
            allocated_label="AI Working",
            unallocated_label="Loading..."
        )

        self.close()  # Закрываем главное окно на время выполнения
        self.custom_thread = Worker()  # Создание процесса
        self.custom_thread.start()  # Выполнение процесса
        self.custom_thread.middle_result.connect(lambda x: self.splashscreen.progress(x))  # Обновление ProgressBar
        self.custom_thread.end_working.connect(lambda x: self.add_defect_elements(x))

    def add_defect_elements(self, list_of_paths: list):
        self.ui.defectList.clear()

        for path in list_of_paths:
            self.ui.defectList.addItem(path + "\nХуй повис")

        self.ui.DefectsFinded.setText(f"Найдено дефектов: {self.ui.defectList.count()}")

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