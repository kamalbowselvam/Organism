from PyQt5.QtCore import QPointF, QLineF, Qt
from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsPolygonItem, QGraphicsScene, QGraphicsView, QApplication
from PyQt5.QtGui import QPixmap, QPolygonF, QBrush, QPen
from Tools.Arrow import Arrow
import sys

class Tower(QGraphicsPixmapItem):

    SCALE_FACTOR = 100

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
        self.border.setPen(QPen(Qt.red))
        self.border.setScale(0.5)



        self.border.setPen(QPen(Qt.white))
        self.poly_center = QPointF(1.5,1.5)
        self.poly_center *= Tower.SCALE_FACTOR


        self.poly_center = self.mapToScene(self.poly_center)
        print (self.poly_center)
        self.tower_center = QPointF(self.x()+50,self.y()+50)
        self.line = QLineF(self.poly_center, self.tower_center)
        print(self.border.x())
        print(self.line.dy())
        self.border.setPos(self.border.x()+self.line.dx(), self.border.y()+self.line.dy())
