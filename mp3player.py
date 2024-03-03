from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont, QCursor
from PySide2.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QFrame, QGraphicsBlurEffect, QGraphicsDropShadowEffect, QLabel, QMainWindow, QPushButton
from pygame import mixer 
import glob 
import sys
class Test(QMainWindow):
    def __init__(self):
        super(Test, self).__init__()
        self.x, self.y = 250, 200 
        self.w, self.h = 800, 650
        self.count = 0
        self.flag = 0 
        self.ispause = False
        self.volume = 1
        self.imCount = 0 
        # self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.initUI()
        self.filesList = glob.glob("/Users/abdurrehman/Desktop/Mp3Player/mp3files/*.*")
        self.images = glob.glob("/Users/abdurrehman/Desktop/Mp3Player/backgroundImages/*.*")
        mixer.init()
        pix = QPixmap("/Users/abdurrehman/Desktop/Mp3Player/logos/cursor.png")
        cursor = QCursor(pix)
        self.setCursor(cursor)

        
    def initUI(self):   
        self.setGeometry(self.x, self.y, self.w, self.h)
        self.mainFrame = QFrame(self)
        self.mainFrame.setGeometry(0, 0, self.w, self.h)
        self.mainFrame.setObjectName('MF')

        pix = QPixmap("/Users/abdurrehman/Desktop/Mp3Player/logos/cursorHover.png")
        cursor = QCursor(pix)

        # self.mFBlur = QGraphicsBlurEffect()
        # self.mainFrame.setGraphicsEffect(self.mFBlur)

        self.innerLabel = QLabel(self.mainFrame)
        self.innerLabel.setObjectName('IL')
        self.innerLabel.setGeometry(250,80,300,500)
        self.innerLabel.setWindowOpacity(0.9)
        self.innerShadow = QGraphicsDropShadowEffect()
        self.innerShadow.setBlurRadius(50)
        self.innerLabel.setGraphicsEffect(self.innerShadow)

        self.logoImg = QLabel(self.innerLabel)
        self.logoImg.setGeometry(50,60,200,200)
        self.logoImg.setObjectName('Logo')
        self.innerShadow.setBlurRadius(100)
        self.logoImg.setGraphicsEffect(self.innerShadow)
     

        
        self.b0 = QPushButton(self.logoImg)
        self.b0.setGeometry(57, 57, 85, 85)
        self.b0.clicked.connect(self.mid)

        self.b1 = QPushButton(self.innerLabel)
        self.b1.setGeometry(130, 330, 35, 35)
        self.b1.clicked.connect(self.start)
        self.b1.setCursor(cursor)

        self.b2 = QPushButton(self.innerLabel)
        self.b2.setGeometry(90, 330, 35, 35)
        self.b2.clicked.connect(self.prev)
        self.b2.setCursor(cursor)

        self.b3 = QPushButton(self.innerLabel)
        self.b3.setGeometry(170, 330, 35, 35)
        self.b3.clicked.connect(self.nextt)
        self.b3.setCursor(cursor)
        
        self.b4 = QPushButton(self.innerLabel)
        self.b4.setGeometry(132, 380, 33, 33)
        self.b4.clicked.connect(self.loop)
        self.b4.setCursor(cursor)
        
        self.b5 = QPushButton(self.innerLabel)
        self.b5.setGeometry(173, 380, 33, 33)
        self.b5.clicked.connect(self.incVolume)
        self.b5.setCursor(cursor)

        self.b6 = QPushButton(self.innerLabel)
        self.b6.setGeometry(91, 380, 33, 33)
        self.b6.clicked.connect(self.decVolume)
        self.b6.setCursor(cursor)
        
        self.closeImg = QLabel(self.mainFrame)
        self.closeImg.setGeometry(740, 0, 57, 57)
        self.closeImg.setObjectName('Logo')
        self.closeImg.setStyleSheet("background-color: transparent;")
        self.innerShadow.setBlurRadius(200)
        self.closeImg.setGraphicsEffect(self.innerShadow)
        self.closeImg.setWindowOpacity(0.1)
        
        self.b7 = QPushButton(self.closeImg)
        self.b7.setGeometry(0, 0, 57, 57)
        self.b7.clicked.connect(self.closeWindow)
        self.b7.setCursor(cursor)
        # background-image: url('/Users/abdurrehman/Desktop/Mp3Player/logos/question-mark.png');
        #  background-image: url("/Users/abdurrehman/Desktop/Mp3Player/newpng.png");
        self.mainFrame.setStyleSheet('''
            #MF {

                background-image: url("/Users/abdurrehman/Desktop/Mp3Player/backgroundImages/2.jpeg");
                background-position: center;   
                background-repeat: no-repeat;
            }
        ''')
        self.innerLabel.setStyleSheet('''
            #IL {

                background-color: rgba(255,255,255,0.3);
                border: 2px solid white;
                border-top-left-radius: 50px;
                border-bottom-right-radius: 50px;
                border-top-right-radius: 2px;
                border-bottom-left-radius: 2px;
            }
            #Logo {

                background-image: url("/Users/abdurrehman/Desktop/test.jpg");
                background-position: center;  
            }
        ''')
        self.logoImg.setStyleSheet('''
        QLabel {
            border: 1px solid white;
            border-radius: 3px;
        }
        ''')
        self.b0.setStyleSheet('''
        QPushButton {
           
            background-position: center;  
            background-repeat: no-repeat;
            background-color: transparent;
            
        }
        ''')
        self.b1.setStyleSheet('''
        QPushButton {
            background-image: url('/Users/abdurrehman/Desktop/Mp3Player/logos/stopButton.png');
            background-position: center;  
            background-repeat: no-repeat;
            background-color: transparent;
            border: 1px solid black;
            }
        QPushButton:hover {
            border: 1px solid white;
            border-style: dashed;
        }
        ''')
        self.b2.setStyleSheet('''
        QPushButton {
            background-image: url('/Users/abdurrehman/Desktop/Mp3Player/logos/leftarrow.png');
            background-position: center;  
            background-repeat: no-repeat;
            background-color: transparent;
            }
        QPushButton:hover {
            border-bottom: 2px solid white;
            border-style: dashed;
        }
        ''')
        self.b3.setStyleSheet('''
        QPushButton {
            background-image: url('/Users/abdurrehman/Desktop/Mp3Player/logos/rightarrow.png');
            background-position: center;  
            background-repeat: no-repeat;
            background-color: transparent;
            }
        QPushButton:hover {
            border-bottom: 2px solid white;
            border-style: dashed;
        }
        ''')
        self.b4.setStyleSheet('''
        QPushButton {
            background-image: url('/Users/abdurrehman/Desktop/Mp3Player/logos/refreshh.png');
            background-position: center;  
            background-repeat: no-repeat;
            background-color: transparent;
    
            }
        QPushButton:hover {
            border-bottom: 2px solid white;
            border-style: dashed;
        }
        ''')
        self.b5.setStyleSheet('''
        QPushButton {
            background-image: url('/Users/abdurrehman/Desktop/Mp3Player/logos/speaker.png');
            background-position: center;  
            background-repeat: no-repeat;
            background-color: transparent;

            }
        QPushButton:hover {
            border-bottom: 2px solid white;
            border-style: dashed;
        }
        ''')   
        self.b6.setStyleSheet('''
        QPushButton {
            background-image: url('/Users/abdurrehman/Desktop/Mp3Player/logos/speaker2.png');
            background-position: center;  
            background-repeat: no-repeat;
            background-color: transparent;

            }
        QPushButton:hover {
            border-bottom: 2px solid white;
            border-style: dashed;
        }
        ''')
        self.b7.setStyleSheet('''
        QPushButton {
            background-image: url('/Users/abdurrehman/Desktop/Mp3Player/logos/close.png');
            background-position: center;  
            background-repeat: no-repeat;
            background-color: transparent;

            }
        QPushButton:hover {
            border-bottom: 2px solid white;
            border-style: dashed;
            
        }
        ''')
    def closeWindow(self):
        self.close()
    
    def mid(self):
        print('pressed')

    def prev(self):
        if self.count < 0:
            self.count = len(self.filesList)
            self.count -=1
            # self.start()
            mixer.music.load(self.filesList[self.count])
            mixer.music.play()

        else:
            print("Previous")
            self.count -=1
            # self.start()
            mixer.music.load(self.filesList[self.count])
            mixer.music.play()
    def start(self):
        print("Start")
        self.flag +=1
        mixer.music.load(self.filesList[self.count])
        if self.flag % 2 != 0: 
            mixer.music.play()
            self.b1.setStyleSheet('''
            background-image: url(/Users/abdurrehman/Desktop/Mp3Player/logos/pauseButton.png);
            background-position: center;  
            background-repeat: no-repeat;
            background-color: transparent;
            border: 1px solid black;
            ''')
        
        
        if self.flag %2 == 0: 
            mixer.music.stop()
            self.b1.setStyleSheet('''
            background-image: url('/Users/abdurrehman/Desktop/Mp3Player/logos/stopButton.png');
            background-position: center;  
            background-repeat: no-repeat;
            background-color: transparent;
            border: 1px solid black;
            
            ''')
        
        
    def nextt(self):
        if len(self.filesList)-1 == self.count:
            self.count = 0 
           
            # self.start()
            mixer.music.load(self.filesList[self.count])
            mixer.music.play()
            self.logoImg.setPixmap(QPixmap(self.images[self.imCount]))
            self.imCount +=1
        if len(self.images)-1 == self.imCount:
            self.imCount = 0    
        else: 
            print("Next")
            self.count +=1
            
            # self.start()
            mixer.music.load(self.filesList[self.count])
            mixer.music.play()
            self.logoImg.setPixmap(QPixmap(self.images[self.imCount]))
            self.imCount+=1
    def loop(self):
        mixer.music.load(self.filesList[self.count])
        mixer.music.play(-1)

    def incVolume(self):
        
        mixer.music.set_volume(self.volume)
        self.volume += 0.1
    def decVolume(self):
        
        mixer.music.set_volume(self.volume)
        self.volume -= 0.1 
# def window():
#     app = QApplication(sys.argv)
#     win = Test()
#     win.show()
#     sys.exit(app.exec_())
# window()
