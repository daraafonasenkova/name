import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('tt.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.shape = 1
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            x = randint(10, 400)
            y = randint(10, 400)
            colors = (255, 255, 0)
            qp.setBrush(QColor(*colors))
            if self.shape == 1:
                w = randint(10, 100)
                qp.drawEllipse(x - w // 2, y - w // 2, w, w)
            qp.end()

    def run(self):
        self.shape = 1
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())