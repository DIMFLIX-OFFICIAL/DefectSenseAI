import sys
import logging

from PySide6.QtWidgets import *

from modules.main_window import MainWindow
from modules.splash_screen import SplashScreen


if __name__ == "__main__":
    app = QApplication()
    main_window = MainWindow()
    logging.getLogger("utils.general").setLevel(logging.WARNING)
    window = SplashScreen(lambda: main_window.show(), automatic=True)
    sys.exit(app.exec())
