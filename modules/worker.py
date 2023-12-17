import glob
import os
import time
from datetime import datetime

import cv2
from PySide6.QtCore import Signal, QThread, QDir
from ultralytics import YOLO

from config import allow_extensions


class Worker(QThread):
    update_progress = Signal(int)
    end_working = Signal(list)
    progress_increment = Signal()

    def __init__(self, path_to_file: str, save_result: bool):
        self.path_to_file = path_to_file
        self.save_result = save_result

        super().__init__()

    @staticmethod
    def is_image_file(filename):
        return any(extension in filename for extension in allow_extensions)

    def find_paths(self, path):
        result = []

        if os.path.isfile(path):
            if self.is_image_file(path):
                result.append(path)
        elif os.path.isdir(path):
            result = []
            for ext in allow_extensions:
                result += glob.glob(os.path.join(path, f'**/*{ext}'), recursive=True)

        return result

    def run(self):
        paths = self.find_paths(self.path_to_file)

        if not QDir().exists("results"):
            QDir().mkdir("results")

        if len(paths) == 0:
            self.update_progress.emit(100)
            self.end_working.emit(None)
            return
        else:
            for i in range(51):
                time.sleep(0.0015)
                self.update_progress.emit(i)

            model = YOLO('./weights/best.pt')
            results = model(paths)
            response = []

            for result in results:
                path = result.path
                filename = os.path.basename(path)

                for box in result[0].boxes:
                    class_id = result.names[box.cls[0].item()]
                    cords = box.xyxy[0].tolist()
                    cords = [round(x) for x in cords]

                    img = cv2.imread(path)
                    cv2.rectangle(img, (cords[0], cords[1]), (cords[2], cords[3]), (0, 255, 255), 5)

                    if self.save_result:
                        foldername = str(datetime.now())[:-7].replace(":", "-")
                        QDir().mkdir(f"./results/{foldername}")
                        cv2.imwrite(f'./results/{foldername}/{filename}', img)

                    if class_id != "не дефект":
                        response.append({"type": class_id, "image": img, "filename": filename})

                for i in range(50//len(results)):
                    self.progress_increment.emit()
                    time.sleep(0.015)

            self.update_progress.emit(100)
            self.end_working.emit(response)
