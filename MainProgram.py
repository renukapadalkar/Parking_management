import sys
import os
#from PyQt5 import Qt
from InstallWindows import InstallWindow
from LoginWindow import LoginScreen
from PyQt5.QtWidgets import QApplication, QSplashScreen,QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer

from HomeWindow import HomeScreen



class MainScreen():
    def showSplashScreen(self):  # introduction image
        self.pix=QPixmap("python_vehicle.png")
        self.splassh=QSplashScreen(self.pix,Qt.WindowStaysOnTopHint)
        self.splassh.show()

#creating functions to show install window and login window
def showSetupWindow():
    mainScreen.splassh.close()
    installWindow.show()

def showLoginWindow():
    mainScreen.splassh.close()

    login.showLoginScreen()


app=QApplication(sys.argv)
login=LoginScreen()
mainScreen=MainScreen()
mainScreen.showSplashScreen()
installWindow=InstallWindow()

if os.path.exists("./config.json"): #(JavaScript Object Notation)
    QTimer.singleShot(3000,showLoginWindow)

else:
    QTimer.singleShot(3000, showSetupWindow)

sys.exit(app.exec_())  #adding app instance into sys.exit() to terminate program