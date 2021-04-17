# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vsRUwPHr.ui'
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
        self.headerFrame.setGeometry(QRect(0, 0, 1201, 70))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.headerFrame.sizePolicy().hasHeightForWidth())
        self.headerFrame.setSizePolicy(sizePolicy1)
        self.headerFrame.setMinimumSize(QSize(0, 70))
        self.headerFrame.setMaximumSize(QSize(16777215, 70))
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

        self.headerProfileName = QTextEdit(self.headerFrame)
        self.headerProfileName.setObjectName(u"headerProfileName")
        self.headerProfileName.setGeometry(QRect(50, 10, 241, 31))
        font2 = QFont()
        font2.setFamily(u"Humanst521 BT")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.headerProfileName.setFont(font2)
        self.headerProfileName.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: white;\n"
"font-size: 12pt;\n"
"font-weight: bold;\n"
"height: 30px;")
        self.headerProfileIcon = QLabel(self.headerFrame)
        self.headerProfileIcon.setObjectName(u"headerProfileIcon")
        self.headerProfileIcon.setGeometry(QRect(10, 10, 31, 31))
        self.headerProfileIcon.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"image: url(:/icons/Media/icons/cil-user.png);")
        self.footerFrame = QFrame(self.centralwidget)
        self.footerFrame.setObjectName(u"footerFrame")
        self.footerFrame.setGeometry(QRect(0, 599, 1200, 50))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.footerFrame.sizePolicy().hasHeightForWidth())
        self.footerFrame.setSizePolicy(sizePolicy2)
        self.footerFrame.setMinimumSize(QSize(0, 50))
        self.footerFrame.setMaximumSize(QSize(16777215, 50))
        self.footerFrame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.506, x2:1, y2:0.517, stop:0 rgba(170, 0, 255, 255), stop:1 rgba(0, 170, 255, 255));")
        self.footerFrame.setFrameShape(QFrame.StyledPanel)
        self.footerFrame.setFrameShadow(QFrame.Raised)
        self.spotifyLabel = QLabel(self.footerFrame)
        self.spotifyLabel.setObjectName(u"spotifyLabel")
        self.spotifyLabel.setGeometry(QRect(550, 0, 121, 41))
        sizePolicy.setHeightForWidth(self.spotifyLabel.sizePolicy().hasHeightForWidth())
        self.spotifyLabel.setSizePolicy(sizePolicy)
        self.spotifyLabel.setStyleSheet(u"QLabel{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"\n"
"	image: url(:/images/Media/poweredby_2.png);\n"
"}")
        self.spotifyLabel.setScaledContents(True)
        self.bodyFrame = QFrame(self.centralwidget)
        self.bodyFrame.setObjectName(u"bodyFrame")
        self.bodyFrame.setGeometry(QRect(0, 0, 1200, 651))
        self.bodyFrame.setMinimumSize(QSize(1200, 651))
        self.bodyFrame.setSizeIncrement(QSize(1, 1))
        self.bodyFrame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.bodyFrame.setFrameShape(QFrame.StyledPanel)
        self.bodyFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.bodyFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stackedWidget = QStackedWidget(self.bodyFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 500))
        self.stackedWidget.setMaximumSize(QSize(16777215, 500))
        self.stackedWidget.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"\n"
"/*background-color: rgb(43, 43, 43);*/")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.buttonFrame = QFrame(self.homePage)
        self.buttonFrame.setObjectName(u"buttonFrame")
        self.buttonFrame.setGeometry(QRect(130, 110, 921, 170))
        sizePolicy.setHeightForWidth(self.buttonFrame.sizePolicy().hasHeightForWidth())
        self.buttonFrame.setSizePolicy(sizePolicy)
        self.buttonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.buttonFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.buttonFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
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

        self.horizontalLayout_3.addWidget(self.createButton)

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

        self.horizontalLayout_3.addWidget(self.profileButton)

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

        self.horizontalLayout_3.addWidget(self.settingsButton)

        self.frame = QFrame(self.homePage)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(180, 260, 811, 61))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.createLabel = QLabel(self.frame)
        self.createLabel.setObjectName(u"createLabel")
        font3 = QFont()
        font3.setFamily(u"Humnst777 BlkCn BT")
        font3.setPointSize(12)
        self.createLabel.setFont(font3)
        self.createLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.createLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.createLabel)

        self.profileLabel = QLabel(self.frame)
        self.profileLabel.setObjectName(u"profileLabel")
        self.profileLabel.setFont(font3)
        self.profileLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.profileLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.profileLabel)

        self.settingsLabel = QLabel(self.frame)
        self.settingsLabel.setObjectName(u"settingsLabel")
        self.settingsLabel.setFont(font3)
        self.settingsLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.settingsLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.settingsLabel)

        self.stackedWidget.addWidget(self.homePage)
        self.createPage = QWidget()
        self.createPage.setObjectName(u"createPage")
        self.homeButtonFrame = QFrame(self.createPage)
        self.homeButtonFrame.setObjectName(u"homeButtonFrame")
        self.homeButtonFrame.setGeometry(QRect(10, 0, 51, 51))
        self.homeButtonFrame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.homeButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.homeButtonFrame.setFrameShadow(QFrame.Raised)
        self.homeButton_create = QPushButton(self.homeButtonFrame)
        self.homeButton_create.setObjectName(u"homeButton_create")
        self.homeButton_create.setGeometry(QRect(10, 10, 31, 31))
        self.homeButton_create.setStyleSheet(u"QPushButton{\n"
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
        self.buttonFrame_2.setGeometry(QRect(130, 110, 921, 201))
        self.buttonFrame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.buttonFrame_2.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.buttonFrame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.createGenreButton = QPushButton(self.buttonFrame_2)
        self.createGenreButton.setObjectName(u"createGenreButton")
        self.createGenreButton.setMinimumSize(QSize(150, 150))
        self.createGenreButton.setMaximumSize(QSize(150, 150))
        self.createGenreButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.createGenreButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/createGenre.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/createGenre.png);\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	border-style: none;\n"
"	border-radius: 40px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.createGenreButton, 0, 1, 1, 1)

        self.createGenreLabel = QLabel(self.buttonFrame_2)
        self.createGenreLabel.setObjectName(u"createGenreLabel")
        self.createGenreLabel.setFont(font3)
        self.createGenreLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.createGenreLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.createGenreLabel, 2, 1, 1, 1)

        self.createArtistButton = QPushButton(self.buttonFrame_2)
        self.createArtistButton.setObjectName(u"createArtistButton")
        self.createArtistButton.setMinimumSize(QSize(150, 150))
        self.createArtistButton.setMaximumSize(QSize(150, 150))
        self.createArtistButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.createArtistButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/createArtist.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/createArtist.png);\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	border-style: none;\n"
"	border-radius: 40px;\n"
"}")

        self.gridLayout_2.addWidget(self.createArtistButton, 0, 0, 1, 1)

        self.createArtistLabel = QLabel(self.buttonFrame_2)
        self.createArtistLabel.setObjectName(u"createArtistLabel")
        self.createArtistLabel.setFont(font3)
        self.createArtistLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.createArtistLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.createArtistLabel, 2, 0, 1, 1)

        self.createMoodButton = QPushButton(self.buttonFrame_2)
        self.createMoodButton.setObjectName(u"createMoodButton")
        self.createMoodButton.setMinimumSize(QSize(150, 150))
        self.createMoodButton.setMaximumSize(QSize(150, 150))
        self.createMoodButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.createMoodButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/mood.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/mood.png);\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	border-style: none;\n"
"	border-radius: 40px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.createMoodButton, 0, 2, 1, 1)

        self.createMoodLabel = QLabel(self.buttonFrame_2)
        self.createMoodLabel.setObjectName(u"createMoodLabel")
        self.createMoodLabel.setFont(font3)
        self.createMoodLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.createMoodLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.createMoodLabel, 2, 2, 1, 1)

        self.stackedWidget.addWidget(self.createPage)
        self.createArtistPage = QWidget()
        self.createArtistPage.setObjectName(u"createArtistPage")
        self.buttonFrame_3 = QFrame(self.createArtistPage)
        self.buttonFrame_3.setObjectName(u"buttonFrame_3")
        self.buttonFrame_3.setGeometry(QRect(480, 10, 251, 131))
        self.buttonFrame_3.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.buttonFrame_3.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame_3.setFrameShadow(QFrame.Raised)
        self.basedOnArtistLabel2 = QLabel(self.buttonFrame_3)
        self.basedOnArtistLabel2.setObjectName(u"basedOnArtistLabel2")
        self.basedOnArtistLabel2.setGeometry(QRect(70, 80, 108, 20))
        self.basedOnArtistLabel2.setFont(font3)
        self.basedOnArtistLabel2.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.basedOnArtistLabel2.setAlignment(Qt.AlignCenter)
        self.basedOnArtistLabel = QLabel(self.buttonFrame_3)
        self.basedOnArtistLabel.setObjectName(u"basedOnArtistLabel")
        self.basedOnArtistLabel.setGeometry(QRect(10, 10, 221, 71))
        self.basedOnArtistLabel.setStyleSheet(u"image: url(:/icons/Media/icons/createArtist.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.keyLabel1 = QLabel(self.buttonFrame_3)
        self.keyLabel1.setObjectName(u"keyLabel1")
        self.keyLabel1.setGeometry(QRect(30, 110, 181, 21))
        font4 = QFont()
        font4.setFamily(u"Humnst777 BT")
        font4.setPointSize(12)
        self.keyLabel1.setFont(font4)
        self.keyLabel1.setStyleSheet(u"color: rgb(248, 231, 28);")
        self.artistTxtBoxes = QFrame(self.createArtistPage)
        self.artistTxtBoxes.setObjectName(u"artistTxtBoxes")
        self.artistTxtBoxes.setGeometry(QRect(430, 130, 351, 281))
        self.artistTxtBoxes.setFrameShape(QFrame.StyledPanel)
        self.artistTxtBoxes.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.artistTxtBoxes)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.artist1_txtbox = QLineEdit(self.artistTxtBoxes)
        self.artist1_txtbox.setObjectName(u"artist1_txtbox")
        self.artist1_txtbox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: white;\n"
"font-size: 12pt;\n"
"height: 30px;")

        self.verticalLayout.addWidget(self.artist1_txtbox)

        self.artist2_txtbox = QLineEdit(self.artistTxtBoxes)
        self.artist2_txtbox.setObjectName(u"artist2_txtbox")
        self.artist2_txtbox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: white;\n"
"font-size: 12pt;\n"
"height: 30px;")

        self.verticalLayout.addWidget(self.artist2_txtbox)

        self.artist3_txtbox = QLineEdit(self.artistTxtBoxes)
        self.artist3_txtbox.setObjectName(u"artist3_txtbox")
        self.artist3_txtbox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: white;\n"
"font-size: 12pt;\n"
"height: 30px;")

        self.verticalLayout.addWidget(self.artist3_txtbox)

        self.artist4_txtbox = QLineEdit(self.artistTxtBoxes)
        self.artist4_txtbox.setObjectName(u"artist4_txtbox")
        self.artist4_txtbox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: white;\n"
"font-size: 12pt;\n"
"height: 30px;")

        self.verticalLayout.addWidget(self.artist4_txtbox)

        self.artist5_txtbox = QLineEdit(self.artistTxtBoxes)
        self.artist5_txtbox.setObjectName(u"artist5_txtbox")
        self.artist5_txtbox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: white;\n"
"font-size: 12pt;\n"
"height: 30px;")

        self.verticalLayout.addWidget(self.artist5_txtbox)

        self.artist1Label = QLabel(self.createArtistPage)
        self.artist1Label.setObjectName(u"artist1Label")
        self.artist1Label.setGeometry(QRect(370, 150, 61, 41))
        font5 = QFont()
        font5.setFamily(u"Humnst777 Blk BT")
        font5.setPointSize(12)
        self.artist1Label.setFont(font5)
        self.artist1Label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.artist2Label = QLabel(self.createArtistPage)
        self.artist2Label.setObjectName(u"artist2Label")
        self.artist2Label.setGeometry(QRect(370, 200, 61, 41))
        self.artist2Label.setFont(font5)
        self.artist2Label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.artist3Label = QLabel(self.createArtistPage)
        self.artist3Label.setObjectName(u"artist3Label")
        self.artist3Label.setGeometry(QRect(370, 250, 61, 41))
        self.artist3Label.setFont(font5)
        self.artist3Label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.artist4Label = QLabel(self.createArtistPage)
        self.artist4Label.setObjectName(u"artist4Label")
        self.artist4Label.setGeometry(QRect(370, 300, 61, 41))
        self.artist4Label.setFont(font5)
        self.artist4Label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.artist5Label = QLabel(self.createArtistPage)
        self.artist5Label.setObjectName(u"artist5Label")
        self.artist5Label.setGeometry(QRect(370, 350, 61, 41))
        self.artist5Label.setFont(font5)
        self.artist5Label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.homeButtonFrame_2 = QFrame(self.createArtistPage)
        self.homeButtonFrame_2.setObjectName(u"homeButtonFrame_2")
        self.homeButtonFrame_2.setGeometry(QRect(10, 0, 51, 51))
        self.homeButtonFrame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.homeButtonFrame_2.setFrameShape(QFrame.StyledPanel)
        self.homeButtonFrame_2.setFrameShadow(QFrame.Raised)
        self.homeButton_boa = QPushButton(self.homeButtonFrame_2)
        self.homeButton_boa.setObjectName(u"homeButton_boa")
        self.homeButton_boa.setGeometry(QRect(10, 10, 31, 31))
        self.homeButton_boa.setStyleSheet(u"QPushButton{\n"
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
        self.genArtistButton = QPushButton(self.createArtistPage)
        self.genArtistButton.setObjectName(u"genArtistButton")
        self.genArtistButton.setGeometry(QRect(530, 420, 151, 31))
        font6 = QFont()
        font6.setFamily(u"Humnst777 BT")
        font6.setPointSize(10)
        self.genArtistButton.setFont(font6)
        self.genArtistButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(248, 231, 28);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
"}")
        self.stackedWidget.addWidget(self.createArtistPage)
        self.createArtistLoadingPage = QWidget()
        self.createArtistLoadingPage.setObjectName(u"createArtistLoadingPage")
        self.frame_2 = QFrame(self.createArtistLoadingPage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(370, 70, 441, 361))
        self.frame_2.setStyleSheet(u"image: url(:/images/Media/vpLocation_5.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.createArtistLoadingPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(460, 20, 251, 31))
        font7 = QFont()
        font7.setFamily(u"Humnst777 BT")
        font7.setPointSize(16)
        self.label.setFont(font7)
        self.label.setStyleSheet(u"color: rgb(248, 231, 28);")
        self.label_2 = QLabel(self.createArtistLoadingPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(400, 410, 381, 111))
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.homeButtonFrame_13 = QFrame(self.createArtistLoadingPage)
        self.homeButtonFrame_13.setObjectName(u"homeButtonFrame_13")
        self.homeButtonFrame_13.setGeometry(QRect(10, 0, 51, 51))
        self.homeButtonFrame_13.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.homeButtonFrame_13.setFrameShape(QFrame.StyledPanel)
        self.homeButtonFrame_13.setFrameShadow(QFrame.Raised)
        self.homeButton_calp = QPushButton(self.homeButtonFrame_13)
        self.homeButton_calp.setObjectName(u"homeButton_calp")
        self.homeButton_calp.setGeometry(QRect(10, 10, 31, 31))
        self.homeButton_calp.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/home_btn.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/home_btn.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: none;\n"
"	border-radius: 40px;\n"
"}")
        self.stackedWidget.addWidget(self.createArtistLoadingPage)
        self.createGenrePage = QWidget()
        self.createGenrePage.setObjectName(u"createGenrePage")
        self.genreLabel5 = QLabel(self.createGenrePage)
        self.genreLabel5.setObjectName(u"genreLabel5")
        self.genreLabel5.setGeometry(QRect(360, 350, 71, 41))
        self.genreLabel5.setFont(font5)
        self.genreLabel5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.genreLabel2 = QLabel(self.createGenrePage)
        self.genreLabel2.setObjectName(u"genreLabel2")
        self.genreLabel2.setGeometry(QRect(360, 200, 71, 41))
        self.genreLabel2.setFont(font5)
        self.genreLabel2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.buttonFrame_4 = QFrame(self.createGenrePage)
        self.buttonFrame_4.setObjectName(u"buttonFrame_4")
        self.buttonFrame_4.setGeometry(QRect(480, 10, 251, 131))
        self.buttonFrame_4.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.buttonFrame_4.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame_4.setFrameShadow(QFrame.Raised)
        self.basedOnGenreLabel2 = QLabel(self.buttonFrame_4)
        self.basedOnGenreLabel2.setObjectName(u"basedOnGenreLabel2")
        self.basedOnGenreLabel2.setGeometry(QRect(70, 80, 108, 20))
        self.basedOnGenreLabel2.setFont(font3)
        self.basedOnGenreLabel2.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.basedOnGenreLabel2.setAlignment(Qt.AlignCenter)
        self.basedOnGenreLabel = QLabel(self.buttonFrame_4)
        self.basedOnGenreLabel.setObjectName(u"basedOnGenreLabel")
        self.basedOnGenreLabel.setGeometry(QRect(10, 10, 221, 71))
        self.basedOnGenreLabel.setStyleSheet(u"image: url(:/icons/Media/icons/createGenre.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.keyLabel2 = QLabel(self.buttonFrame_4)
        self.keyLabel2.setObjectName(u"keyLabel2")
        self.keyLabel2.setGeometry(QRect(30, 110, 181, 21))
        self.keyLabel2.setFont(font4)
        self.keyLabel2.setStyleSheet(u"color: rgb(248, 231, 28);")
        self.genreLabel3 = QLabel(self.createGenrePage)
        self.genreLabel3.setObjectName(u"genreLabel3")
        self.genreLabel3.setGeometry(QRect(360, 250, 71, 41))
        self.genreLabel3.setFont(font5)
        self.genreLabel3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.genreLabel4 = QLabel(self.createGenrePage)
        self.genreLabel4.setObjectName(u"genreLabel4")
        self.genreLabel4.setGeometry(QRect(360, 300, 71, 41))
        self.genreLabel4.setFont(font5)
        self.genreLabel4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.genGenreButton = QPushButton(self.createGenrePage)
        self.genGenreButton.setObjectName(u"genGenreButton")
        self.genGenreButton.setGeometry(QRect(530, 420, 151, 31))
        self.genGenreButton.setFont(font6)
        self.genGenreButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 0.6);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"}")
        self.artistTxtBoxes_2 = QFrame(self.createGenrePage)
        self.artistTxtBoxes_2.setObjectName(u"artistTxtBoxes_2")
        self.artistTxtBoxes_2.setGeometry(QRect(430, 140, 351, 271))
        self.artistTxtBoxes_2.setFrameShape(QFrame.StyledPanel)
        self.artistTxtBoxes_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.artistTxtBoxes_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.genre1 = QTextEdit(self.artistTxtBoxes_2)
        self.genre1.setObjectName(u"genre1")
        self.genre1.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: white;\n"
"font-size: 12pt;")

        self.verticalLayout_2.addWidget(self.genre1)

        self.genre2 = QTextEdit(self.artistTxtBoxes_2)
        self.genre2.setObjectName(u"genre2")
        self.genre2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: white;\n"
"font-size: 12pt;")

        self.verticalLayout_2.addWidget(self.genre2)

        self.genre3 = QTextEdit(self.artistTxtBoxes_2)
        self.genre3.setObjectName(u"genre3")
        self.genre3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: white;\n"
"font-size: 12pt;")

        self.verticalLayout_2.addWidget(self.genre3)

        self.genre4 = QTextEdit(self.artistTxtBoxes_2)
        self.genre4.setObjectName(u"genre4")
        self.genre4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: white;\n"
"font-size: 12pt;")

        self.verticalLayout_2.addWidget(self.genre4)

        self.genre5 = QTextEdit(self.artistTxtBoxes_2)
        self.genre5.setObjectName(u"genre5")
        self.genre5.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: white;\n"
"font-size: 12pt;")

        self.verticalLayout_2.addWidget(self.genre5)

        self.genreLabel1 = QLabel(self.createGenrePage)
        self.genreLabel1.setObjectName(u"genreLabel1")
        self.genreLabel1.setGeometry(QRect(360, 150, 71, 41))
        self.genreLabel1.setFont(font5)
        self.genreLabel1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.homeButtonFrame_5 = QFrame(self.createGenrePage)
        self.homeButtonFrame_5.setObjectName(u"homeButtonFrame_5")
        self.homeButtonFrame_5.setGeometry(QRect(10, 0, 51, 51))
        self.homeButtonFrame_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.homeButtonFrame_5.setFrameShape(QFrame.StyledPanel)
        self.homeButtonFrame_5.setFrameShadow(QFrame.Raised)
        self.homeButton_bog = QPushButton(self.homeButtonFrame_5)
        self.homeButton_bog.setObjectName(u"homeButton_bog")
        self.homeButton_bog.setGeometry(QRect(10, 10, 31, 31))
        self.homeButton_bog.setStyleSheet(u"QPushButton{\n"
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
        self.stackedWidget.addWidget(self.createGenrePage)
        self.createMoodPage = QWidget()
        self.createMoodPage.setObjectName(u"createMoodPage")
        self.homeButtonFrame_6 = QFrame(self.createMoodPage)
        self.homeButtonFrame_6.setObjectName(u"homeButtonFrame_6")
        self.homeButtonFrame_6.setGeometry(QRect(10, 0, 51, 51))
        self.homeButtonFrame_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.homeButtonFrame_6.setFrameShape(QFrame.StyledPanel)
        self.homeButtonFrame_6.setFrameShadow(QFrame.Raised)
        self.homeButton_bom = QPushButton(self.homeButtonFrame_6)
        self.homeButton_bom.setObjectName(u"homeButton_bom")
        self.homeButton_bom.setGeometry(QRect(10, 10, 31, 31))
        self.homeButton_bom.setStyleSheet(u"QPushButton{\n"
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
        self.buttonFrame_5 = QFrame(self.createMoodPage)
        self.buttonFrame_5.setObjectName(u"buttonFrame_5")
        self.buttonFrame_5.setGeometry(QRect(480, 10, 251, 131))
        self.buttonFrame_5.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.buttonFrame_5.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame_5.setFrameShadow(QFrame.Raised)
        self.basedOnGenreLabel2_2 = QLabel(self.buttonFrame_5)
        self.basedOnGenreLabel2_2.setObjectName(u"basedOnGenreLabel2_2")
        self.basedOnGenreLabel2_2.setGeometry(QRect(70, 80, 108, 20))
        self.basedOnGenreLabel2_2.setFont(font3)
        self.basedOnGenreLabel2_2.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.basedOnGenreLabel2_2.setAlignment(Qt.AlignCenter)
        self.basedOnGenreLabel_2 = QLabel(self.buttonFrame_5)
        self.basedOnGenreLabel_2.setObjectName(u"basedOnGenreLabel_2")
        self.basedOnGenreLabel_2.setGeometry(QRect(10, 10, 221, 71))
        self.basedOnGenreLabel_2.setStyleSheet(u"image: url(:/icons/Media/icons/mood.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.keyLabel2_2 = QLabel(self.buttonFrame_5)
        self.keyLabel2_2.setObjectName(u"keyLabel2_2")
        self.keyLabel2_2.setGeometry(QRect(0, 110, 241, 21))
        self.keyLabel2_2.setFont(font4)
        self.keyLabel2_2.setStyleSheet(u"color: rgb(248, 231, 28);")
        self.genMoodButton = QPushButton(self.createMoodPage)
        self.genMoodButton.setObjectName(u"genMoodButton")
        self.genMoodButton.setGeometry(QRect(520, 420, 151, 31))
        self.genMoodButton.setFont(font6)
        self.genMoodButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 255, 255, 0.6);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"}")
        self.dial = QDial(self.createMoodPage)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(380, 130, 431, 291))
        self.stackedWidget.addWidget(self.createMoodPage)
        self.profilePage = QWidget()
        self.profilePage.setObjectName(u"profilePage")
        self.homeButtonFrame_3 = QFrame(self.profilePage)
        self.homeButtonFrame_3.setObjectName(u"homeButtonFrame_3")
        self.homeButtonFrame_3.setGeometry(QRect(10, 0, 51, 51))
        self.homeButtonFrame_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.homeButtonFrame_3.setFrameShape(QFrame.StyledPanel)
        self.homeButtonFrame_3.setFrameShadow(QFrame.Raised)
        self.homeButton_profile = QPushButton(self.homeButtonFrame_3)
        self.homeButton_profile.setObjectName(u"homeButton_profile")
        self.homeButton_profile.setGeometry(QRect(10, 10, 31, 31))
        self.homeButton_profile.setStyleSheet(u"QPushButton{\n"
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
        self.infoFrame = QFrame(self.profilePage)
        self.infoFrame.setObjectName(u"infoFrame")
        self.infoFrame.setGeometry(QRect(420, 260, 331, 141))
        self.infoFrame.setFrameShape(QFrame.StyledPanel)
        self.infoFrame.setFrameShadow(QFrame.Raised)
        self.nameLabel = QLabel(self.infoFrame)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(10, 10, 51, 41))
        font8 = QFont()
        font8.setFamily(u"Humanst521 BT")
        font8.setPointSize(14)
        self.nameLabel.setFont(font8)
        self.nameLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.subscriptLabel = QLabel(self.infoFrame)
        self.subscriptLabel.setObjectName(u"subscriptLabel")
        self.subscriptLabel.setGeometry(QRect(10, 70, 101, 41))
        self.subscriptLabel.setFont(font8)
        self.subscriptLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.name_txtbox = QTextEdit(self.infoFrame)
        self.name_txtbox.setObjectName(u"name_txtbox")
        self.name_txtbox.setGeometry(QRect(80, 20, 251, 31))
        self.name_txtbox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: white;\n"
"font-size: 12pt;\n"
"height: 30px;")
        self.sub_txtbox = QTextEdit(self.infoFrame)
        self.sub_txtbox.setObjectName(u"sub_txtbox")
        self.sub_txtbox.setGeometry(QRect(120, 80, 211, 31))
        self.sub_txtbox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: white;\n"
"font-size: 12pt;\n"
"height: 30px;")
        self.profilePicBox = QLabel(self.profilePage)
        self.profilePicBox.setObjectName(u"profilePicBox")
        self.profilePicBox.setGeometry(QRect(500, 80, 181, 171))
        self.profilePicBox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-style: none;\n"
"border-radius: 10px;")
        self.stackedWidget.addWidget(self.profilePage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.homeButtonFrame_4 = QFrame(self.settingsPage)
        self.homeButtonFrame_4.setObjectName(u"homeButtonFrame_4")
        self.homeButtonFrame_4.setGeometry(QRect(10, 0, 51, 51))
        self.homeButtonFrame_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.homeButtonFrame_4.setFrameShape(QFrame.StyledPanel)
        self.homeButtonFrame_4.setFrameShadow(QFrame.Raised)
        self.homeButton_settings = QPushButton(self.homeButtonFrame_4)
        self.homeButton_settings.setObjectName(u"homeButton_settings")
        self.homeButton_settings.setGeometry(QRect(10, 10, 31, 31))
        self.homeButton_settings.setStyleSheet(u"QPushButton{\n"
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
        self.buttonFrame_6 = QFrame(self.settingsPage)
        self.buttonFrame_6.setObjectName(u"buttonFrame_6")
        self.buttonFrame_6.setGeometry(QRect(130, 110, 921, 170))
        sizePolicy.setHeightForWidth(self.buttonFrame_6.sizePolicy().hasHeightForWidth())
        self.buttonFrame_6.setSizePolicy(sizePolicy)
        self.buttonFrame_6.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.buttonFrame_6.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.buttonFrame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.aboutButton = QPushButton(self.buttonFrame_6)
        self.aboutButton.setObjectName(u"aboutButton")
        self.aboutButton.setMinimumSize(QSize(150, 150))
        self.aboutButton.setMaximumSize(QSize(150, 150))
        self.aboutButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.aboutButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/about.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/about.png);\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	border-style: none;\n"
"	border-radius: 40px;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.aboutButton)

        self.darkModeButton = QPushButton(self.buttonFrame_6)
        self.darkModeButton.setObjectName(u"darkModeButton")
        self.darkModeButton.setMinimumSize(QSize(150, 150))
        self.darkModeButton.setMaximumSize(QSize(150, 150))
        self.darkModeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.darkModeButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/darkMode.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/darkMode.png);\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	border-style: none;\n"
"	border-radius: 40px;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.darkModeButton)

        self.frame_3 = QFrame(self.settingsPage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(230, 260, 721, 61))
        self.frame_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.aboutLabel = QLabel(self.frame_3)
        self.aboutLabel.setObjectName(u"aboutLabel")
        self.aboutLabel.setFont(font3)
        self.aboutLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.aboutLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.aboutLabel)

        self.darkModeLabel = QLabel(self.frame_3)
        self.darkModeLabel.setObjectName(u"darkModeLabel")
        self.darkModeLabel.setFont(font3)
        self.darkModeLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.darkModeLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.darkModeLabel)

        self.stackedWidget.addWidget(self.settingsPage)
        self.aboutPage = QWidget()
        self.aboutPage.setObjectName(u"aboutPage")
        self.homeButtonFrame_7 = QFrame(self.aboutPage)
        self.homeButtonFrame_7.setObjectName(u"homeButtonFrame_7")
        self.homeButtonFrame_7.setGeometry(QRect(10, 0, 51, 51))
        self.homeButtonFrame_7.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.homeButtonFrame_7.setFrameShape(QFrame.StyledPanel)
        self.homeButtonFrame_7.setFrameShadow(QFrame.Raised)
        self.homeButton_about = QPushButton(self.homeButtonFrame_7)
        self.homeButton_about.setObjectName(u"homeButton_about")
        self.homeButton_about.setGeometry(QRect(10, 10, 31, 31))
        self.homeButton_about.setStyleSheet(u"QPushButton{\n"
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
        self.frame_4 = QFrame(self.aboutPage)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(440, 80, 311, 321))
        self.frame_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-style: none;\n"
"border-radius: 10px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 50, 141, 31))
        self.label_3.setFont(font8)
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 80, 181, 31))
        self.label_4.setFont(font8)
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 60, 91, 21))
        font9 = QFont()
        font9.setFamily(u"Humanst521 BT")
        font9.setPointSize(12)
        self.label_5.setFont(font9)
        self.label_5.setStyleSheet(u"color: white;\n"
"background-color: rgb(74, 74, 74);")
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(200, 90, 91, 21))
        self.label_6.setFont(font9)
        self.label_6.setStyleSheet(u"color: white;\n"
"background-color: rgb(74, 74, 74);")
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 120, 221, 21))
        self.label_7.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"font-weight: bold;")
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 140, 201, 21))
        self.label_8.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 160, 121, 21))
        self.label_9.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 10, 211, 41))
        self.label_10.setStyleSheet(u"image: url(:/images/Media/VS_2tone.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 180, 271, 16))
        self.label_11.setStyleSheet(u"border-bottom: 5px dotted black;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 210, 271, 16))
        self.label_12.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 230, 271, 16))
        self.label_13.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 250, 271, 16))
        self.label_14.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_15 = QLabel(self.frame_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 270, 271, 16))
        self.label_15.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_16 = QLabel(self.frame_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(30, 290, 271, 16))
        self.label_16.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"font-style: italic;")
        self.stackedWidget.addWidget(self.aboutPage)

        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 1, 1)

        VSMain.setCentralWidget(self.centralwidget)
        self.bodyFrame.raise_()
        self.headerFrame.raise_()
        self.footerFrame.raise_()

        self.retranslateUi(VSMain)

        self.stackedWidget.setCurrentIndex(8)


        QMetaObject.connectSlotsByName(VSMain)
    # setupUi

    def retranslateUi(self, VSMain):
        VSMain.setWindowTitle(QCoreApplication.translate("VSMain", u"VibeShare: Playlist Generator", None))
        self.vsLogo.setText("")
        self.descLabel.setText(QCoreApplication.translate("VSMain", u"Finding New Music Made Easy", None))
        self.minimizeButton.setText("")
        self.restoreButton.setText("")
        self.closeButton.setText("")
        self.headerProfileName.setHtml(QCoreApplication.translate("VSMain", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Humanst521 BT'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.headerProfileIcon.setText("")
        self.spotifyLabel.setText("")
        self.createButton.setText("")
        self.profileButton.setText("")
        self.settingsButton.setText("")
        self.createLabel.setText(QCoreApplication.translate("VSMain", u"Create+", None))
        self.profileLabel.setText(QCoreApplication.translate("VSMain", u"Profile", None))
        self.settingsLabel.setText(QCoreApplication.translate("VSMain", u"Settings", None))
        self.homeButton_create.setText("")
        self.createGenreButton.setText("")
        self.createGenreLabel.setText(QCoreApplication.translate("VSMain", u"Based on Genre", None))
        self.createArtistButton.setText("")
        self.createArtistLabel.setText(QCoreApplication.translate("VSMain", u"Based On Artist", None))
        self.createMoodButton.setText("")
        self.createMoodLabel.setText(QCoreApplication.translate("VSMain", u"Based on Mood", None))
        self.basedOnArtistLabel2.setText(QCoreApplication.translate("VSMain", u"Based On Artist", None))
        self.basedOnArtistLabel.setText("")
        self.keyLabel1.setText(QCoreApplication.translate("VSMain", u"*Input at least one artist", None))
        self.artist1Label.setText(QCoreApplication.translate("VSMain", u"Artist 1", None))
        self.artist2Label.setText(QCoreApplication.translate("VSMain", u"Artist 2", None))
        self.artist3Label.setText(QCoreApplication.translate("VSMain", u"Artist 3", None))
        self.artist4Label.setText(QCoreApplication.translate("VSMain", u"Artist 4", None))
        self.artist5Label.setText(QCoreApplication.translate("VSMain", u"Artist 5", None))
        self.homeButton_boa.setText("")
        self.genArtistButton.setText(QCoreApplication.translate("VSMain", u"Generate", None))
        self.label.setText(QCoreApplication.translate("VSMain", u"Your new playlist is ready!", None))
        self.label_2.setText(QCoreApplication.translate("VSMain", u"Look for the \"VibeShare Playlist\" on your Spotify app", None))
        self.homeButton_calp.setText("")
        self.genreLabel5.setText(QCoreApplication.translate("VSMain", u"Genre 5", None))
        self.genreLabel2.setText(QCoreApplication.translate("VSMain", u"Genre 2", None))
        self.basedOnGenreLabel2.setText(QCoreApplication.translate("VSMain", u"Based On Genre", None))
        self.basedOnGenreLabel.setText("")
        self.keyLabel2.setText(QCoreApplication.translate("VSMain", u"*Input at least one genre", None))
        self.genreLabel3.setText(QCoreApplication.translate("VSMain", u"Genre 3", None))
        self.genreLabel4.setText(QCoreApplication.translate("VSMain", u"Genre 4", None))
        self.genGenreButton.setText(QCoreApplication.translate("VSMain", u"Generate", None))
        self.genreLabel1.setText(QCoreApplication.translate("VSMain", u"Genre 1", None))
        self.homeButton_bog.setText("")
        self.homeButton_bom.setText("")
        self.basedOnGenreLabel2_2.setText(QCoreApplication.translate("VSMain", u"Based On Mood", None))
        self.basedOnGenreLabel_2.setText("")
        self.keyLabel2_2.setText(QCoreApplication.translate("VSMain", u"*Select a mood to generate from", None))
        self.genMoodButton.setText(QCoreApplication.translate("VSMain", u"Generate", None))
        self.homeButton_profile.setText("")
        self.nameLabel.setText(QCoreApplication.translate("VSMain", u"Name: ", None))
        self.subscriptLabel.setText(QCoreApplication.translate("VSMain", u"Spotify ID:", None))
        self.profilePicBox.setText("")
        self.homeButton_settings.setText("")
        self.aboutButton.setText("")
        self.darkModeButton.setText("")
        self.aboutLabel.setText(QCoreApplication.translate("VSMain", u"About", None))
        self.darkModeLabel.setText(QCoreApplication.translate("VSMain", u"Dark Mode On/ Off", None))
        self.homeButton_about.setText("")
        self.label_3.setText(QCoreApplication.translate("VSMain", u"Software Version: ", None))
        self.label_4.setText(QCoreApplication.translate("VSMain", u"Software Release Date:", None))
        self.label_5.setText(QCoreApplication.translate("VSMain", u"  v1.0_04_16", None))
        self.label_6.setText(QCoreApplication.translate("VSMain", u"  04/16/2021", None))
        self.label_7.setText(QCoreApplication.translate("VSMain", u"Created by Team Big Pecs:", None))
        self.label_8.setText(QCoreApplication.translate("VSMain", u"Zach Johnson, Azal Abduh, Gameil Alsaidi,", None))
        self.label_9.setText(QCoreApplication.translate("VSMain", u"Tin Pham, & Kalia Jeffries", None))
        self.label_10.setText("")
        self.label_11.setText("")
        self.label_12.setText(QCoreApplication.translate("VSMain", u"VibeShare is a standalone application created to make", None))
        self.label_13.setText(QCoreApplication.translate("VSMain", u"playlist generation easier and more appealing to Spotify", None))
        self.label_14.setText(QCoreApplication.translate("VSMain", u"users. Users have the ability to generate unique", None))
        self.label_15.setText(QCoreApplication.translate("VSMain", u"playlists based on specified Artists, Genres, and Moods!", None))
        self.label_16.setText(QCoreApplication.translate("VSMain", u"(Functionality made possible through Spotify API)", None))
    # retranslateUi
