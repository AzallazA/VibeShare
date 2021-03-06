import sys
import os
import platform

from ui_splash_screen import *
from vs import *

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# Global values
progressBarValue = 0

# Main class/ Splash window
class SplashWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
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

        #Lets use QTIMER to delay the progressBar
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.appProgress)

        #Time interval in Milliseconds for the progressbar to change value
        self.timer.start(30)

        # Show window
        self.show()


    # Lets define appProgress function
    #Update the progressBar value
    def appProgress(self):
        # Acess the global variable progressBarValue
        global progressBarValue

        #Apply progressBarValue to the progressBar
        self.ui.progressBar.setValue(progressBarValue)

        #View progressBarValue and update status text or close splash screen and open main window(We'll do this on next tutorial)
        if progressBarValue > 100:
                #reset / stop timer
                self.timer.stop()
                self.main = MainAppWindow()
                #Close the splash screen after the progress is complete
                self.close()

                # Lets change the loading status text
                # QtCore.QTimer.singleShot(0, lambda: self.ui.loading_progress_status.setText("Loading completed succesfully"))

                # Show main window when the progress is over

            #####    #self.VSMain = AppWindow()
            #####    #self.VSMain.show()

        # Lets update the loading status text as the progress changes
        elif progressBarValue < 10:
                QtCore.QTimer.singleShot(0, lambda: self.ui.loading_progress_status.setText("Connecting to Nike server"))

        elif progressBarValue < 20:
                QtCore.QTimer.singleShot(0, lambda: self.ui.loading_progress_status.setText("Logging in..."))

        elif progressBarValue < 35:
                QtCore.QTimer.singleShot(0, lambda: self.ui.loading_progress_status.setText("Logging in succesfully. Requesting profile..."))

        elif progressBarValue < 55:
                QtCore.QTimer.singleShot(0, lambda: self.ui.loading_progress_status.setText("Profile set to Spinn Design. Requesting Spinn Design profile information..."))

        elif progressBarValue < 65:
                QtCore.QTimer.singleShot(0, lambda: self.ui.loading_progress_status.setText("Finalizing profile setup..."))

        elif progressBarValue < 85:
                QtCore.QTimer.singleShot(0, lambda: self.ui.loading_progress_status.setText("Almost done...."))

                # Change loadingstatus text
                QtCore.QTimer.singleShot(0, lambda: self.ui.loadingstatus.setText("Spinn Design"))

        #increase progressBarValue by 1 after every time interval we set of 100 milliseconds;
        progressBarValue+=1

# Execute app
#
if __name__ == "__main__":
    app = QApplication(sys.argv)
    splashWin = SplashWindow()
    sys.exit(app.exec_())
