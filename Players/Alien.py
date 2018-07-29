
from PyQt5.QtWidgets import  QGraphicsRectItem, QGraphicsPixmapItem
from PyQt5.QtCore import  QTimer, QPointF,QLineF
from PyQt5.QtGui import QPixmap
import random
import numpy as np

class Alien(QGraphicsPixmapItem):
    STEP_SIZE = 3
    value = 0

    def __init__(self):
        super(Alien,self).__init__()
        self.setPixmap(QPixmap(":/Resources/images/Aliens.png"))
#        self.setScale(0.5)
        self.setTransformOriginPoint(50,50)
        self.directionPoints = [QPointF(200,200),QPointF(400,200)]
        self.point_index=0
        self.currentDestination = self.directionPoints[self.point_index]
        self.rotateToPoint(self.currentDestination)

        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.move_forward())
        self.timer.start(150)


    def move_forward(self):

        distance_line = QLineF(self.pos(),self.currentDestination)
        if(distance_line.length() < 5):
            self.point_index+=1
            if (self.point_index >= len(self.directionPoints)):
                return
            self.currentDestination = self.directionPoints[self.point_index]
            self.rotateToPoint(self.currentDestination)

        theta = self.rotation()
        dy = Alien.STEP_SIZE * np.sin(np.radians(theta))
        dx = Alien.STEP_SIZE * np.cos(np.radians(theta))
        self.setPos(self.x() + dx, self.y() + dy)

    def rotateToPoint(self,point):
        track_line = QLineF(self.pos(),point)
        self.setRotation(-1 * track_line.angle())
