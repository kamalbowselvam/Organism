from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsItem
from PyQt5.QtCore import  QRectF, QPointF, qDebug, Qt, QTimer, QObject
from Tools.Score import Score
from  Tools.Health import Health


class PlayGround(QGraphicsScene):

    def __init__(self):
        super(PlayGround,self).__init__()
        self.setSceneRect(0,0,800,600)
        self.score = Score()
        self.addItem(self.score)

        self.health = Health()
        self.addItem(self.health)

        self.health.setPos(0,self.health.pos().y()+25)

    def increaseScore(self):

        self.score.increase()

    def decreaseHealth(self):
        self.health.decrease()