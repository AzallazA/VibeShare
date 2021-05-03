# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vsZMOrPp.ui'
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
        self.vsLogo.setGeometry(QRect(460, 0, 241, 51))
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
        self.descLabel.setGeometry(QRect(540, 40, 191, 31))
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
"    border: none;\n"
"    outline: none;\n"
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
"    border: none;\n"
"    outline: none;\n"
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
"    border: none;\n"
"    outline: none;\n"
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
        self.headerProfileName.setGeometry(QRect(50, 10, 241, 21))
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
        self.headerProfileIcon.setGeometry(QRect(20, 10, 31, 31))
        self.headerProfileIcon.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"image: url(:/icons/Media/icons/cil-user.png);")
        self.headerSignoutButton = QPushButton(self.headerFrame)
        self.headerSignoutButton.setObjectName(u"headerSignoutButton")
        self.headerSignoutButton.setGeometry(QRect(50, 30, 51, 20))
        self.headerSignoutButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	text-decoration: underline;\n"
"	font-style: italic;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(248, 231, 28);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	text-decoration: underline;\n"
"	font-style: italic;\n"
"	font-weight: bold;\n"
"}")
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
        self.spotifyLabel.setGeometry(QRect(-10, 0, 1211, 41))
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
        font3 = QFont()
        font3.setFamily(u"Montserrat Medium")
        self.stackedWidget.setFont(font3)
        self.stackedWidget.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"\n"
"/*background-color: rgb(43, 43, 43);*/")
        self.loadingPage = QWidget()
        self.loadingPage.setObjectName(u"loadingPage")
        self.stackedWidget.addWidget(self.loadingPage)
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
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/create.png);\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	 border: none;\n"
"    outline: none;\n"
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
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/profile.png);\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	border-style: none;\n"
"    border: none;\n"
"    outline: none;\n"
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
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/settings.png);\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	border-style: none;\n"
"    border: none;\n"
"    outline: none;\n"
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
        font4 = QFont()
        font4.setFamily(u"Humnst777 BlkCn BT")
        font4.setPointSize(12)
        self.createLabel.setFont(font4)
        self.createLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.createLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.createLabel)

        self.profileLabel = QLabel(self.frame)
        self.profileLabel.setObjectName(u"profileLabel")
        self.profileLabel.setFont(font4)
        self.profileLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.profileLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.profileLabel)

        self.settingsLabel = QLabel(self.frame)
        self.settingsLabel.setObjectName(u"settingsLabel")
        self.settingsLabel.setFont(font4)
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
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/goback.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: none;\n"
"    border: none;\n"
"    outline: none;\n"
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
        self.createMoodButton = QPushButton(self.buttonFrame_2)
        self.createMoodButton.setObjectName(u"createMoodButton")
        self.createMoodButton.setMinimumSize(QSize(150, 150))
        self.createMoodButton.setMaximumSize(QSize(150, 150))
        self.createMoodButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.createMoodButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/mood.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/mood.png);\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	border-style: none;\n"
"    border: none;\n"
"    outline: none;\n"
"	border-radius: 40px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.createMoodButton, 0, 2, 1, 1)

        self.createGenreButton = QPushButton(self.buttonFrame_2)
        self.createGenreButton.setObjectName(u"createGenreButton")
        self.createGenreButton.setMinimumSize(QSize(150, 150))
        self.createGenreButton.setMaximumSize(QSize(150, 150))
        self.createGenreButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.createGenreButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/createGenre.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/createGenre.png);\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	border-style: none;\n"
"    border: none;\n"
"    outline: none;\n"
"	border-radius: 40px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.createGenreButton, 0, 1, 1, 1)

        self.createArtistButton = QPushButton(self.buttonFrame_2)
        self.createArtistButton.setObjectName(u"createArtistButton")
        self.createArtistButton.setMinimumSize(QSize(150, 150))
        self.createArtistButton.setMaximumSize(QSize(150, 150))
        self.createArtistButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.createArtistButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/createArtist.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/createArtist.png);\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	border-style: none;\n"
"    border: none;\n"
"    outline: none;\n"
"	border-radius: 40px;\n"
"}")

        self.gridLayout_2.addWidget(self.createArtistButton, 0, 0, 1, 1)

        self.createArtistLabel = QLabel(self.buttonFrame_2)
        self.createArtistLabel.setObjectName(u"createArtistLabel")
        self.createArtistLabel.setFont(font4)
        self.createArtistLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.createArtistLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.createArtistLabel, 2, 0, 1, 1)

        self.createMoodLabel = QLabel(self.buttonFrame_2)
        self.createMoodLabel.setObjectName(u"createMoodLabel")
        self.createMoodLabel.setFont(font4)
        self.createMoodLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.createMoodLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.createMoodLabel, 2, 2, 1, 1)

        self.createGenreLabel = QLabel(self.buttonFrame_2)
        self.createGenreLabel.setObjectName(u"createGenreLabel")
        self.createGenreLabel.setFont(font4)
        self.createGenreLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.createGenreLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.createGenreLabel, 2, 1, 1, 1)

        self.recommendButton = QPushButton(self.buttonFrame_2)
        self.recommendButton.setObjectName(u"recommendButton")
        self.recommendButton.setMinimumSize(QSize(150, 150))
        self.recommendButton.setMaximumSize(QSize(150, 150))
        self.recommendButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.recommendButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/recommend.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/recommend.png);\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	border-style: none;\n"
"	border-radius: 40px;\n"
"}")

        self.gridLayout_2.addWidget(self.recommendButton, 0, 3, 1, 1)

        self.recommendLabel = QLabel(self.buttonFrame_2)
        self.recommendLabel.setObjectName(u"recommendLabel")
        self.recommendLabel.setFont(font4)
        self.recommendLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.recommendLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.recommendLabel, 2, 3, 1, 1)

        self.stackedWidget.addWidget(self.createPage)
        self.createArtistPage = QWidget()
        self.createArtistPage.setObjectName(u"createArtistPage")
        self.buttonFrame_3 = QFrame(self.createArtistPage)
        self.buttonFrame_3.setObjectName(u"buttonFrame_3")
        self.buttonFrame_3.setGeometry(QRect(460, 10, 221, 81))
        self.buttonFrame_3.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.buttonFrame_3.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame_3.setFrameShadow(QFrame.Raised)
        self.basedOnArtistLabel2 = QLabel(self.buttonFrame_3)
        self.basedOnArtistLabel2.setObjectName(u"basedOnArtistLabel2")
        self.basedOnArtistLabel2.setGeometry(QRect(60, 50, 108, 20))
        self.basedOnArtistLabel2.setFont(font4)
        self.basedOnArtistLabel2.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.basedOnArtistLabel2.setAlignment(Qt.AlignCenter)
        self.basedOnArtistLabel = QLabel(self.buttonFrame_3)
        self.basedOnArtistLabel.setObjectName(u"basedOnArtistLabel")
        self.basedOnArtistLabel.setGeometry(QRect(20, 0, 191, 51))
        self.basedOnArtistLabel.setStyleSheet(u"image: url(:/icons/Media/icons/createArtist.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.artistTxtBoxes = QFrame(self.createArtistPage)
        self.artistTxtBoxes.setObjectName(u"artistTxtBoxes")
        self.artistTxtBoxes.setGeometry(QRect(430, 140, 311, 281))
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

        self.artist1_txtbox.raise_()
        self.artist3_txtbox.raise_()
        self.artist2_txtbox.raise_()
        self.artist4_txtbox.raise_()
        self.artist5_txtbox.raise_()
        self.artist1Label = QLabel(self.createArtistPage)
        self.artist1Label.setObjectName(u"artist1Label")
        self.artist1Label.setGeometry(QRect(370, 160, 61, 41))
        font5 = QFont()
        font5.setFamily(u"Humnst777 Blk BT")
        font5.setPointSize(12)
        self.artist1Label.setFont(font5)
        self.artist1Label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.artist2Label = QLabel(self.createArtistPage)
        self.artist2Label.setObjectName(u"artist2Label")
        self.artist2Label.setGeometry(QRect(370, 210, 61, 41))
        self.artist2Label.setFont(font5)
        self.artist2Label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.artist3Label = QLabel(self.createArtistPage)
        self.artist3Label.setObjectName(u"artist3Label")
        self.artist3Label.setGeometry(QRect(370, 260, 61, 41))
        self.artist3Label.setFont(font5)
        self.artist3Label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.artist4Label = QLabel(self.createArtistPage)
        self.artist4Label.setObjectName(u"artist4Label")
        self.artist4Label.setGeometry(QRect(370, 310, 61, 41))
        self.artist4Label.setFont(font5)
        self.artist4Label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.artist5Label = QLabel(self.createArtistPage)
        self.artist5Label.setObjectName(u"artist5Label")
        self.artist5Label.setGeometry(QRect(370, 360, 61, 41))
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
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/goback.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: none;\n"
"    border: none;\n"
"    outline: none;\n"
"	border-radius: 40px;\n"
"}")
        self.genArtistButton = QPushButton(self.createArtistPage)
        self.genArtistButton.setObjectName(u"genArtistButton")
        self.genArtistButton.setGeometry(QRect(510, 410, 151, 31))
        font6 = QFont()
        font6.setFamily(u"Humnst777 BT")
        font6.setPointSize(10)
        self.genArtistButton.setFont(font6)
        self.genArtistButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(248, 231, 28);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"    border: none;\n"
"    outline: none;\n"
"	font-weight: bold;\n"
"}")
        self.label_30 = QLabel(self.createArtistPage)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(480, 450, 211, 21))
        font7 = QFont()
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_30.setFont(font7)
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_30.setAlignment(Qt.AlignCenter)
        self.frame_10 = QFrame(self.createArtistPage)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(210, 90, 761, 51))
        self.frame_10.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.7);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-top-radius\n"
"border-style: none;\n"
"color: white;\n"
"font-size: 12pt;\n"
"height: 30px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_43 = QLabel(self.createArtistPage)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(270, 90, 181, 51))
        font8 = QFont()
        font8.setFamily(u"Humnst777 BlkCn BT")
        font8.setPointSize(16)
        font8.setBold(False)
        font8.setItalic(False)
        font8.setUnderline(False)
        font8.setWeight(50)
        self.label_43.setFont(font8)
        self.label_43.setStyleSheet(u"color: rgb(74, 144, 226);")
        self.label_43.setAlignment(Qt.AlignCenter)
        self.label_44 = QLabel(self.createArtistPage)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(210, 90, 761, 401))
        self.label_44.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.2);\n"
"border-style: none;\n"
"border-radius: 10px;")
        self.artistPlaylistName = QLineEdit(self.createArtistPage)
        self.artistPlaylistName.setObjectName(u"artistPlaylistName")
        self.artistPlaylistName.setGeometry(QRect(460, 100, 441, 31))
        self.artistPlaylistName.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: rgb(144, 19, 254);\n"
"font-size: 12pt;\n"
"height: 30px;")
        self.stackedWidget.addWidget(self.createArtistPage)
        self.label_44.raise_()
        self.buttonFrame_3.raise_()
        self.artistTxtBoxes.raise_()
        self.artist1Label.raise_()
        self.artist2Label.raise_()
        self.artist3Label.raise_()
        self.artist4Label.raise_()
        self.artist5Label.raise_()
        self.homeButtonFrame_2.raise_()
        self.genArtistButton.raise_()
        self.label_30.raise_()
        self.frame_10.raise_()
        self.label_43.raise_()
        self.artistPlaylistName.raise_()
        self.createArtistLoadingPage = QWidget()
        self.createArtistLoadingPage.setObjectName(u"createArtistLoadingPage")
        self.frame_2 = QFrame(self.createArtistLoadingPage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(200, 90, 331, 271))
        self.frame_2.setStyleSheet(u"image: url(:/images/Media/vpArtist_location.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.createArtistLoadingPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(460, 10, 251, 31))
        font9 = QFont()
        font9.setFamily(u"Humnst777 BT")
        font9.setPointSize(16)
        self.label.setFont(font9)
        self.label.setStyleSheet(u"color: rgb(248, 231, 28);")
        self.label_2 = QLabel(self.createArtistLoadingPage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(540, 120, 381, 31))
        font10 = QFont()
        font10.setFamily(u"Humnst777 BT")
        font10.setPointSize(12)
        self.label_2.setFont(font10)
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
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/home_btn.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: none;\n"
"    border: none;\n"
"    outline: none;\n"
"	border-radius: 40px;\n"
"}")
        self.artistLinkTxtbox = QTextEdit(self.createArtistLoadingPage)
        self.artistLinkTxtbox.setObjectName(u"artistLinkTxtbox")
        self.artistLinkTxtbox.setGeometry(QRect(540, 240, 391, 81))
        self.artistLinkTxtbox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: black;\n"
"font-size: 12pt;\n"
"height: 30px;")
        self.label_20 = QLabel(self.createArtistLoadingPage)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(540, 210, 101, 21))
        self.label_20.setFont(font6)
        self.label_20.setStyleSheet(u"color: white;")
        self.label_21 = QLabel(self.createArtistLoadingPage)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(210, 60, 751, 331))
        self.label_21.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.2);\n"
"border-style: none;\n"
"border-radius: 10px;")
        self.label_29 = QLabel(self.createArtistLoadingPage)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(540, 140, 391, 31))
        self.label_29.setFont(font10)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_47 = QLabel(self.createArtistLoadingPage)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(540, 160, 371, 31))
        self.label_47.setFont(font10)
        self.label_47.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.createArtistLoadingPage)
        self.label_21.raise_()
        self.frame_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.homeButtonFrame_13.raise_()
        self.artistLinkTxtbox.raise_()
        self.label_20.raise_()
        self.label_29.raise_()
        self.label_47.raise_()
        self.recommendLoadingPage = QWidget()
        self.recommendLoadingPage.setObjectName(u"recommendLoadingPage")
        self.homeButtonFrame_14 = QFrame(self.recommendLoadingPage)
        self.homeButtonFrame_14.setObjectName(u"homeButtonFrame_14")
        self.homeButtonFrame_14.setGeometry(QRect(10, 0, 51, 51))
        self.homeButtonFrame_14.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.homeButtonFrame_14.setFrameShape(QFrame.StyledPanel)
        self.homeButtonFrame_14.setFrameShadow(QFrame.Raised)
        self.homeButton_rlp = QPushButton(self.homeButtonFrame_14)
        self.homeButton_rlp.setObjectName(u"homeButton_rlp")
        self.homeButton_rlp.setGeometry(QRect(10, 10, 31, 31))
        self.homeButton_rlp.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/home_btn.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/home_btn.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: none;\n"
"    border: none;\n"
"    outline: none;\n"
"	border-radius: 40px;\n"
"}")
        self.label_17 = QLabel(self.recommendLoadingPage)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(460, 10, 251, 31))
        self.label_17.setFont(font9)
        self.label_17.setStyleSheet(u"color: rgb(248, 231, 28);")
        self.label_19 = QLabel(self.recommendLoadingPage)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(540, 120, 381, 31))
        self.label_19.setFont(font10)
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_5 = QFrame(self.recommendLoadingPage)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(200, 90, 331, 271))
        self.frame_5.setStyleSheet(u"image: url(:/images/Media/vpRecommendations_location.png);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_22 = QLabel(self.recommendLoadingPage)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(540, 210, 101, 21))
        self.label_22.setFont(font6)
        self.label_22.setStyleSheet(u"color: white;")
        self.label_23 = QLabel(self.recommendLoadingPage)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(210, 60, 751, 331))
        self.label_23.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.2);\n"
"border-style: none;\n"
"border-radius: 10px;")
        self.recommendtLinkTxtbox = QTextEdit(self.recommendLoadingPage)
        self.recommendtLinkTxtbox.setObjectName(u"recommendtLinkTxtbox")
        self.recommendtLinkTxtbox.setGeometry(QRect(540, 240, 391, 81))
        self.recommendtLinkTxtbox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: black;\n"
"font-size: 12pt;\n"
"height: 30px;")
        self.label_24 = QLabel(self.recommendLoadingPage)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(540, 140, 381, 31))
        self.label_24.setFont(font10)
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.recommendLoadingPage)
        self.label_23.raise_()
        self.homeButtonFrame_14.raise_()
        self.label_17.raise_()
        self.label_19.raise_()
        self.frame_5.raise_()
        self.label_22.raise_()
        self.recommendtLinkTxtbox.raise_()
        self.label_24.raise_()
        self.genreLoadingPage = QWidget()
        self.genreLoadingPage.setObjectName(u"genreLoadingPage")
        self.genreLinkTxtbox = QTextEdit(self.genreLoadingPage)
        self.genreLinkTxtbox.setObjectName(u"genreLinkTxtbox")
        self.genreLinkTxtbox.setGeometry(QRect(540, 240, 391, 81))
        self.genreLinkTxtbox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: black;\n"
"font-size: 12pt;\n"
"height: 30px;")
        self.homeButtonFrame_15 = QFrame(self.genreLoadingPage)
        self.homeButtonFrame_15.setObjectName(u"homeButtonFrame_15")
        self.homeButtonFrame_15.setGeometry(QRect(10, 0, 51, 51))
        self.homeButtonFrame_15.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.homeButtonFrame_15.setFrameShape(QFrame.StyledPanel)
        self.homeButtonFrame_15.setFrameShadow(QFrame.Raised)
        self.homeButton_glp = QPushButton(self.homeButtonFrame_15)
        self.homeButton_glp.setObjectName(u"homeButton_glp")
        self.homeButton_glp.setGeometry(QRect(10, 10, 31, 31))
        self.homeButton_glp.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/home_btn.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/home_btn.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: none;\n"
"    border: none;\n"
"    outline: none;\n"
"	border-radius: 40px;\n"
"}")
        self.label_26 = QLabel(self.genreLoadingPage)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(540, 210, 101, 21))
        self.label_26.setFont(font6)
        self.label_26.setStyleSheet(u"color: white;")
        self.label_25 = QLabel(self.genreLoadingPage)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(540, 120, 401, 31))
        self.label_25.setFont(font10)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_6 = QFrame(self.genreLoadingPage)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(200, 90, 331, 271))
        self.frame_6.setStyleSheet(u"image: url(:/images/Media/vpGenre_location.png);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_18 = QLabel(self.genreLoadingPage)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(460, 10, 251, 31))
        self.label_18.setFont(font9)
        self.label_18.setStyleSheet(u"color: rgb(248, 231, 28);")
        self.label_27 = QLabel(self.genreLoadingPage)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(210, 60, 751, 331))
        self.label_27.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.2);\n"
"border-style: none;\n"
"border-radius: 10px;")
        self.label_28 = QLabel(self.genreLoadingPage)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(540, 140, 391, 31))
        self.label_28.setFont(font10)
        self.label_28.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_45 = QLabel(self.genreLoadingPage)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(540, 160, 371, 31))
        self.label_45.setFont(font10)
        self.label_45.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.genreLoadingPage)
        self.label_27.raise_()
        self.genreLinkTxtbox.raise_()
        self.homeButtonFrame_15.raise_()
        self.label_26.raise_()
        self.label_25.raise_()
        self.frame_6.raise_()
        self.label_18.raise_()
        self.label_28.raise_()
        self.label_45.raise_()
        self.createGenrePage = QWidget()
        self.createGenrePage.setObjectName(u"createGenrePage")
        self.buttonFrame_4 = QFrame(self.createGenrePage)
        self.buttonFrame_4.setObjectName(u"buttonFrame_4")
        self.buttonFrame_4.setGeometry(QRect(460, 0, 251, 101))
        self.buttonFrame_4.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.buttonFrame_4.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame_4.setFrameShadow(QFrame.Raised)
        self.basedOnGenreLabel2 = QLabel(self.buttonFrame_4)
        self.basedOnGenreLabel2.setObjectName(u"basedOnGenreLabel2")
        self.basedOnGenreLabel2.setGeometry(QRect(70, 60, 108, 20))
        self.basedOnGenreLabel2.setFont(font4)
        self.basedOnGenreLabel2.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.basedOnGenreLabel2.setAlignment(Qt.AlignCenter)
        self.basedOnGenreLabel = QLabel(self.buttonFrame_4)
        self.basedOnGenreLabel.setObjectName(u"basedOnGenreLabel")
        self.basedOnGenreLabel.setGeometry(QRect(30, 10, 191, 51))
        self.basedOnGenreLabel.setStyleSheet(u"image: url(:/icons/Media/icons/createGenre.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.genGenreButton = QPushButton(self.createGenrePage)
        self.genGenreButton.setObjectName(u"genGenreButton")
        self.genGenreButton.setGeometry(QRect(510, 250, 151, 31))
        self.genGenreButton.setFont(font6)
        self.genGenreButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(248, 231, 28);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"    border: none;\n"
"    outline: none;\n"
"	font-weight: bold;\n"
"}")
        self.artistTxtBoxes_2 = QFrame(self.createGenrePage)
        self.artistTxtBoxes_2.setObjectName(u"artistTxtBoxes_2")
        self.artistTxtBoxes_2.setGeometry(QRect(410, 170, 351, 51))
        self.artistTxtBoxes_2.setFrameShape(QFrame.StyledPanel)
        self.artistTxtBoxes_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.artistTxtBoxes_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.genre_txtbox = QLineEdit(self.artistTxtBoxes_2)
        self.genre_txtbox.setObjectName(u"genre_txtbox")
        self.genre_txtbox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: white;\n"
"font-size: 12pt;\n"
"height: 30px;")

        self.verticalLayout_2.addWidget(self.genre_txtbox)

        self.genreLabel = QLabel(self.createGenrePage)
        self.genreLabel.setObjectName(u"genreLabel")
        self.genreLabel.setGeometry(QRect(360, 170, 51, 41))
        self.genreLabel.setFont(font5)
        self.genreLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
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
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/goback.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: none;\n"
"    border: none;\n"
"    outline: none;\n"
"	border-radius: 40px;\n"
"}")
        self.label_31 = QLabel(self.createGenrePage)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(480, 290, 211, 21))
        self.label_31.setFont(font7)
        self.label_31.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_31.setAlignment(Qt.AlignCenter)
        self.frame_9 = QFrame(self.createGenrePage)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(200, 90, 771, 51))
        self.frame_9.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.7);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-top-radius\n"
"border-style: none;\n"
"color: white;\n"
"font-size: 12pt;\n"
"height: 30px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_41 = QLabel(self.createGenrePage)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(270, 90, 181, 51))
        font11 = QFont()
        font11.setFamily(u"Humnst777 BlkCn BT")
        font11.setPointSize(16)
        self.label_41.setFont(font11)
        self.label_41.setStyleSheet(u"color: rgb(74, 144, 226);")
        self.label_41.setAlignment(Qt.AlignCenter)
        self.label_42 = QLabel(self.createGenrePage)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(200, 90, 771, 261))
        self.label_42.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.2);\n"
"border-style: none;\n"
"border-radius: 10px;")
        self.genrePlaylistName = QLineEdit(self.createGenrePage)
        self.genrePlaylistName.setObjectName(u"genrePlaylistName")
        self.genrePlaylistName.setGeometry(QRect(460, 100, 441, 31))
        self.genrePlaylistName.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: rgb(144, 19, 254);\n"
"font-size: 12pt;\n"
"height: 30px;")
        self.stackedWidget.addWidget(self.createGenrePage)
        self.label_42.raise_()
        self.buttonFrame_4.raise_()
        self.genGenreButton.raise_()
        self.artistTxtBoxes_2.raise_()
        self.genreLabel.raise_()
        self.homeButtonFrame_5.raise_()
        self.label_31.raise_()
        self.frame_9.raise_()
        self.genrePlaylistName.raise_()
        self.label_41.raise_()
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
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/goback.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: none;\n"
"    border: none;\n"
"    outline: none;\n"
"	border-radius: 40px;\n"
"}")
        self.buttonFrame_5 = QFrame(self.createMoodPage)
        self.buttonFrame_5.setObjectName(u"buttonFrame_5")
        self.buttonFrame_5.setGeometry(QRect(460, 10, 241, 81))
        self.buttonFrame_5.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.buttonFrame_5.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame_5.setFrameShadow(QFrame.Raised)
        self.basedOnGenreLabel2_2 = QLabel(self.buttonFrame_5)
        self.basedOnGenreLabel2_2.setObjectName(u"basedOnGenreLabel2_2")
        self.basedOnGenreLabel2_2.setGeometry(QRect(70, 50, 108, 20))
        self.basedOnGenreLabel2_2.setFont(font4)
        self.basedOnGenreLabel2_2.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.basedOnGenreLabel2_2.setAlignment(Qt.AlignCenter)
        self.basedOnGenreLabel_2 = QLabel(self.buttonFrame_5)
        self.basedOnGenreLabel_2.setObjectName(u"basedOnGenreLabel_2")
        self.basedOnGenreLabel_2.setGeometry(QRect(60, 0, 131, 51))
        self.basedOnGenreLabel_2.setStyleSheet(u"image: url(:/icons/Media/icons/mood.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.genMoodButton = QPushButton(self.createMoodPage)
        self.genMoodButton.setObjectName(u"genMoodButton")
        self.genMoodButton.setGeometry(QRect(730, 290, 161, 31))
        self.genMoodButton.setFont(font6)
        self.genMoodButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(248, 231, 28);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"    border: none;\n"
"    outline: none;\n"
"	font-weight: bold;\n"
"}")
        self.moodDial = QDial(self.createMoodPage)
        self.moodDial.setObjectName(u"moodDial")
        self.moodDial.setGeometry(QRect(220, 160, 361, 231))
        self.moodDial.setStyleSheet(u"QDial {\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.moodDial.setNotchesVisible(True)
        self.moodDialLabel = QLabel(self.createMoodPage)
        self.moodDialLabel.setObjectName(u"moodDialLabel")
        self.moodDialLabel.setGeometry(QRect(360, 230, 81, 61))
        font12 = QFont()
        font12.setPointSize(12)
        font12.setBold(True)
        font12.setWeight(75)
        self.moodDialLabel.setFont(font12)
        self.moodDialLabel.setStyleSheet(u"QLabel {\n"
"	color: white;\n"
"	font-weight: bold;\n"
"	image: ;\n"
"}")
        self.moodDialLabel.setAlignment(Qt.AlignCenter)
        self.happyLabel = QLabel(self.createMoodPage)
        self.happyLabel.setObjectName(u"happyLabel")
        self.happyLabel.setGeometry(QRect(240, 310, 81, 41))
        font13 = QFont()
        font13.setFamily(u"Humnst777 BT")
        font13.setPointSize(12)
        font13.setBold(True)
        font13.setItalic(False)
        font13.setUnderline(False)
        font13.setWeight(75)
        font13.setStrikeOut(False)
        self.happyLabel.setFont(font13)
        self.happyLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.happyLabel.setAlignment(Qt.AlignCenter)
        self.neutralLabel = QLabel(self.createMoodPage)
        self.neutralLabel.setObjectName(u"neutralLabel")
        self.neutralLabel.setGeometry(QRect(230, 190, 81, 41))
        self.neutralLabel.setFont(font13)
        self.neutralLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.neutralLabel.setAlignment(Qt.AlignCenter)
        self.sadLabel = QLabel(self.createMoodPage)
        self.sadLabel.setObjectName(u"sadLabel")
        self.sadLabel.setGeometry(QRect(490, 190, 81, 41))
        self.sadLabel.setFont(font13)
        self.sadLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.sadLabel.setAlignment(Qt.AlignCenter)
        self.happyLabel_2 = QLabel(self.createMoodPage)
        self.happyLabel_2.setObjectName(u"happyLabel_2")
        self.happyLabel_2.setGeometry(QRect(480, 310, 81, 41))
        self.happyLabel_2.setFont(font13)
        self.happyLabel_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.happyLabel_2.setAlignment(Qt.AlignCenter)
        self.currentMoodLabel = QLabel(self.createMoodPage)
        self.currentMoodLabel.setObjectName(u"currentMoodLabel")
        self.currentMoodLabel.setGeometry(QRect(370, 290, 61, 31))
        font14 = QFont()
        font14.setFamily(u"Humnst777 BT")
        self.currentMoodLabel.setFont(font14)
        self.currentMoodLabel.setStyleSheet(u"color: rgb(46, 124, 255);")
        self.currentMoodLabel.setAlignment(Qt.AlignCenter)
        self.moodGenreTxtbox = QLineEdit(self.createMoodPage)
        self.moodGenreTxtbox.setObjectName(u"moodGenreTxtbox")
        self.moodGenreTxtbox.setGeometry(QRect(710, 210, 201, 30))
        self.moodGenreTxtbox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: white;\n"
"font-size: 12pt;\n"
"height: 30px;")
        self.label_36 = QLabel(self.createMoodPage)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(710, 180, 201, 31))
        self.label_36.setFont(font6)
        self.label_36.setStyleSheet(u"color: white;")
        self.genreLabel_3 = QLabel(self.createMoodPage)
        self.genreLabel_3.setObjectName(u"genreLabel_3")
        self.genreLabel_3.setGeometry(QRect(650, 200, 51, 41))
        self.genreLabel_3.setFont(font5)
        self.genreLabel_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_32 = QLabel(self.createMoodPage)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(700, 330, 221, 21))
        self.label_32.setFont(font7)
        self.label_32.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_32.setAlignment(Qt.AlignCenter)
        self.label_39 = QLabel(self.createMoodPage)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(200, 90, 761, 331))
        self.label_39.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.2);\n"
"border-style: none;\n"
"border-radius: 10px;")
        self.label_40 = QLabel(self.createMoodPage)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(260, 90, 181, 51))
        self.label_40.setFont(font11)
        self.label_40.setStyleSheet(u"color: rgb(74, 144, 226);")
        self.label_40.setAlignment(Qt.AlignCenter)
        self.moodPlaylistName = QLineEdit(self.createMoodPage)
        self.moodPlaylistName.setObjectName(u"moodPlaylistName")
        self.moodPlaylistName.setGeometry(QRect(450, 100, 441, 31))
        self.moodPlaylistName.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: rgb(144, 19, 254);\n"
"font-size: 12pt;\n"
"height: 30px;")
        self.frame_8 = QFrame(self.createMoodPage)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(200, 90, 761, 51))
        self.frame_8.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.7);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-top-radius\n"
"border-style: none;\n"
"color: white;\n"
"font-size: 12pt;\n"
"height: 30px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.stackedWidget.addWidget(self.createMoodPage)
        self.label_39.raise_()
        self.homeButtonFrame_6.raise_()
        self.buttonFrame_5.raise_()
        self.genMoodButton.raise_()
        self.moodDial.raise_()
        self.happyLabel.raise_()
        self.neutralLabel.raise_()
        self.sadLabel.raise_()
        self.happyLabel_2.raise_()
        self.moodGenreTxtbox.raise_()
        self.label_36.raise_()
        self.genreLabel_3.raise_()
        self.label_32.raise_()
        self.moodDialLabel.raise_()
        self.currentMoodLabel.raise_()
        self.frame_8.raise_()
        self.label_40.raise_()
        self.moodPlaylistName.raise_()
        self.moodLoadingPage = QWidget()
        self.moodLoadingPage.setObjectName(u"moodLoadingPage")
        self.buttonFrame_7 = QFrame(self.moodLoadingPage)
        self.buttonFrame_7.setObjectName(u"buttonFrame_7")
        self.buttonFrame_7.setGeometry(QRect(430, -10, 241, 131))
        self.buttonFrame_7.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.buttonFrame_7.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame_7.setFrameShadow(QFrame.Raised)
        self.homeButtonFrame_16 = QFrame(self.moodLoadingPage)
        self.homeButtonFrame_16.setObjectName(u"homeButtonFrame_16")
        self.homeButtonFrame_16.setGeometry(QRect(10, 0, 51, 51))
        self.homeButtonFrame_16.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.homeButtonFrame_16.setFrameShape(QFrame.StyledPanel)
        self.homeButtonFrame_16.setFrameShadow(QFrame.Raised)
        self.homeButton_mlp = QPushButton(self.homeButtonFrame_16)
        self.homeButton_mlp.setObjectName(u"homeButton_mlp")
        self.homeButton_mlp.setGeometry(QRect(10, 10, 31, 31))
        self.homeButton_mlp.setStyleSheet(u"QPushButton{\n"
"	image: url(:/icons/Media/icons/home_btn.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/home_btn.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: none;\n"
"    border: none;\n"
"    outline: none;\n"
"	border-radius: 40px;\n"
"}")
        self.label_33 = QLabel(self.moodLoadingPage)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(540, 210, 101, 21))
        self.label_33.setFont(font6)
        self.label_33.setStyleSheet(u"color: white;")
        self.frame_7 = QFrame(self.moodLoadingPage)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(200, 90, 331, 271))
        self.frame_7.setStyleSheet(u"image: url(:/images/Media/vpMood_location.png);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_34 = QLabel(self.moodLoadingPage)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(540, 120, 381, 31))
        self.label_34.setFont(font10)
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_35 = QLabel(self.moodLoadingPage)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(460, 10, 251, 31))
        self.label_35.setFont(font9)
        self.label_35.setStyleSheet(u"color: rgb(248, 231, 28);")
        self.moodLinkTxtbox = QTextEdit(self.moodLoadingPage)
        self.moodLinkTxtbox.setObjectName(u"moodLinkTxtbox")
        self.moodLinkTxtbox.setGeometry(QRect(540, 240, 391, 81))
        self.moodLinkTxtbox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: black;\n"
"font-size: 12pt;\n"
"height: 30px;")
        self.label_37 = QLabel(self.moodLoadingPage)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(210, 60, 751, 331))
        self.label_37.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.2);\n"
"border-style: none;\n"
"border-radius: 10px;")
        self.label_38 = QLabel(self.moodLoadingPage)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(540, 140, 391, 31))
        self.label_38.setFont(font10)
        self.label_38.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_46 = QLabel(self.moodLoadingPage)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(540, 160, 371, 31))
        self.label_46.setFont(font10)
        self.label_46.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.moodLoadingPage)
        self.label_37.raise_()
        self.buttonFrame_7.raise_()
        self.homeButtonFrame_16.raise_()
        self.label_33.raise_()
        self.frame_7.raise_()
        self.label_34.raise_()
        self.label_35.raise_()
        self.moodLinkTxtbox.raise_()
        self.label_38.raise_()
        self.label_46.raise_()
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
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	image: url(:/icons/Media/icons/goback.png);\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-style: none;\n"
"    border: none;\n"
"    outline: none;\n"
"	border-radius: 40px;\n"
"}")
        self.mainProfileFrame = QFrame(self.profilePage)
        self.mainProfileFrame.setObjectName(u"mainProfileFrame")
        self.mainProfileFrame.setGeometry(QRect(290, 90, 581, 211))
        self.mainProfileFrame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-style: none;\n"
"border-radius: 10px;")
        self.mainProfileFrame.setFrameShape(QFrame.StyledPanel)
        self.mainProfileFrame.setFrameShadow(QFrame.Raised)
        self.profilePicBox = QLabel(self.mainProfileFrame)
        self.profilePicBox.setObjectName(u"profilePicBox")
        self.profilePicBox.setGeometry(QRect(20, 20, 171, 171))
        self.profilePicBox.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.5);\n"
"border-style: none;\n"
"border-radius: 10px;")
        self.infoFrame = QFrame(self.mainProfileFrame)
        self.infoFrame.setObjectName(u"infoFrame")
        self.infoFrame.setGeometry(QRect(210, 20, 351, 171))
        self.infoFrame.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.5);")
        self.infoFrame.setFrameShape(QFrame.StyledPanel)
        self.infoFrame.setFrameShadow(QFrame.Raised)
        self.nameLabel = QLabel(self.infoFrame)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(20, 20, 51, 41))
        font15 = QFont()
        font15.setFamily(u"Humanst521 BT")
        font15.setPointSize(14)
        self.nameLabel.setFont(font15)
        self.nameLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.subscriptLabel = QLabel(self.infoFrame)
        self.subscriptLabel.setObjectName(u"subscriptLabel")
        self.subscriptLabel.setGeometry(QRect(20, 90, 81, 41))
        self.subscriptLabel.setFont(font15)
        self.subscriptLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.name_txtbox = QTextEdit(self.infoFrame)
        self.name_txtbox.setObjectName(u"name_txtbox")
        self.name_txtbox.setGeometry(QRect(80, 30, 251, 31))
        self.name_txtbox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: rgb(255, 255, 255);\n"
"font-size: 12pt;\n"
"height: 30px;")
        self.sub_txtbox = QTextEdit(self.infoFrame)
        self.sub_txtbox.setObjectName(u"sub_txtbox")
        self.sub_txtbox.setGeometry(QRect(120, 100, 211, 41))
        self.sub_txtbox.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"color: rgb(255, 255, 255);\n"
"font-size: 12pt;\n"
"height: 30px;")
        self.signoutButton = QPushButton(self.profilePage)
        self.signoutButton.setObjectName(u"signoutButton")
        self.signoutButton.setGeometry(QRect(510, 340, 151, 31))
        self.signoutButton.setFont(font6)
        self.signoutButton.setStyleSheet(u"QPushButton{\n"
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
        self.aboutLabel.setFont(font4)
        self.aboutLabel.setStyleSheet(u"QLabel{\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.aboutLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.aboutLabel)

        self.darkModeLabel = QLabel(self.frame_3)
        self.darkModeLabel.setObjectName(u"darkModeLabel")
        self.darkModeLabel.setFont(font4)
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
        self.frame_4.setGeometry(QRect(430, 80, 311, 321))
        self.frame_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.5);\n"
"border-style: none;\n"
"border-radius: 10px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 50, 141, 31))
        self.label_3.setFont(font15)
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 80, 181, 31))
        self.label_4.setFont(font15)
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 60, 91, 21))
        font16 = QFont()
        font16.setFamily(u"Humanst521 BT")
        font16.setPointSize(12)
        self.label_5.setFont(font16)
        self.label_5.setStyleSheet(u"color: white;\n"
"background-color: rgb(74, 74, 74);")
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(200, 90, 91, 21))
        self.label_6.setFont(font16)
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

        self.gridLayout_3.addWidget(self.stackedWidget, 0, 1, 1, 1)

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
        self.headerSignoutButton.setText(QCoreApplication.translate("VSMain", u"Sign Out", None))
        self.spotifyLabel.setText("")
        self.createButton.setText("")
        self.profileButton.setText("")
        self.settingsButton.setText("")
        self.createLabel.setText(QCoreApplication.translate("VSMain", u"Create+", None))
        self.profileLabel.setText(QCoreApplication.translate("VSMain", u"Profile", None))
        self.settingsLabel.setText(QCoreApplication.translate("VSMain", u"Settings", None))
        self.homeButton_create.setText("")
        self.createMoodButton.setText("")
        self.createGenreButton.setText("")
        self.createArtistButton.setText("")
        self.createArtistLabel.setText(QCoreApplication.translate("VSMain", u"Based On Artist", None))
        self.createMoodLabel.setText(QCoreApplication.translate("VSMain", u"Based on Mood", None))
        self.createGenreLabel.setText(QCoreApplication.translate("VSMain", u"Based on Genre", None))
        self.recommendButton.setText("")
        self.recommendLabel.setText(QCoreApplication.translate("VSMain", u"Random Recommend", None))
        self.basedOnArtistLabel2.setText(QCoreApplication.translate("VSMain", u"Based On Artist", None))
        self.basedOnArtistLabel.setText("")
        self.artist1Label.setText(QCoreApplication.translate("VSMain", u"Artist 1", None))
        self.artist2Label.setText(QCoreApplication.translate("VSMain", u"Artist 2", None))
        self.artist3Label.setText(QCoreApplication.translate("VSMain", u"Artist 3", None))
        self.artist4Label.setText(QCoreApplication.translate("VSMain", u"Artist 4", None))
        self.artist5Label.setText(QCoreApplication.translate("VSMain", u"Artist 5", None))
        self.homeButton_boa.setText("")
        self.genArtistButton.setText(QCoreApplication.translate("VSMain", u"Generate", None))
        self.label_30.setText(QCoreApplication.translate("VSMain", u"Note: This may take a moment...", None))
        self.label_43.setText(QCoreApplication.translate("VSMain", u"Name Your Playlist:", None))
        self.label_44.setText("")
        self.artistPlaylistName.setText("")
        self.label.setText(QCoreApplication.translate("VSMain", u"Your new playlist is ready!", None))
        self.label_2.setText(QCoreApplication.translate("VSMain", u"Look for the \"VibeShare Artist Playlist\" on your", None))
        self.homeButton_calp.setText("")
        self.label_20.setText(QCoreApplication.translate("VSMain", u"Your playlist link:", None))
        self.label_21.setText("")
        self.label_29.setText(QCoreApplication.translate("VSMain", u"Spotify app/ or if you decided to name your playlist,", None))
        self.label_47.setText(QCoreApplication.translate("VSMain", u"look for that instead!", None))
        self.homeButton_rlp.setText("")
        self.label_17.setText(QCoreApplication.translate("VSMain", u"Your new playlist is ready!", None))
        self.label_19.setText(QCoreApplication.translate("VSMain", u"Look for the \"VibeShare Recommendations\" on your", None))
        self.label_22.setText(QCoreApplication.translate("VSMain", u"Your playlist link:", None))
        self.label_23.setText("")
        self.label_24.setText(QCoreApplication.translate("VSMain", u"Spotify app", None))
        self.homeButton_glp.setText("")
        self.label_26.setText(QCoreApplication.translate("VSMain", u"Your playlist link:", None))
        self.label_25.setText(QCoreApplication.translate("VSMain", u"Look for the \"VibeShare Genre Playlist\" on your", None))
        self.label_18.setText(QCoreApplication.translate("VSMain", u"Your new playlist is ready!", None))
        self.label_27.setText("")
        self.label_28.setText(QCoreApplication.translate("VSMain", u"Spotify app/ or if you decided to name your playlist,", None))
        self.label_45.setText(QCoreApplication.translate("VSMain", u"look for that instead!", None))
        self.basedOnGenreLabel2.setText(QCoreApplication.translate("VSMain", u"Based On Genre", None))
        self.basedOnGenreLabel.setText("")
        self.genGenreButton.setText(QCoreApplication.translate("VSMain", u"Generate", None))
        self.genreLabel.setText(QCoreApplication.translate("VSMain", u"Genre", None))
        self.homeButton_bog.setText("")
        self.label_31.setText(QCoreApplication.translate("VSMain", u"Note: This may take a moment...", None))
        self.label_41.setText(QCoreApplication.translate("VSMain", u"Name Your Playlist:", None))
        self.label_42.setText("")
        self.homeButton_bom.setText("")
        self.basedOnGenreLabel2_2.setText(QCoreApplication.translate("VSMain", u"Based On Mood", None))
        self.basedOnGenreLabel_2.setText("")
        self.genMoodButton.setText(QCoreApplication.translate("VSMain", u"Generate", None))
        self.moodDialLabel.setText("")
        self.happyLabel.setText(QCoreApplication.translate("VSMain", u"Bliss", None))
        self.neutralLabel.setText(QCoreApplication.translate("VSMain", u"Neutral", None))
        self.sadLabel.setText(QCoreApplication.translate("VSMain", u"Mourn", None))
        self.happyLabel_2.setText(QCoreApplication.translate("VSMain", u"Rage", None))
        self.currentMoodLabel.setText("")
        self.label_36.setText(QCoreApplication.translate("VSMain", u"(Optional) Add a specific genre", None))
        self.genreLabel_3.setText(QCoreApplication.translate("VSMain", u"Genre", None))
        self.label_32.setText(QCoreApplication.translate("VSMain", u"Note: This may take a moment...", None))
        self.label_39.setText("")
        self.label_40.setText(QCoreApplication.translate("VSMain", u"Name Your Playlist:", None))
        self.homeButton_mlp.setText("")
        self.label_33.setText(QCoreApplication.translate("VSMain", u"Your playlist link:", None))
        self.label_34.setText(QCoreApplication.translate("VSMain", u"Look for the \"VibeShare Mood Playlist\" on your", None))
        self.label_35.setText(QCoreApplication.translate("VSMain", u"Your new playlist is ready!", None))
        self.label_37.setText("")
        self.label_38.setText(QCoreApplication.translate("VSMain", u"Spotify app/ or if you decided to name your playlist,", None))
        self.label_46.setText(QCoreApplication.translate("VSMain", u"look for that instead!", None))
        self.homeButton_profile.setText("")
        self.profilePicBox.setText("")
        self.nameLabel.setText(QCoreApplication.translate("VSMain", u"Name: ", None))
        self.subscriptLabel.setText(QCoreApplication.translate("VSMain", u"Spotify ID:", None))
        self.signoutButton.setText(QCoreApplication.translate("VSMain", u"Sign Out", None))
        self.homeButton_settings.setText("")
        self.aboutButton.setText("")
        self.darkModeButton.setText("")
        self.aboutLabel.setText(QCoreApplication.translate("VSMain", u"About", None))
        self.darkModeLabel.setText(QCoreApplication.translate("VSMain", u"Dark Mode On/ Off", None))
        self.homeButton_about.setText("")
        self.label_3.setText(QCoreApplication.translate("VSMain", u"Software Version: ", None))
        self.label_4.setText(QCoreApplication.translate("VSMain", u"Software Release Date:", None))
        self.label_5.setText(QCoreApplication.translate("VSMain", u"  v1.3_05_01", None))
        self.label_6.setText(QCoreApplication.translate("VSMain", u"  05/01/2021", None))
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

