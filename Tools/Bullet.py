
import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsItem
from PyQt5.QtCore import  QRectF, QPointF, qDebug, Qt, QTimer, QObject
from Players.Enemy import Enemy


class Bullet(QGraphicsRectItem):
    value = 0

    def __init__(self):
        super(Bullet,self).__init__()
        self.setRect(0,0,5,25)
        self.timer = QTimer()
        self.timer.timeout.connect(lambda:  self.move())
        self.timer.start(50)
        Bullet.value +=  1
        self.bulletCouter()


    def move(self):

        collidingItems = self.collidingItems()
        for item in collidingItems:
            if isinstance(item,Enemy):

                self.scene().increaseScore()
                self.scene().removeItem(item)
                self.scene().removeItem(self)
                item.timer = None                           #Setting the enemy QTimer to None (To clear the Reference)
                del item
                self.timer = None                           #Setting the Bullet Qtimer to None (To clear of the Reference)
                del self
                return

        self.setPos(self.x(),self.y()-10)
        if (self.pos().y() < 20):
            self.timer = None
            self.scene().removeItem(self)
            del self

    def bulletCouter(self):
        print("Number of Bullet Launched =" + str(Bullet.value))


    def __del__(self):
        Bullet.value -= 1
        print("Bullet deleted")