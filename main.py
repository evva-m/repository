import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtCore import Qt, QPointF
from random import randrange
from UI import Ui_Form


class Suprematism(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            a = randrange(20, 100)
            qp.setBrush(QColor(randrange(0, 256), randrange(0, 256), randrange(0, 256)))
            qp.drawEllipse(QPointF(200, 200), a, a)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
