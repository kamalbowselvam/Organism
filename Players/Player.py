from PyQt5.QtWidgets import QGraphicsRectItem
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsRectItem

from Tools.Bullet import Bullet


class Player(QGraphicsRectItem):

    def __init__(self):
        super(Player,self).__init__()
        self.setRect(0,0,50,50)

    def keyPressEvent(self, QKeyEvent):
        if (QKeyEvent.key() ==  Qt.Key_Right):
            if (self.pos().x() +100 < 800):
                self.setPos(self.x() + 10, self.y())

        if(QKeyEvent.key() ==  Qt.Key_Left):
            if (self.pos().x() + 100 > 100):
                self.setPos(self.x() - 10, self.y())

        if (QKeyEvent.key() == Qt.Key_Up):
            if (self.pos().y() + 100 > 100):
                self.setPos(self.x(), self.y()-10)

        if (QKeyEvent.key() == Qt.Key_Down):
            if (self.pos().y() + 100 < 600):
                self.setPos(self.x(), self.y()+10)

        if (QKeyEvent.key() ==  Qt.Key_Space):
            bullet = Bullet()
            bullet.setPos(self.x(),self.y())
            self.scene().addItem(bullet)
