
import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsItem, QGraphicsPixmapItem
from PyQt5.QtCore import  QRectF, QPointF, qDebug, Qt, QTimer, QObject
from PyQt5.QtGui import QPixmap
import random


class Enemy(QGraphicsPixmapItem):

    value = 0

    def __init__(self):
        super(Enemy,self).__init__()
#        self.setRect(0,0,50,50)
        self.setPixmap(QPixmap(":/Resources/images/Enemy.png"))
        self.setScale(0.2)

        random_number = random.randint(0,600)
        self.setPos(random_number,0)
        self.timer = QTimer()
        self.timer.timeout.connect(lambda:  self.move())
        self.timer.start(50)
        Enemy.value +=  1
        self.enemyCouter()


    def move(self):
        self.setPos(self.x(),self.y()+2)
        if (self.pos().y() > 550):
            self.scene().decreaseHealth()
            self.timer = None
            self.scene().removeItem(self)
            del self

    def enemyCouter(self):
        print("Number of Enemy Launched =" + str(Enemy.value))


    def __del__(self):
        Enemy.value -= 1
        print("Enemy deleted")