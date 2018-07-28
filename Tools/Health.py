from PyQt5.QtWidgets import QGraphicsTextItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont




class Health(QGraphicsTextItem):

    def __init__(self):
        super(Health,self).__init__()

        self.health = 3
        self.setPlainText("Health : " + str(self.health))
        self.setDefaultTextColor(Qt.red)
        self.setFont(QFont("times", 16))



    def decrease(self):

        self.health = self.health - 1
        self.setPlainText("Score : " + str(self.health))


    def getHealth(self):

        return self.health