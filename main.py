import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtCore import Qt, QPointF
from random import randrange
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(610, 536)
        self.btn = QtWidgets.QPushButton(parent=Form)
        self.btn.setGeometry(QtCore.QRect(270, 30, 75, 23))
        self.btn.setObjectName("btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn.setText(_translate("Form", "PushButton"))


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
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(QPointF(200, 200), a, a)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())