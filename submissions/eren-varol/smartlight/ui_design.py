# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_design.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_LightBackManager(object):
    def setupUi(self, LightBackManager):
        if not LightBackManager.objectName():
            LightBackManager.setObjectName(u"LightBackManager")
        LightBackManager.resize(586, 311)
        font = QFont()
        font.setItalic(False)
        font.setStyleStrategy(QFont.PreferDefault)
        LightBackManager.setFont(font)
        LightBackManager.setMouseTracking(False)
        self.centralwidget = QWidget(LightBackManager)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 561, 281))
        self.pushButton_activate = QPushButton(self.groupBox)
        self.pushButton_activate.setObjectName(u"pushButton_activate")
        self.pushButton_activate.setGeometry(QRect(330, 120, 151, 31))
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.pushButton_activate.setFont(font1)
        self.pushButton_back = QPushButton(self.groupBox)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setGeometry(QRect(160, 120, 161, 31))
        self.pushButton_back.setFont(font1)
        self.pushButton_back.setMouseTracking(False)
        self.lineEdit_color = QLineEdit(self.groupBox)
        self.lineEdit_color.setObjectName(u"lineEdit_color")
        self.lineEdit_color.setGeometry(QRect(160, 80, 321, 26))
        self.sceneName = QLabel(self.groupBox)
        self.sceneName.setObjectName(u"sceneName")
        self.sceneName.setGeometry(QRect(30, 30, 81, 16))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setUnderline(True)
        font2.setStrikeOut(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.sceneName.setFont(font2)
        self.brightness = QLabel(self.groupBox)
        self.brightness.setObjectName(u"brightness")
        self.brightness.setGeometry(QRect(30, 60, 121, 16))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(True)
        font3.setUnderline(True)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.brightness.setFont(font3)
        self.color = QLabel(self.groupBox)
        self.color.setObjectName(u"color")
        self.color.setGeometry(QRect(30, 90, 81, 16))
        self.color.setFont(font3)
        self.lineEdit_sceneName = QLineEdit(self.groupBox)
        self.lineEdit_sceneName.setObjectName(u"lineEdit_sceneName")
        self.lineEdit_sceneName.setGeometry(QRect(160, 20, 321, 26))
        self.label_status = QLabel(self.groupBox)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setGeometry(QRect(310, 160, 201, 81))
        font4 = QFont()
        font4.setFamilies([u"Arial Black"])
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.label_status.setFont(font4)
        self.lineEdit_brightness = QLineEdit(self.groupBox)
        self.lineEdit_brightness.setObjectName(u"lineEdit_brightness")
        self.lineEdit_brightness.setGeometry(QRect(160, 50, 321, 26))
        self.pushButton_cinema = QPushButton(self.groupBox)
        self.pushButton_cinema.setObjectName(u"pushButton_cinema")
        self.pushButton_cinema.setGeometry(QRect(160, 160, 121, 26))
        font5 = QFont()
        font5.setPointSize(13)
        font5.setItalic(False)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.pushButton_cinema.setFont(font5)
        self.pushButton_study = QPushButton(self.groupBox)
        self.pushButton_study.setObjectName(u"pushButton_study")
        self.pushButton_study.setGeometry(QRect(160, 190, 121, 26))
        self.pushButton_sleep = QPushButton(self.groupBox)
        self.pushButton_sleep.setObjectName(u"pushButton_sleep")
        self.pushButton_sleep.setGeometry(QRect(160, 220, 121, 26))
        LightBackManager.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(LightBackManager)
        self.statusbar.setObjectName(u"statusbar")
        LightBackManager.setStatusBar(self.statusbar)

        self.retranslateUi(LightBackManager)

        QMetaObject.connectSlotsByName(LightBackManager)
    # setupUi

    def retranslateUi(self, LightBackManager):
        LightBackManager.setWindowTitle(QCoreApplication.translate("LightBackManager", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("LightBackManager", u"ROOM LIGHTING PANEL", None))
        self.pushButton_activate.setText(QCoreApplication.translate("LightBackManager", u"Activate New Scene", None))
        self.pushButton_back.setText(QCoreApplication.translate("LightBackManager", u"Back to Previous Scene", None))
        self.sceneName.setText(QCoreApplication.translate("LightBackManager", u"Scene Name:", None))
        self.brightness.setText(QCoreApplication.translate("LightBackManager", u"Brightness (0-100):", None))
        self.color.setText(QCoreApplication.translate("LightBackManager", u"Light Color:", None))
        self.label_status.setText(QCoreApplication.translate("LightBackManager", u"No active scene in the system.", None))
        self.pushButton_cinema.setText(QCoreApplication.translate("LightBackManager", u"\U0001f3ac Cinema Mode", None))
        self.pushButton_study.setText(QCoreApplication.translate("LightBackManager", u"\U0001f4da Study Mode", None))
        self.pushButton_sleep.setText(QCoreApplication.translate("LightBackManager", u"\U0001f319 Sleep Mode", None))
    # retranslateUi

