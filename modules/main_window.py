import os
from typing import Union, List

import cv2
from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import *

from modules.splash_screen import SplashScreen
from modules.worker import Worker
from ui.ui_mainwindow import Ui_MainWindow
from config import allow_extensions


class MainWindow(QMainWindow):
    dragPos: int
    path_to_file: Union[str, None] = None
    save_results: bool = False

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

        ##==> Какие-то кнопошки
        ################################################
        self.ui.StartAIBtn.clicked.connect(self.start_ai_working)
        self.ui.BackBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.save_to_folder_checkbox.stateChanged.connect(
            lambda: setattr(self, "save_results", self.ui.save_to_folder_checkbox.isChecked())
        )

    def start_ai_working(self):
        if self.path_to_file is None or self.path_to_file == "":
            QMessageBox.critical(None, "Ошибка", "Выберите файл!")
            return

        self.splashscreen = SplashScreen(
            lambda: self.end_ai_working(None),
            automatic=False,
            allocated_label="AI Working",
            unallocated_label="Loading..."
        )

        self.close()  # Закрываем главное окно на время выполнения
        self.custom_thread = Worker(self.path_to_file, self.save_results)  # Создание процесса
        self.custom_thread.start()  # Выполнение процесса
        self.custom_thread.update_progress.connect(lambda x: self.splashscreen.progress(x))  # Обновление ProgressBar
        self.custom_thread.progress_increment.connect(lambda: self.splashscreen.progress(self.splashscreen.counter+1))
        self.custom_thread.end_working.connect(lambda results: self.end_ai_working(results))  # Завершение работы АИ

    def end_ai_working(self, results: Union[None, list]):
        if hasattr(self, "splashscreen"):
            if self.splashscreen.isVisible():
                self.splashscreen.close()

        self.show()

        if results is not None and len(results) > 0:
            self.add_defect_elements(results)
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.delete_file_in_drag_and_drop()

    def add_defect_elements(self, results: List[dict]) -> None:
        def open_img(item):
            data = item.data(Qt.UserRole)
            cv2.imshow(data["filename"], data["image"])
            cv2.waitKey(0)

        self.ui.defectList.clear()
        for res in results:
            new_item = QListWidgetItem(f"Файл: {res['filename']}\nКлассификация: {res['type']}\n{res['cors']}")
            new_item.setData(Qt.UserRole, res)

            self.ui.defectList.addItem(new_item)

        self.ui.defectList.itemClicked.connect(open_img)
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
        self.change_focus_in_drag_and_drop(False)
        url = event.mimeData().urls()[-1].toLocalFile()

        if os.path.isfile(url):
            if os.path.splitext(url)[1] not in allow_extensions:
                QMessageBox.critical(None, "Error", "Неверное расширение файла")
                return

        self.path_to_file = url
        self.ui.filename.setText(os.path.basename(url))
        self.ui.el_in_drag_and_drop.show()

    def move_window(self, event: QMouseEvent):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()
