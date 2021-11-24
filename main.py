import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('tt.ui', self)
        self.pushbutton.clicked.connect(self.run)
        self.shape = 1
        #self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            print(self.coords)
            x, y = self.coords
            colors = (randint(0, 255) for i in range(3))
            qp.setBrush(QColor(*colors))
            if self.shape == 1:
                w = randint(10, 100)
                qp.drawEllipse(x - w // 2, y - w // 2, w, w)

    def run(self, event):
        if event.button() == Qt.LeftButton:
            self.shape = 1

    def mouseMoveEvent(self, event):
        self.coords = [event.x(), event.y()]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())