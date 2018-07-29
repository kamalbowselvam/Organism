from PyQt5.QtWidgets import  QGraphicsView
from Tools.Arrow import Arrow


class PlayGroundView(QGraphicsView):
    def __init__(self):
        super(PlayGroundView,self).__init__()



    def mousePressEvent(self, QMouseEvent):

        arrow = Arrow()
        arrow.setPos(QMouseEvent.pos())
        arrow.setRotation(40)
        self.scene().addItem(arrow)
