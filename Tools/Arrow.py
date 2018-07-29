
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtCore import QTimer, QUrl
from Players.Enemy import Enemy
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
import numpy as np

class Arrow(QGraphicsPixmapItem):
    STEP_SIZE = 30
    value = 0

    def __init__(self):
        super(Arrow,self).__init__()
        self.setPixmap(QPixmap(":/Resources/images/Arrow.png"))
        self.setScale(0.05)
        self.setTransformOriginPoint(12.8,12.8)
        self.timer = QTimer()
        self.timer.timeout.connect(lambda:  self.move())
        self.timer.start(50)

        self.bulletSound = QMediaPlayer()
        self.bulletSound.setMedia(QMediaContent(QUrl("qrc:/Resources/sounds/Bullet.mp3")))
        self.bulletSound.setVolume(10)
        self.bulletSound.play()

        Arrow.value +=  1
        self.arrowCouter()


    def move(self):

        theta = self.rotation()
        dy = Arrow.STEP_SIZE * np.sin(np.radians(theta))
        dx = Arrow.STEP_SIZE * np.cos(np.radians(theta))
        self.setPos(self.x()+dx,self.y()+dy)

    def arrowCouter(self):
        print("Number of Bullet Launched =" + str(Arrow.value))


    def __del__(self):
        Arrow.value -= 1
        print("Bullet deleted")