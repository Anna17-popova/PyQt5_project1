import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtGui import QPainter, QColor
from random import randrange


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ellips.ui", self)
        self.btn.clicked.connect(self.paint)
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellips(qp)
            qp.end()

    def draw_ellips(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        d = randrange(0, 300)
        qp.drawEllipse(randrange(0, 500), randrange(0, 500), d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
