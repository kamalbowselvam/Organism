from Grounds.PlayGround import PlayGround
from Grounds.PlayGroundView import PlayGroundView
from Players.Player import Player
from Players.Enemy import Enemy
from PyQt5.QtWidgets import  QGraphicsItem, QGraphicsTextItem
from PyQt5.QtCore import Qt, QObject, QUrl
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtCore import QTimer
from Resources import *



class Game(QObject):

    def __init__(self):
        super(Game,self).__init__()
        self.scene = PlayGround()
        self.view = PlayGroundView()
        self.view.setScene(self.scene)
        self.player = Player()
        self.addToGround(self.player)
        self.backgroundMusic = QMediaPlayer()
        self.backgroundMusic.setMedia(QUrl(":/sounds/Game_Background.mp3"))


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


