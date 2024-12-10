import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtCore import Qt, QPointF
from random import randrange
from PyQt6 import uic
import io


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>610</width>
    <height>536</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="btn">
   <property name="geometry">
    <rect>
     <x>270</x>
     <y>30</y>
     <width>75</width>
     <height>23</height>
    </rect>
   </property>
   <property name="text">
    <string>PushButton</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
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