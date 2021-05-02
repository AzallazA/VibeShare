import sys, os, platform, requests, datetime, base64
import ctypes, subprocess

from secrets import *
from bs4 import BeautifulSoup
import requests, lxml, html5lib
import re, random

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
import webbrowser

#from vs_auth import *

import tekore as tk
from tekore import UserAuth, RefreshingCredentials, RefreshingToken
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask
"""https://accounts.spotify.com/en/authorize?client_id=f0feb7039cfc44789f7b83631dc79825&redirect_uri=https:%2F%2Fvibeshareapp.com%2Flogin.html&response_type=token
&scope=playlist-modify-private%20playlist-modify-public%20playlist-read-collaborative%20playlist-read-private%20ugc-image-upload%20user-follow-modify%20user-follow-read%20user-library-modify%20user-library-read%20user-modify-playback-state%20user-read-currently-playing%20user-read-email%20user-read-playback-position%20user-read-playback-state%20user-read-private%20user-read-recently-played%20user-top-read&state=dc9DNnpSuyUYtmBrBX-ZMuBhYt3G6UPoErA81JebNBM&show_dialog=true"""
#Globals
WINDOW_SIZE = 0
counter = 0

# Client info and redirect and scope info as needed
client_id = 'b74cf8069d564daaa6bcc7eb21e80c52'
client_secret = '217c6d35964545128c1efc70908ebfbc'
redirect_uri = 'https://vibeshareapp.com/login.html'
scopes = tk.scope.every

#The following lines get the user_token by opening the browser and prompting login
cred = RefreshingCredentials(client_id, client_secret, redirect_uri)
auth = UserAuth(cred, scope=scopes)
webbrowser.open(auth.url)
redirected = input('Please paste redirect URL here: ') #stores the redirect URL
user_token = auth.request_token(url = redirected) #gets the token from the URL

#creates the spotify object and gets the user
spotify = tk.Spotify(user_token)
user = spotify.current_user()

# Main window class
class MainAppWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_VSMain()
        self.ui.setupUi(self)

        # Remove window tlttle bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #Get's user credentials and adds logs them in
        user_id = user.id
        userName = user.display_name
        #print(userName)

        # Apply shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 150))
        # Appy shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        self.ui.stackedWidget.setCurrentWidget(self.ui.homePage)

        #SPOTIFY USER
        #Set Profile Picture on Profile Page
        amountOfImages = len(user.images)
        if amountOfImages == 0:
            self.ui.profilePicBox.setPixmap("Media/icons/default.png")
        else:
            image_url = user.images[0].url
            image = QImage()
            image.loadFromData(requests.get(image_url).content)
            pixmap = QPixmap(image)
            pixmap = pixmap.scaled(181, 171)
            self.ui.profilePicBox.setPixmap(pixmap)

        self.ui.headerProfileName.setText(userName)
        self.ui.name_txtbox.setText(userName)
        self.ui.sub_txtbox.setText(user_id)
        self.ui.headerProfileName.setText(user.display_name)
        self.ui.name_txtbox.setText(user.display_name)
        self.ui.sub_txtbox.setText(user.id)
        self.ui.headerProfileName.setPlainText(userName)

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

        #GENERATE
        #Generate Artist Playlist
        self.ui.genArtistButton.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.createArtistLoadingPage))
        self.ui.genArtistButton.clicked.connect(self.getArtistText)


        #Generate Reccomendations Button Clicked
        self.ui.recommendButton.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.recommendLoadingPage))
        self.ui.recommendButton.clicked.connect(self.genRecommendations)

        #Generate Genre
        self.ui.genGenreButton.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.genreLoadingPage))
        self.ui.genGenreButton.clicked.connect(self.genGenre)

        #Generate Mood
        self.ui.genMoodButton.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.moodLoadingPage))
        self.ui.genMoodButton.clicked.connect(self.genMood)

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
        self.ui.homeButton_glp.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.homePage))
        self.ui.homeButton_mlp.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.homePage))

        self.ui.homeButton_about.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.settingsPage))
        self.ui.homeButton_about.clicked.connect(lambda: self.ui.stackedWidget.
            setCurrentWidget(self.ui.settingsPage))

        #self.ui.stackedWidget.setCurrentWidget(self.ui.homePage)

        #Mood dial
        self.ui.moodDialLabel.setPixmap('Media/icons/happy.png')
        self.ui.currentMoodLabel.setText('Blissful')
        self.ui.moodDial.valueChanged.connect(self.dial_changed)

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
        """if self:
            if spotify == spotify:
                #Minimize command prompt automatically
                print('Logining In...')
                ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )"""
        # ###############################################
    # ###############################################
    # Add mouse events to the window
    # ###############################################

    #Mood dial value
    def dial_changed(self):
        getVal = self.ui.moodDial.value()
        #self.ui.valueLabel.setText(str(getVal))
        #self.ui.moodDialLabel.setText(str(getVal))
        if getVal >= 0 and getVal <= 19:
            self.ui.currentMoodLabel.setText('Blissful')
            self.ui.moodDialLabel.setPixmap('Media/icons/happy.png')
        elif getVal >= 20 and getVal <= 49:
            self.ui.currentMoodLabel.setText('Neutral')
            self.ui.moodDialLabel.setPixmap('Media/icons/meh.png')
        elif getVal >= 50 and getVal <= 79:
            self.ui.currentMoodLabel.setText('Mournful')
            self.ui.moodDialLabel.setPixmap('Media/icons/sad.png')
        elif getVal >= 80 and getVal <= 99:
            self.ui.currentMoodLabel.setText('Rageful')
            self.ui.moodDialLabel.setPixmap('Media/icons/angry.png')

    """def openSpotify(self):
        return#webbrowser.open_new('')

    def getAccessCode(self):
        redirected = self.ui.accessCodeTxtBox.toPlainText()
        print(redirected)"""

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
        artist1_out = self.ui.artist1_txtbox.text()
        artist2_out = self.ui.artist2_txtbox.text()
        artist3_out = self.ui.artist3_txtbox.text()
        artist4_out = self.ui.artist4_txtbox.text()
        artist5_out = self.ui.artist5_txtbox.text()

        artist_list = [artist1_out, artist2_out, artist3_out, artist4_out, artist5_out]
        while("" in artist_list):
            artist_list.remove("")

        playlist = spotify.playlist_create(user.id, name = "VibeShare Artist Playlist",
            public = True, description = "Made with VibeShare. Based on your preferred artists!")

        for artist_out in artist_list:
            artists, = spotify.search(artist_out, types=('artist',), limit = 1)
            artist = artists.items[0]
            tracks = spotify.artist_top_tracks(artist.id, market = 'from_token')
            uris = [track.uri for track in tracks]
            spotify.playlist_add(playlist.id, uris = uris)

        self.ui.artistLinkTxtbox.setText('spotify:playlist:' + str(playlist))
        webbrowser.open_new(str('spotify:playlist:' + str(playlist)))

        self.ui.artist1_txtbox.clear()
        self.ui.artist2_txtbox.clear()
        self.ui.artist3_txtbox.clear()
        self.ui.artist4_txtbox.clear()
        self.ui.artist5_txtbox.clear()

    #Generating based on genre
    def genGenre(self):
        genre_out = self.ui.genre_txtbox.text()
        genre = genre_out.replace(' ', '+')
        source = requests.get("https://everynoise.com/research.cgi?mode=genre&name=" + genre).text
        soup = BeautifulSoup(source, 'lxml')
        links = soup.find_all('div', class_='artistname')
        artists_list = []
        for class_tag in soup.find_all('div', class_='artistname'):
            a_tag = class_tag.find('a')
            for name in a_tag:
                artists_list.append(name.string)

        random_artists = random.sample(artists_list, 30)

        playlist = spotify.playlist_create(user.id, name = "VibeShare Genre Playlist",
            public = True, description = "Made with VibeShare. Based on your preferred genre!")

        uris = []
        for art in random_artists:
            artists, = spotify.search(art, types=('artist',), limit = 1)
            artist = artists.items[0]
            tracks = spotify.artist_top_tracks(artist.id, market = 'from_token')
            uris.append(tracks[0].uri)
        spotify.playlist_add(playlist.id, uris = uris)

        self.ui.genreLinkTxtbox.setText(str(playlist.uri))
        webbrowser.open_new(str(playlist.uri))
        self.ui.genre_txtbox.clear()

    #Generating based on mood
    def genMood(self):
        getVal = self.ui.moodDial.value()
        search_emotion = ""
        #Bliss
        if getVal >= 0 and getVal <= 19:
            search_emotion = "happy"
        #Neutral
        elif getVal >= 20 and getVal <= 49:
            search_emotion = "popular"
        #Mourn
        elif getVal >= 50 and getVal <= 79:
            search_emotion = "sad"
        #Rage
        elif getVal >= 80 and getVal <= 99:
            search_emotion = "angry"

        genre = self.ui.moodGenreTxtbox.text()
        if genre == "":
            search = search_emotion
        else:
            search = search_emotion + " " + genre
        print(search)

        moodPlaylist = spotify.playlist_create(user.id, name = "VibeShare Mood Playlist",
            public = True, description = "Made with VibeShare. Based on your provided mood!")

        tracks = []
        addTrack = []

        playlists, = spotify.search(search, types=('playlist',))
        playlist = playlists.items[0]
        tracks = spotify.playlist_items(playlist.id).items
        for track in tracks:
            addTrack.append(track.track)
        uris = [track.uri for track in addTrack]
        spotify.playlist_add(moodPlaylist.id, uris = uris)
        self.ui.moodLinkTxtbox.setText(str(moodPlaylist.uri))
        webbrowser.open_new(str(moodPlaylist.uri))

    #Generating based on recommendations
    def genRecommendations(self):
        top_tracks = spotify.current_user_top_tracks(limit=5).items
        top_track_ids = [t.id for t in top_tracks]
        recommendations = spotify.recommendations(track_ids=top_track_ids).tracks

        playlist = spotify.playlist_create(
            user.id,
            'VibeShare Recommendations',
            public=True,
            description='Recommendations based on your top tracks <3'
        )
        uris = [t.uri for t in recommendations]
        spotify.playlist_add(playlist.id, uris=uris)

        self.ui.recommendtLinkTxtbox.setText('spotify:playlist:' + str(playlist.id))
        webbrowser.open_new(str('spotify:playlist:' + str(playlist.id)))

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
