from PyQt5.QtCore import QPointF, QLineF, Qt, QTimer
from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsPolygonItem, QGraphicsScene, QGraphicsView, QApplication, QGraphicsLineItem
from PyQt5.QtGui import QPixmap, QPolygonF, QBrush, QPen
from Tools.Arrow import Arrow
from Players.Enemy import Enemy
import sys

class Tower(QGraphicsPixmapItem):

    SCALE_FACTOR = 300

    def __init__(self,parent=None):
        super(Tower,self).__init__(parent)
        self.setPixmap(QPixmap(':/Resources/images/Tower.png'))
        self.setScale(0.5)
        self.points = [QPointF(1,0),QPointF(2,0),QPointF(3,1),QPointF(3,2),QPointF(2,3),QPointF(1,3),QPointF(0,2),QPointF(0,1)]
        for point in self.points:
            point.setX(point.x()*Tower.SCALE_FACTOR)
            point.setY(point.y()*Tower.SCALE_FACTOR)

        self.polygon = QPolygonF(self.points)
        self.border = QGraphicsPolygonItem(self.polygon,self)
#        self.border.setPen(QPen(Qt.red))

        self.border.setScale(0.5)

        self.border.setPen(QPen(Qt.DashLine))
        self.poly_center = QPointF(1.5,1.5)
        self.poly_center *= Tower.SCALE_FACTOR


        self.poly_center = self.mapToScene(self.poly_center)
        self.tower_center = QPointF(self.x()+50,self.y()+50)
        self.line = QLineF(self.poly_center, self.tower_center)
        self.border.setPos(self.border.x()+self.line.dx(), self.border.y()+self.line.dy())

#        self.attack_destination = QPointF(800,0)

        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.accquire_target())
        self.timer.start(1000)

    def fire(self):
        arrow = Arrow()
        arrow.setPos(self.x(),self.y())
        attack_line = QLineF(QPointF(self.x()+25,self.y()+25), self.attack_destination)
        line = QGraphicsLineItem(attack_line)
        line.setPen(QPen(Qt.blue))
 #       self.scene().addItem(line)
        attack_angle = -1 * attack_line.angle()   # Multiplied by -1 because the angle is given in counter clockwise direction
        arrow.setRotation(attack_angle)
        self.scene().addItem(arrow)

    def distance_to(self,item):

        distance = QLineF(QPointF(self.pos().x()+25, self.pos().y()+25),item.pos())
        line = QGraphicsLineItem(distance)
        line.setPen(QPen(Qt.red))
#        self.scene().addItem(line)
        return distance.length()



    def accquire_target(self):

        attack_item = self.border.collidingItems()

        if (len(attack_item) == 1):
            self.has_target = False
            return

        closet_distance = 300
        closet_pt = QPointF(0,0)

        for item in attack_item:
            if isinstance(item,Enemy):
                distance = self.distance_to(item)
                if (distance < closet_distance):
                    closet_distance = distance
                    closet_pt = QPointF(item.pos().x()+50, item.pos().y()+50)
                    self.has_target = True

                self.attack_destination = closet_pt
                self.fire()

