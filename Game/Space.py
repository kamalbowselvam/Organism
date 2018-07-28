from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt, QObject, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent,QMediaPlaylist
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtGui import QBrush, QImage
from Grounds.PlayGround import PlayGround
from Grounds.PlayGroundView import PlayGroundView
from Players.Enemy import Enemy
from Players.Player import Player

import resoruces


class Game(QObject):

    def __init__(self):
        super(Game,self).__init__()
        self.scene = PlayGround()
        self.scene.setBackgroundBrush(QBrush(QImage(":/Resources/images/BackGround.png")))
        self.view = PlayGroundView()
        self.view.setScene(self.scene)
        self.player = Player()
        self.addToGround(self.player)
        self.backgroundMusic = QMediaPlayer()
        self.playList = QMediaPlaylist()
        self.playList.addMedia(QMediaContent(QUrl("qrc:/Resources/sounds/Game_Background.mp3")))
        self.playList.setPlaybackMode(QMediaPlaylist.Loop)

        self.backgroundMusic.setPlaylist(self.playList)
        self.backgroundMusic.setVolume(2)
        self.backgroundMusic.play()


        self.changeFocus(self.player)
        self.gameObjectPosition(self.player,750/2,550)
        self.setSize()

        self.spawnEnemies()

    def setSize(self):
        self.view.setFixedSize(800, 600)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)


    def addToGround(self,item):
        self.scene.addItem(item)

    def changeFocus(self,item):
        item.setFlag(QGraphicsItem.ItemIsFocusable)
        item.setFocus()


    def playMusic(self):
        pass

    def gameObjectPosition(self,item,x,y):
        item.setPos(x,y)

    def spawnEnemies(self):
        self.enemyTimer = QTimer()
        self.enemyTimer.timeout.connect(lambda: self.launchEnemies())
        self.enemyTimer.start(5000)

    def launchEnemies(self):
        enemy = Enemy()
        self.scene.addItem(enemy)

    def start(self):
        self.view.show()


