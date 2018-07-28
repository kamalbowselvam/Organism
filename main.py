
import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsItem
from PyQt5.QtCore import  QRectF, QPointF, qDebug, Qt, QTimer, QObject
from Grounds.PlayGround import PlayGround
from Grounds.PlayGroundView import PlayGroundView
from Players.Player import Player
from Game.Space import Game

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Game = Game()
    Game.start()
    app.exec_()
