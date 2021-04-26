import sys, requests, platform, os
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import *
from flask import Flask
from bs4 import BeautifulSoup
import tekore as tk

client_id = 'b74cf8069d564daaa6bcc7eb21e80c52'
client_secret = '217c6d35964545128c1efc70908ebfbc'
redirect = 'https:%2F%2Fvibeshareapp.com%2Flogin.html'
response_type = 'token'
scope = 'playlist-modify-private%20playlist-modify-public%20playlist-read-collaborative%20playlist-read-private%20ugc-image-upload%20user-follow-modify%20user-follow-read%20user-library-modify%20user-library-read%20user-modify-playback-state%20user-read-currently-playing%20user-read-email%20user-read-playback-position%20user-read-playback-state%20user-read-private%20user-read-recently-played%20user-top-read'
state = 'ZA_2buN-j5U4W37boUkV7a9OW1oyojBt8kY9rSNZBps'
show_dialog = 'true'

redirect_uri = ('https://accounts.spotify.com/authorize?' +
'client_id=' + client_id + '&redirect_uri=' + redirect
+ '&response_type=' + response_type + ('&scope=' + scope) +
'&state=' + state + '&show_dialog=' + show_dialog)

app = QApplication(sys.argv)
web = QWebEngineView()
web.resize(800, 700)

web.load(QUrl(redirect_uri))
web.show()


sys.exit(app.exec_())
