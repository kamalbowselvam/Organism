from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsItem
from PyQt5.QtCore import  QRectF, QPointF, qDebug, Qt, QTimer, QObject

class PlayGroundView(QGraphicsView):
    def __init__(self):
        super(PlayGroundView,self).__init__()