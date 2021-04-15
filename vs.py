import sys
import os
import platform

from splash_screen import *
from ui_vs import *
from UserInterfaceFunctions import UserInterfaceFunctions

from PyQt5.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import tekore as tk

#import qdarkstyle
WINDOW_SIZE = 0
counter = 0

# Main window class
class MainAppWindow(QMainWindow):

    # Retreive Spotfy client and make spotify object
    '''    client_id = 'f0feb7039cfc44789f7b83631dc79825'
    client_secret = '573953b4699945d0bae0eed31478aa0a'
    app_token = tk.request_client_token(client_id, client_secret)
    spotify = tk.Spotify(app_token)
    scopes = tk.scope.every

    #Get's user credentials and adds logs them in
    user_token = tk.prompt_for_user_token(client_id, client_secret, 'http://localhost:4555/', scopes)
    spotify.token = user_token

    user = spotify.current_user()
    user_id = user.id
    userName = user.display_name'''

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_VSMain()
        self.ui.setupUi(self)

        #Dark Mode
        #app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())

        # Remove window tlttle bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Apply shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 150))
        # Appy shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        # Button click events to our top bar buttons

        #Minimize window
        self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())
        #Close window
        self.ui.closeButton.clicked.connect(lambda: self.close())
        #Restore/Maximize window
        self.ui.restoreButton.clicked.connect(lambda: self.restore_or_maximize_window())
        # ###############################################
        self.show()
        #Stacked QtWidgets
        self.ui.stackedWidget.setCurrentWidget(self.ui.homePage)

        #Stacked Widget buttons (Navigation)
        #HOME PAGE
        #Create Button
        self.ui.createButton.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.createPage))
        #Profile Button
        self.ui.profileButton.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.profilePage))
        #Settings Button
        self.ui.settingsButton.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.settingsPage))

        #CREATE PAGE
        self.ui.createArtistButton.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.createArtistPage))
        self.ui.createGenreButton.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.createGenrePage))
        self.ui.createMoodButton.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.createMoodPage))


        #CREATE ARTIST PAGE
        #Generate Artist Playlist
        self.ui.genArtistButton.clicked.connect(self.getArtistText)

        self.ui.genGenreButton.clicked.connect(self.genGenre)
        #self.ui.genMoodButton.clicked.connect(self.genMood)

        #Home buttons
        self.ui.homeButton_create.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.homePage))
        self.ui.homeButton_profile.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.homePage))
        self.ui.homeButton_settings.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.homePage))
        self.ui.homeButton_boa.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.createPage))
        self.ui.homeButton_bog.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.createPage))
        self.ui.homeButton_bom.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.createPage))

        # ###############################################
        # Move window on mouse drag event on the tittle bar
        # ###############################################
        def moveWindow(e):
            # Detect if the window is  normal size
            # ###############################################
            if self.isMaximized() == False: #Not maximized
                # Move window only when window is normal size
                # ###############################################
                #if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:
                    #Move window
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
            # ###############################################

        #Window Size Grip
        #QSizeGrip(self.ui.sizeGrip)

        # ###############################################
        # Add click event/Mouse move event/drag event to the top header to move the window
        # ###############################################
        self.ui.headerFrame.mouseMoveEvent = moveWindow
        # ###############################################
        # Show window
        self.show()
        # ###############################################
    # ###############################################
    # Add mouse events to the window
    # ###############################################


    #Submit Button For Generating based on Artist
    def getArtistText(self):
        print("button clicked")
        artist1_out = self.ui.artist1_txtbox.text()
        artist2_out = self.ui.artist2_txtbox.text()
        artist3_out = self.ui.artist3_txtbox.text()
        artist4_out = self.ui.artist4_txtbox.text()
        artist5_out = self.ui.artist5_txtbox.text()

        if artist1_out == "":
            print("This field cannot be blank")
        else:
            print(artist1_out + ", " + artist2_out + ", " +
             artist3_out + ", " + artist4_out + ", " + artist5_out)

    #Submit Button For Generating based on genre
    def genGenre(self):
        print("button clicked")

    #Submit Button For Generating based on mood
    def genMood(self):
        print("button clicked")



    def mousePressEvent(self, event):
        # ###############################################
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # We will use this value to move the window
        # ###############################################
    # ###############################################

    # Restore or maximize your window
    def restore_or_maximize_window(self):
        # Global windows state
        global WINDOW_SIZE #The default value is zero to show that the size is not maximized
        win_status = WINDOW_SIZE

        if win_status == 0:
                # If the window is not maximized
            WINDOW_SIZE = 1 #Update value to show that the window has been maxmized
            self.showMaximized()
        else:
                # If the window is on its default size
            WINDOW_SIZE = 0 #Update value to show that the window has been minimized/set to normal size (which is 800 by 400)
            self.showNormal()
    # /////////////////////////////////////////////////////////////////////////

# Execute app
#
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainAppWindow()
    sys.exit(app.exec_())
