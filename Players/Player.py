from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsRectItem, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap



from Tools.Bullet import Bullet


class Player(QGraphicsPixmapItem):

    def __init__(self):
        super(Player,self).__init__()
#        self.setRect(0,0,50,50)
        self.setPixmap(QPixmap(":/Resources/images/Spaceship.png"))
        self.setScale(0.2)




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
            bullet.setPos(self.x()+12.5,self.y())
            self.scene().addItem(bullet)




