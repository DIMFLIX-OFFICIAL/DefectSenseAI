# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import ui.mainwindow_rc as resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(392, 596)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.backgground = QFrame(self.centralwidget)
        self.backgground.setObjectName(u"backgground")
        self.backgground.setStyleSheet(u"QFrame {\n"
"	background-color: #3C3656;\n"
"	border-radius: 25px;\n"
"}")
        self.backgground.setFrameShape(QFrame.StyledPanel)
        self.backgground.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.backgground)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_area = QFrame(self.backgground)
        self.main_area.setObjectName(u"main_area")
        self.main_area.setFrameShape(QFrame.StyledPanel)
        self.main_area.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_area)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.drag_and_drop = QFrame(self.main_area)
        self.drag_and_drop.setObjectName(u"drag_and_drop")
        self.drag_and_drop.setMaximumSize(QSize(16777215, 350))
        self.drag_and_drop.setStyleSheet(u"border: 5px solid #9382FF;\n"
"border-style: dashed;\n"
"")
        self.drag_and_drop.setFrameShape(QFrame.StyledPanel)
        self.drag_and_drop.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.drag_and_drop)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.drag_and_drop_title = QLabel(self.drag_and_drop)
        self.drag_and_drop_title.setObjectName(u"drag_and_drop_title")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.drag_and_drop_title.setFont(font)
        self.drag_and_drop_title.setStyleSheet(u"QLabel {\n"
"	border: none;\n"
"	color: #FFFFFF;\n"
"}")

        self.verticalLayout_3.addWidget(self.drag_and_drop_title, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.el_in_drag_and_drop = QFrame(self.drag_and_drop)
        self.el_in_drag_and_drop.setObjectName(u"el_in_drag_and_drop")
        self.el_in_drag_and_drop.setMinimumSize(QSize(80, 30))
        self.el_in_drag_and_drop.setMaximumSize(QSize(16777215, 30))
        self.el_in_drag_and_drop.setStyleSheet(u"border: none; \n"
"background-color: #564D7A; \n"
"border-radius: 15px;")
        self.el_in_drag_and_drop.setFrameShape(QFrame.StyledPanel)
        self.el_in_drag_and_drop.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.el_in_drag_and_drop)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 3, 0)
        self.filename = QLabel(self.el_in_drag_and_drop)
        self.filename.setObjectName(u"filename")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.filename.setFont(font1)
        self.filename.setStyleSheet(u"color: #FFFFFF")

        self.horizontalLayout_2.addWidget(self.filename)

        self.del_element_in_drag_end_drop = QPushButton(self.el_in_drag_and_drop)
        self.del_element_in_drag_end_drop.setObjectName(u"del_element_in_drag_end_drop")
        self.del_element_in_drag_end_drop.setMinimumSize(QSize(30, 30))
        self.del_element_in_drag_end_drop.setMaximumSize(QSize(30, 30))
        self.del_element_in_drag_end_drop.setStyleSheet(u"border: none;\n"
"background-color: transparent;")
        icon = QIcon()
        icon.addFile(u":/close/resources/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.del_element_in_drag_end_drop.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.del_element_in_drag_end_drop)


        self.verticalLayout_3.addWidget(self.el_in_drag_and_drop, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.drag_and_drop)

        self.save_to_folder_checkbox = QCheckBox(self.main_area)
        self.save_to_folder_checkbox.setObjectName(u"save_to_folder_checkbox")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.save_to_folder_checkbox.setFont(font2)
        self.save_to_folder_checkbox.setStyleSheet(u"QCheckBox {\n"
"	background: #423B5E;\n"
"	border-radius: 10px;\n"
"	padding-left: 10%;\n"
"	padding-top: 10px; \n"
"	padding-bottom: 10px; \n"
"    color: #FFFFFF;\n"
"    spacing: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 24px;\n"
"    height: 24px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 2px solid #564D7A;\n"
"    background: #4C446D;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border: 2px solid #9382FF;\n"
"    background: #9382FF;\n"
"	image: url(:/check/resources/check.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover,\n"
"QCheckBox::indicator:checked:hover {\n"
"    border: 2px solid #9382FF;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/check/C:/Users/dimap/Downloads/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_to_folder_checkbox.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.save_to_folder_checkbox)

        self.StartAIBtn = QPushButton(self.main_area)
        self.StartAIBtn.setObjectName(u"StartAIBtn")
        self.StartAIBtn.setMinimumSize(QSize(0, 50))
        self.StartAIBtn.setMaximumSize(QSize(16777215, 50))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.StartAIBtn.setFont(font3)
        self.StartAIBtn.setStyleSheet(u"QPushButton {\n"
"	background-color: #9382FF;\n"
"	border: none;\n"
"	border-radius: 15px;\n"
"	color: #FFFFFF;\n"
"}")

        self.verticalLayout_2.addWidget(self.StartAIBtn)


        self.gridLayout.addWidget(self.main_area, 1, 0, 1, 1)

        self.header = QFrame(self.backgground)
        self.header.setObjectName(u"header")
        self.header.setMaximumSize(QSize(16777215, 40))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Title = QLabel(self.header)
        self.Title.setObjectName(u"Title")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.Title.setFont(font4)
        self.Title.setStyleSheet(u"QLabel {\n"
"	color: #FFFFFF;\n"
"}")

        self.horizontalLayout.addWidget(self.Title)

        self.maximize_btn = QPushButton(self.header)
        self.maximize_btn.setObjectName(u"maximize_btn")
        self.maximize_btn.setMinimumSize(QSize(20, 20))
        self.maximize_btn.setMaximumSize(QSize(20, 20))
        self.maximize_btn.setStyleSheet(u"background-color: rgb(0, 255, 0);\n"
"border-radius: 10px;")

        self.horizontalLayout.addWidget(self.maximize_btn)

        self.minimize_btn = QPushButton(self.header)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setMinimumSize(QSize(20, 20))
        self.minimize_btn.setMaximumSize(QSize(20, 20))
        self.minimize_btn.setStyleSheet(u"background-color: rgb(255, 255, 0);\n"
"	border-radius: 10px;")

        self.horizontalLayout.addWidget(self.minimize_btn)

        self.close_btn = QPushButton(self.header)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(20, 20))
        self.close_btn.setMaximumSize(QSize(20, 20))
        self.close_btn.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"	border-radius: 10px;")

        self.horizontalLayout.addWidget(self.close_btn)


        self.gridLayout.addWidget(self.header, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.backgground)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DEFFECT SENSE AI", None))
        self.drag_and_drop_title.setText(QCoreApplication.translate("MainWindow", u"Drop your file here!", None))
        self.filename.setText(QCoreApplication.translate("MainWindow", u"File.txt", None))
        self.del_element_in_drag_end_drop.setText("")
        self.save_to_folder_checkbox.setText(QCoreApplication.translate("MainWindow", u"Save to folder \"Results\"", None))
        self.StartAIBtn.setText(QCoreApplication.translate("MainWindow", u"Start Processing", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"<html>\n"
"<body>\n"
"<p>\n"
"DEFECT SENSE <span style=\"color: #9382FF;\">AI</span>\n"
"</p>\n"
"</body>\n"
"</html>", None))
        self.maximize_btn.setText("")
        self.minimize_btn.setText("")
        self.close_btn.setText("")
    # retranslateUi

