# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenJCcBPK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import vs_app_rc

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(379, 357)
        SplashScreen.setStyleSheet(u"background-color: rgba(255, 255, 255,0);")
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setGeometry(QRect(10, 10, 361, 341))
        font = QFont()
        font.setFamily(u"MS Serif")
        self.mainFrame.setFont(font)
        self.mainFrame.setStyleSheet(u"QFrame{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.506, x2:1, y2:0.517, stop:0 rgba(170, 0, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.versionFrame = QFrame(self.mainFrame)
        self.versionFrame.setObjectName(u"versionFrame")
        self.versionFrame.setGeometry(QRect(290, 310, 75, 32))
        self.versionFrame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.versionFrame.setFrameShape(QFrame.StyledPanel)
        self.versionFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.versionFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.versionLabel = QLabel(self.versionFrame)
        self.versionLabel.setObjectName(u"versionLabel")
        font1 = QFont()
        font1.setFamily(u"Humnst777 BlkCn BT")
        self.versionLabel.setFont(font1)
        self.versionLabel.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout.addWidget(self.versionLabel)

        self.logoFrame = QFrame(self.mainFrame)
        self.logoFrame.setObjectName(u"logoFrame")
        self.logoFrame.setGeometry(QRect(20, 80, 321, 80))
        self.logoFrame.setStyleSheet(u"\n"
"background-color: rgba(255, 255, 255, 0);")
        self.logoFrame.setFrameShape(QFrame.StyledPanel)
        self.logoFrame.setFrameShadow(QFrame.Raised)
        self.logoLabel = QLabel(self.logoFrame)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setGeometry(QRect(10, 0, 291, 111))
        self.logoLabel.setStyleSheet(u"image: url(:/images/Media/vs_white.png);")
        self.musicNoteFrame = QFrame(self.mainFrame)
        self.musicNoteFrame.setObjectName(u"musicNoteFrame")
        self.musicNoteFrame.setGeometry(QRect(90, 9, 191, 121))
        self.musicNoteFrame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.musicNoteFrame.setFrameShape(QFrame.StyledPanel)
        self.musicNoteFrame.setFrameShadow(QFrame.Raised)
        self.musicNoteLabel = QLabel(self.musicNoteFrame)
        self.musicNoteLabel.setObjectName(u"musicNoteLabel")
        self.musicNoteLabel.setGeometry(QRect(0, 0, 181, 101))
        self.musicNoteLabel.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"image: url(:/images/Media/musicnotes2.png);")
        self.spotifyFrame = QFrame(self.mainFrame)
        self.spotifyFrame.setObjectName(u"spotifyFrame")
        self.spotifyFrame.setGeometry(QRect(110, 240, 161, 80))
        self.spotifyFrame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.spotifyFrame.setFrameShape(QFrame.StyledPanel)
        self.spotifyFrame.setFrameShadow(QFrame.Raised)
        self.spotifyLabel = QLabel(self.spotifyFrame)
        self.spotifyLabel.setObjectName(u"spotifyLabel")
        self.spotifyLabel.setGeometry(QRect(10, 20, 131, 41))
        self.spotifyLabel.setStyleSheet(u"image: url(:/images/Media/poweredby_2.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.descFrame = QFrame(self.mainFrame)
        self.descFrame.setObjectName(u"descFrame")
        self.descFrame.setGeometry(QRect(70, 160, 261, 31))
        self.descFrame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.descFrame.setFrameShape(QFrame.StyledPanel)
        self.descFrame.setFrameShadow(QFrame.Raised)
        self.descLabel = QLabel(self.descFrame)
        self.descLabel.setObjectName(u"descLabel")
        self.descLabel.setGeometry(QRect(50, 0, 231, 31))
        font2 = QFont()
        font2.setFamily(u"Humanst521 BT")
        font2.setPointSize(12)
        self.descLabel.setFont(font2)
        self.descLabel.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.progbarFrame = QFrame(self.mainFrame)
        self.progbarFrame.setObjectName(u"progbarFrame")
        self.progbarFrame.setGeometry(QRect(30, 190, 311, 61))
        self.progbarFrame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.progbarFrame.setFrameShape(QFrame.StyledPanel)
        self.progbarFrame.setFrameShadow(QFrame.Raised)
        self.progressBar = QProgressBar(self.progbarFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 20, 231, 31))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	/*background-color: rgb(0, 135, 202);*/\n"
"	background-color: rgba(0, 0, 0, 0.2);\n"
"	color: rgb(255, 255, 255);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.506, x2:1, y2:0.517, stop:0 rgba(170, 0, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
"	border-radius: 10px;\n"
"}")
        self.progressBar.setValue(24)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.versionLabel.setText(QCoreApplication.translate("SplashScreen", u"v1.0_02_21", None))
        self.logoLabel.setText("")
        self.musicNoteLabel.setText("")
        self.spotifyLabel.setText("")
        self.descLabel.setText(QCoreApplication.translate("SplashScreen", u"Finding New Music Made Easy", None))
    # retranslateUi
