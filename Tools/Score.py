import sys
from PyQt5.QtWidgets import QGraphicsTextItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import random




class Score(QGraphicsTextItem):

    def __init__(self):
        super(Score,self).__init__()

        self.score = 0
        self.setPlainText("Score : " + str(self.score))
        self.setDefaultTextColor(Qt.white)
        self.setFont(QFont("times", 16))



    def increase(self):

        self.score = self.score + 1
        self.setPlainText("Score : " + str(self.score))


    def getScore(self):

        return self.score