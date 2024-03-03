from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PySide2.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QFrame, QGraphicsBlurEffect, QGraphicsDropShadowEffect, QLabel, QMainWindow, QPushButton
from pygame import mixer 
import glob 
import sys

images = glob.glob("/Users/abdurrehman/Desktop/Mp3Player/backgroundImages/*.*")
print("IMAGE FOUND : ",images[0])
