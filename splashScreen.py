from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import sys 
from test import Test
import time


class Splashscreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 500)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect()
        self.PBshadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(20)
        self.PBshadow.setBlurRadius(100)

        self.counter = 0 
        self.n = 300
        self.timer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(30)
        self.initUI()
       
    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.frame = QFrame()
        self.frame.setGraphicsEffect(self.shadow)
        layout.addWidget(self.frame)
        
        self.labelTitle = QLabel(self.frame)
        self.labelTitle.setObjectName('labelTitle')
        self.labelTitle.resize(self.width() - 10, 150)
        self.labelTitle.move(0, 40)
        self.labelTitle.setAlignment(Qt.AlignCenter)
        self.labelTitle.setText("<strong>MP3 PLAYER</strong>")
        self.labelTitle.setFont(QFont("Helvetica [Cronyx]"))

        self.labelDescription = QLabel(self.frame)
        self.labelDescription.setObjectName('labelDesc')
        self.labelDescription.resize(self.width() - 10, 150)
        self.labelDescription.move(0, self.labelTitle.height())
        self.labelDescription.setAlignment(Qt.AlignCenter)
        self.labelDescription.setText("<strong>loading...</strong>")
        self.labelDescription.setFont(QFont("Arial"))

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.resize(self.width() - 200 - 10,20)
        self.progressBar.move(100, self.labelDescription.y() +130)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setFormat('%p%')
        self.progressBar.setTextVisible(True)
        self.progressBar.setRange(0, self.n)
        self.progressBar.setValue(20)
        self.progressBar.setObjectName("pBar")
        self.progressBar.setGraphicsEffect(self.PBshadow)


    def loading(self):
        self.progressBar.setValue(self.counter)

        if self.counter >= self.n + 1:
            self.timer.stop()
            self.close()
            time.sleep(1)
            self.win = Test()
            self.win.show()

        self.counter += 1 
def window():
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        #labelTitle {
            font-size: 60px;
            color: #EDF5E1; 
         
        }
        #labelDesc {
            font-size: 30px;
            color: #EDF5E1; 
            
        }
        QFrame {
            background-color: #379683;
            color: black; 
        }
        QProgressBar {
            background-color: #5CDB95;
            color: #379683;
            border-style:none;
            border-radius: 10px;
        }
        QProgressBar::chunk {

            border-radius: 10px;
            background-color: #8EE4AF;
        }
    ''')
    splash = Splashscreen()
    splash.show()
    sys.exit(app.exec_())


window()
