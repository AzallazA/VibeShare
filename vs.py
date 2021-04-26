import sys, os, platform, requests, datetime, base64

from splash_screen import *
from ui_vs import *
from UserInterfaceFunctions import UserInterfaceFunctions

from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import *

from PySide2 import QtCore, QtGui, QtWidgets
#from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PyQt5.QtGui import QMovie

#from vs_auth import *

import tekore as tk
from tekore import UserAuth, RefreshingCredentials, RefreshingToken
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask
"""https://accounts.spotify.com/en/authorize?client_id=f0feb7039cfc44789f7b83631dc79825&redirect_uri=http:%2F%2Flocalhost:4555%2F&response_type=code
&scope=playlist-modify-private%20playlist-modify-public%20playlist-read-collaborative%20playlist-read-private%20ugc-image-upload%20user-follow-modify%20user-follow-read%20user-library-modify%20user-library-read%20user-modify-playback-state%20user-read-currently-playing%20user-read-email%20user-read-playback-position%20user-read-playback-state%20user-read-private%20user-read-recently-played%20user-top-read&state=dc9DNnpSuyUYtmBrBX-ZMuBhYt3G6UPoErA81JebNBM&show_dialog=true"""
#Globals
WINDOW_SIZE = 0
counter = 0

client_id = 'f0feb7039cfc44789f7b83631dc79825'
client_secret = '573953b4699945d0bae0eed31478aa0a'
redirect_uri = 'https://vibeshareapp.com/login.html'
scopes = tk.scope.every

cred = RefreshingCredentials(client_id, client_secret, redirect_uri)
auth = UserAuth(cred, scope=scopes)


class authWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.web = QWebEngineView()
        self.web.resize(800, 700)
        self.web.load(QUrl(auth.url))
        self.web.show()

        #cred = RefreshingCredentials(client_id, client_secret, redirect_uri)
        #auth = UserAuth(cred, scope=scopes)
        #link = accessCodeTxtBox.text()
        #user_token = auth.request_token(.strip())


# Main window class
class MainAppWindow(QMainWindow):

    def __init__(self):
        # Retreive Spotfy client and make spotify object
        """        spotify = tk.Spotify(app_token)
        #Get's user credentials and adds logs them in
        user_token = tk.prompt_for_user_token(client_id, client_secret, redirect_uri, scopes)
        spotify.token = user_token

        #Current user stuff
        user = spotify.current_user()
        user_id = user.id
        userName = user.display_name"""

        QMainWindow.__init__(self)
        self.ui = Ui_VSMain()
        self.ui.setupUi(self)

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
        #Sign out Buttons
        self.ui.headerSignoutButton.clicked.connect(lambda: self.close())
        self.ui.signoutButton.clicked.connect(lambda: self.close())
        #Restore/Maximize window
        #self.ui.restoreButton.clicked.connect(lambda: self.restore_or_maximize_window())
        # ###############################################
        self.show()

        #Stacked QtWidgets
        #self.ui.stackedWidget.setCurrentWidget(self.ui.homePage)
        self.ui.stackedWidget.setCurrentWidget(self.ui.loginPage)

        self.ui.spotifyLoginButton.clicked.connect(self.authWindow)

        self.ui.accessCodeButton.clicked.connect(self.getAccessCode)
        self.ui.accessCodeButton.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.homePage))

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

        #SETTINGS PAGE
        #self.ui.darkModeButton.clicked.connect(self.darkMode)
        self.ui.darkModeButton.setCheckable(True)
        self.ui.darkModeButton.clicked.connect(self.darkMode)

        #ABOUT PAGE
        self.ui.aboutButton.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.aboutPage))

        #CREATE ARTIST PAGE
        #Generate Artist Playlist
        self.ui.genArtistButton.clicked.connect(self.getArtistText)

        #Generate Reccomendations Button Clicked
        self.ui.recommendButton.clicked.connect(self.genRecommendations)

        self.ui.genGenreButton.clicked.connect(self.genGenre)
        #self.ui.genMoodButton.clicked.connect(self.genMood)

        #CREATE LOADING PAGE
        self.ui.genArtistButton.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.createArtistLoadingPage))
        self.ui.recommendButton.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.recommendLoadingPage))

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
        self.ui.homeButton_calp.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.homePage))
        self.ui.homeButton_rlp.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.homePage))

        self.ui.homeButton_about.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.settingsPage))
        self.ui.homeButton_about.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.settingsPage))

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

    def getAccessCode(self):
        redirected = self.ui.accessCodeTxtBox.toPlainText().strip()
        user_token = auth.request_token(url = redirected)
        print(user_token)

    #Dark Mode
    def darkMode(self):
        if self.ui.darkModeButton.isChecked():
            self.ui.centralwidget.setStyleSheet("""
            QWidget {
                background-color: rgb(57, 57, 57);
            }""")
            self.ui.headerFrame.setStyleSheet("""
            QFrame {
                background-color: rgb(57, 57, 57);
            }""")
            self.ui.footerFrame.setStyleSheet("""
            QFrame {
                background-color: rgb(57, 57, 57);
            }""")
        else:
            self.ui.centralwidget.setStyleSheet("""
            QWidget {
                background-color: qlineargradient(spread:pad, x1:0,
                y1:0.506, x2:1, y2:0.517, stop:0 rgba(170, 0, 255, 255),
                stop:1 rgba(0, 170, 255, 255));
            }""")
            self.ui.headerFrame.setStyleSheet("""
            QFrame {
                background-color: qlineargradient(spread:pad, x1:0,
                y1:0.506, x2:1, y2:0.517, stop:0 rgba(170, 0, 255, 255),
                stop:1 rgba(0, 170, 255, 255));
            }""")
            self.ui.footerFrame.setStyleSheet("""
            QFrame {
                background-color: qlineargradient(spread:pad, x1:0,
                y1:0.506, x2:1, y2:0.517, stop:0 rgba(170, 0, 255, 255),
                stop:1 rgba(0, 170, 255, 255));
            }""")

    #Generating based on Artist
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

        artist_list = [artist1_out, artist2_out, artist3_out, artist4_out, artist5_out]
        while("" in artist_list):
            artist_list.remove("")

        playlist = spotify.playlist_create(user_id, name = "VibeShare Playlist",
            public = True, description = "Made with VibeShare")

        for artist_out in artist_list:
            artists, = spotify.search(artist_out, types=('artist',), limit = 1)
            artist = artists.items[0]
            tracks = spotify.artist_top_tracks(artist.id, market = 'US')
            uris = [track.uri for track in tracks]
            spotify.playlist_add(playlist.id, uris = uris)
            print("Your playlist url is" + playlist.uri)

    #Generating based on genre
    def genGenre(self):
        print("button clicked")

    #Generating based on mood
    def genMood(self):
        print("button clicked")

    #Generating based on recommendations
    def genRecommendations(self):
        top_tracks = spotify.current_user_top_tracks(limit=5).items
        top_track_ids = [t.id for t in top_tracks]
        recommendations = spotify.recommendations(track_ids=top_track_ids).tracks

        playlist = spotify.playlist_create(
            user.id,
            'VibeShare Recommendations',
            public=False,
            description='Recommendations based on your top tracks <3'
        )
        uris = [t.uri for t in recommendations]
        spotify.playlist_add(playlist.id, uris=uris)

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
    def authWindow(self):
        self.auth = authWindow()
        #self.auth.show()
        #self.hide()
# Execute app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainAppWindow()
    sys.exit(app.exec_())
