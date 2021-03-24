# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vsZUnYOS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import vs_app_rc

class Ui_VSMain(object):
    def setupUi(self, VSMain):
        if not VSMain.objectName():
            VSMain.setObjectName(u"VSMain")
        VSMain.setWindowModality(Qt.NonModal)
        VSMain.setEnabled(True)
        VSMain.resize(1200, 645)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VSMain.sizePolicy().hasHeightForWidth())
        VSMain.setSizePolicy(sizePolicy)
        VSMain.setMinimumSize(QSize(1200, 645))
        VSMain.setMaximumSize(QSize(16777215, 16777215))
        VSMain.setSizeIncrement(QSize(1, 1))
        VSMain.setBaseSize(QSize(1200, 645))
        icon = QIcon()
        icon.addFile(u"../../.designer/backup/Media/vs.ico", QSize(), QIcon.Normal, QIcon.Off)
        VSMain.setWindowIcon(icon)
        VSMain.setAutoFillBackground(False)
        VSMain.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(VSMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.506, x2:1, y2:0.517, stop:0 rgba(170, 0, 255, 255), stop:1 rgba(0, 170, 255, 255));")
        self.headerFrame = QFrame(self.centralwidget)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setGeometry(QRect(0, 0, 1201, 71))
        sizePolicy.setHeightForWidth(self.headerFrame.sizePolicy().hasHeightForWidth())
        self.headerFrame.setSizePolicy(sizePolicy)
        self.headerFrame.setStyleSheet(u"QFrame{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.506, x2:1, y2:0.517, stop:0 rgba(170, 0, 255, 255), stop:1 rgba(0, 170, 255, 255));\n"
"}\n"
"\n"
"body, html {\n"
"	-webkit-app-region: drag;\n"
"}")
        self.headerFrame.setFrameShape(QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Raised)
        self.vsLogo = QLabel(self.headerFrame)
        self.vsLogo.setObjectName(u"vsLogo")
        self.vsLogo.setGeometry(QRect(470, 0, 241, 51))
        sizePolicy.setHeightForWidth(self.vsLogo.sizePolicy().hasHeightForWidth())
        self.vsLogo.setSizePolicy(sizePolicy)
        self.vsLogo.setStyleSheet(u"QLabel{\n"
"	image: url(:/images/Media/vs_white.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"")
        self.vsLogo.setScaledContents(True)
        self.descLabel = QLabel(self.headerFrame)
        self.descLabel.setObjectName(u"descLabel")
        self.descLabel.setGeometry(QRect(550, 40, 191, 31))
        sizePolicy.setHeightForWidth(self.descLabel.sizePolicy().hasHeightForWidth())
        self.descLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Humanst521 BT")
        font.setPointSize(9)
        self.descLabel.setFont(font)
        self.descLabel.setAutoFillBackground(False)
        self.descLabel.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: white;")
        self.topRightButtons = QFrame(self.headerFrame)
        self.topRightButtons.setObjectName(u"topRightButtons")
        self.topRightButtons.setGeometry(QRect(1080, 0, 120, 41))
        sizePolicy.setHeightForWidth(self.topRightButtons.sizePolicy().hasHeightForWidth())
        self.topRightButtons.setSizePolicy(sizePolicy)
        self.topRightButtons.setMinimumSize(QSize(120, 0))
        self.topRightButtons.setMaximumSize(QSize(16777215, 16777215))
        self.topRightButtons.setStyleSheet(u"border-style: none;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.topRightButtons.setFrameShape(QFrame.WinPanel)
        self.topRightButtons.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.topRightButtons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.minimizeButton = QPushButton(self.topRightButtons)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setWeight(50)
        self.minimizeButton.setFont(font1)
        self.minimizeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimizeButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/icons8-macos-minimize-90_white.png);\n"
"	height: 30px;\n"
"	width: 30px;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/icons8-macos-minimize-90_white.png);\n"
"	height: 30px;\n"
"	width: 30px;\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"}")
        self.minimizeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.minimizeButton)

        self.restoreButton = QPushButton(self.topRightButtons)
        self.restoreButton.setObjectName(u"restoreButton")
        self.restoreButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.restoreButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/icons8-macos-maximize-90_white.png);\n"
"	height: 30px;\n"
"	width: 30px;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/icons8-macos-maximize-90_white.png);\n"
"	height: 30px;\n"
"	width: 30px;\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout.addWidget(self.restoreButton)

        self.closeButton = QPushButton(self.topRightButtons)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/icons8-macos-close-90_white.png);\n"
"	height: 30px;\n"
"	width: 30px;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/icons8-macos-close-90_white.png);\n"
"	height: 30px;\n"
"	width: 30px;\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout.addWidget(self.closeButton)

        self.footerFrame = QFrame(self.centralwidget)
        self.footerFrame.setObjectName(u"footerFrame")
        self.footerFrame.setGeometry(QRect(0, 599, 1201, 51))
        sizePolicy.setHeightForWidth(self.footerFrame.sizePolicy().hasHeightForWidth())
        self.footerFrame.setSizePolicy(sizePolicy)
        self.footerFrame.setMinimumSize(QSize(0, 0))
        self.footerFrame.setMaximumSize(QSize(16777215, 16777215))
        self.footerFrame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.506, x2:1, y2:0.517, stop:0 rgba(170, 0, 255, 255), stop:1 rgba(0, 170, 255, 255));")
        self.footerFrame.setFrameShape(QFrame.StyledPanel)
        self.footerFrame.setFrameShadow(QFrame.Raised)
        self.spotifyLabel = QLabel(self.footerFrame)
        self.spotifyLabel.setObjectName(u"spotifyLabel")
        self.spotifyLabel.setGeometry(QRect(560, 0, 121, 41))
        sizePolicy.setHeightForWidth(self.spotifyLabel.sizePolicy().hasHeightForWidth())
        self.spotifyLabel.setSizePolicy(sizePolicy)
        self.spotifyLabel.setStyleSheet(u"QLabel{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	\n"
"	image: url(:/images/Media/poweredby_2.png);\n"
"}")
        self.spotifyLabel.setScaledContents(True)
        self.sizeGrip = QFrame(self.footerFrame)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setGeometry(QRect(1190, 40, 20, 20))
        self.sizeGrip.setMinimumSize(QSize(20, 20))
        self.sizeGrip.setMaximumSize(QSize(20, 20))
        self.sizeGrip.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)
        self.bodyFrame = QFrame(self.centralwidget)
        self.bodyFrame.setObjectName(u"bodyFrame")
        self.bodyFrame.setGeometry(QRect(0, 0, 1201, 16777215))
        self.bodyFrame.setMinimumSize(QSize(1200, 651))
        self.bodyFrame.setSizeIncrement(QSize(1, 1))
        self.bodyFrame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.bodyFrame.setFrameShape(QFrame.StyledPanel)
        self.bodyFrame.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.bodyFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 70, 1201, 531))
        self.stackedWidget.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.buttonFrame = QFrame(self.homePage)
        self.buttonFrame.setObjectName(u"buttonFrame")
        self.buttonFrame.setGeometry(QRect(60, 120, 1081, 201))
        sizePolicy.setHeightForWidth(self.buttonFrame.sizePolicy().hasHeightForWidth())
        self.buttonFrame.setSizePolicy(sizePolicy)
        self.buttonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.buttonFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.buttonFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.profileLabel = QLabel(self.buttonFrame)
        self.profileLabel.setObjectName(u"profileLabel")
        font2 = QFont()
        font2.setFamily(u"Humnst777 BlkCn BT")
        font2.setPointSize(12)
        self.profileLabel.setFont(font2)
        self.profileLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.profileLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.profileLabel, 2, 2, 1, 1)

        self.profileButton = QPushButton(self.buttonFrame)
        self.profileButton.setObjectName(u"profileButton")
        self.profileButton.setMinimumSize(QSize(150, 150))
        self.profileButton.setMaximumSize(QSize(150, 150))
        self.profileButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.profileButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/profile.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/profile.png);\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	border-style: none;\n"
"	border-radius: 40px;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.profileButton, 0, 2, 1, 1)

        self.settingsButton = QPushButton(self.buttonFrame)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setMinimumSize(QSize(150, 150))
        self.settingsButton.setMaximumSize(QSize(150, 150))
        self.settingsButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingsButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/settings.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/settings.png);\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	border-style: none;\n"
"	border-radius: 40px;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.settingsButton, 0, 3, 1, 1)

        self.shareButton = QPushButton(self.buttonFrame)
        self.shareButton.setObjectName(u"shareButton")
        self.shareButton.setMinimumSize(QSize(150, 150))
        self.shareButton.setMaximumSize(QSize(150, 150))
        self.shareButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.shareButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/share.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/share.png);\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	border-style: none;\n"
"	border-radius: 40px;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.shareButton, 0, 1, 1, 1)

        self.createButton = QPushButton(self.buttonFrame)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setMinimumSize(QSize(150, 150))
        self.createButton.setMaximumSize(QSize(150, 150))
        self.createButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.createButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/create.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/create.png);\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	border-style: none;\n"
"	border-radius: 40px;\n"
"}")

        self.gridLayout.addWidget(self.createButton, 0, 0, 1, 1)

        self.shareLabel = QLabel(self.buttonFrame)
        self.shareLabel.setObjectName(u"shareLabel")
        self.shareLabel.setFont(font2)
        self.shareLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.shareLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.shareLabel, 2, 1, 1, 1)

        self.createLabel = QLabel(self.buttonFrame)
        self.createLabel.setObjectName(u"createLabel")
        self.createLabel.setFont(font2)
        self.createLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.createLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.createLabel, 2, 0, 1, 1)

        self.settingsLabel = QLabel(self.buttonFrame)
        self.settingsLabel.setObjectName(u"settingsLabel")
        self.settingsLabel.setFont(font2)
        self.settingsLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.settingsLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.settingsLabel, 2, 3, 1, 1)

        self.stackedWidget.addWidget(self.homePage)
        self.createPage = QWidget()
        self.createPage.setObjectName(u"createPage")
        self.homeButtonFrame = QFrame(self.createPage)
        self.homeButtonFrame.setObjectName(u"homeButtonFrame")
        self.homeButtonFrame.setGeometry(QRect(10, 0, 51, 51))
        self.homeButtonFrame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.homeButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.homeButtonFrame.setFrameShadow(QFrame.Raised)
        self.homeButton = QPushButton(self.homeButtonFrame)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setGeometry(QRect(10, 10, 31, 31))
        self.homeButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/goback.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/goback.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: none;\n"
"	border-radius: 40px;\n"
"}")
        self.buttonFrame_2 = QFrame(self.createPage)
        self.buttonFrame_2.setObjectName(u"buttonFrame_2")
        self.buttonFrame_2.setGeometry(QRect(300, 120, 601, 201))
        self.buttonFrame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.buttonFrame_2.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.buttonFrame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.createArtistLabel = QLabel(self.buttonFrame_2)
        self.createArtistLabel.setObjectName(u"createArtistLabel")
        self.createArtistLabel.setFont(font2)
        self.createArtistLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.createArtistLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.createArtistLabel, 2, 0, 1, 1)

        self.createArtistButton = QPushButton(self.buttonFrame_2)
        self.createArtistButton.setObjectName(u"createArtistButton")
        self.createArtistButton.setMinimumSize(QSize(150, 150))
        self.createArtistButton.setMaximumSize(QSize(150, 150))
        self.createArtistButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.createArtistButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/create.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/create.png);\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	border-style: none;\n"
"	border-radius: 40px;\n"
"}")

        self.gridLayout_2.addWidget(self.createArtistButton, 0, 0, 1, 1)

        self.createGenreLabel = QLabel(self.buttonFrame_2)
        self.createGenreLabel.setObjectName(u"createGenreLabel")
        self.createGenreLabel.setFont(font2)
        self.createGenreLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.createGenreLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.createGenreLabel, 2, 1, 1, 1)

        self.createGenreButton = QPushButton(self.buttonFrame_2)
        self.createGenreButton.setObjectName(u"createGenreButton")
        self.createGenreButton.setMinimumSize(QSize(150, 150))
        self.createGenreButton.setMaximumSize(QSize(150, 150))
        self.createGenreButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.createGenreButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/share.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/share.png);\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	border-style: none;\n"
"	border-radius: 40px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.createGenreButton, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.createPage)
        self.sharePage = QWidget()
        self.sharePage.setObjectName(u"sharePage")
        self.homeButtonFrame_2 = QFrame(self.sharePage)
        self.homeButtonFrame_2.setObjectName(u"homeButtonFrame_2")
        self.homeButtonFrame_2.setGeometry(QRect(10, 0, 51, 51))
        self.homeButtonFrame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.homeButtonFrame_2.setFrameShape(QFrame.StyledPanel)
        self.homeButtonFrame_2.setFrameShadow(QFrame.Raised)
        self.homeButton_2 = QPushButton(self.homeButtonFrame_2)
        self.homeButton_2.setObjectName(u"homeButton_2")
        self.homeButton_2.setGeometry(QRect(10, 10, 31, 31))
        self.homeButton_2.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/goback.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/goback.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: none;\n"
"	border-radius: 40px;\n"
"}")
        self.stackedWidget.addWidget(self.sharePage)
        self.profilePage = QWidget()
        self.profilePage.setObjectName(u"profilePage")
        self.homeButtonFrame_3 = QFrame(self.profilePage)
        self.homeButtonFrame_3.setObjectName(u"homeButtonFrame_3")
        self.homeButtonFrame_3.setGeometry(QRect(10, 0, 51, 51))
        self.homeButtonFrame_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.homeButtonFrame_3.setFrameShape(QFrame.StyledPanel)
        self.homeButtonFrame_3.setFrameShadow(QFrame.Raised)
        self.homeButton_3 = QPushButton(self.homeButtonFrame_3)
        self.homeButton_3.setObjectName(u"homeButton_3")
        self.homeButton_3.setGeometry(QRect(10, 10, 31, 31))
        self.homeButton_3.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/goback.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/goback.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: none;\n"
"	border-radius: 40px;\n"
"}")
        self.stackedWidget.addWidget(self.profilePage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.homeButtonFrame_4 = QFrame(self.settingsPage)
        self.homeButtonFrame_4.setObjectName(u"homeButtonFrame_4")
        self.homeButtonFrame_4.setGeometry(QRect(10, 0, 51, 51))
        self.homeButtonFrame_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.homeButtonFrame_4.setFrameShape(QFrame.StyledPanel)
        self.homeButtonFrame_4.setFrameShadow(QFrame.Raised)
        self.homeButton_4 = QPushButton(self.homeButtonFrame_4)
        self.homeButton_4.setObjectName(u"homeButton_4")
        self.homeButton_4.setGeometry(QRect(10, 10, 31, 31))
        self.homeButton_4.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/goback.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/goback.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: none;\n"
"	border-radius: 40px;\n"
"}")
        self.stackedWidget.addWidget(self.settingsPage)
        VSMain.setCentralWidget(self.centralwidget)
        self.bodyFrame.raise_()
        self.headerFrame.raise_()
        self.footerFrame.raise_()

        self.retranslateUi(VSMain)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(VSMain)
    # setupUi

    def retranslateUi(self, VSMain):
        VSMain.setWindowTitle(QCoreApplication.translate("VSMain", u"VibeShare: Playlist Generator", None))
        self.vsLogo.setText("")
        self.descLabel.setText(QCoreApplication.translate("VSMain", u"Finding New Music Made Easy", None))
        self.minimizeButton.setText("")
        self.restoreButton.setText("")
        self.closeButton.setText("")
        self.spotifyLabel.setText("")
        self.profileLabel.setText(QCoreApplication.translate("VSMain", u"Profile", None))
        self.profileButton.setText("")
        self.settingsButton.setText("")
        self.shareButton.setText("")
        self.createButton.setText("")
        self.shareLabel.setText(QCoreApplication.translate("VSMain", u"Share", None))
        self.createLabel.setText(QCoreApplication.translate("VSMain", u"Create+", None))
        self.settingsLabel.setText(QCoreApplication.translate("VSMain", u"Settings", None))
        self.homeButton.setText("")
        self.createArtistLabel.setText(QCoreApplication.translate("VSMain", u"Based On Artist", None))
        self.createArtistButton.setText("")
        self.createGenreLabel.setText(QCoreApplication.translate("VSMain", u"Based on Genre", None))
        self.createGenreButton.setText("")
        self.homeButton_2.setText("")
        self.homeButton_3.setText("")
        self.homeButton_4.setText("")
    # retranslateUi

