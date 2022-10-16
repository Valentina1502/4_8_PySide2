#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QWidget, QApplication
from PySide2.QtCore import QPropertyAnimation, QPoint


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(450, 450)
        self.setWindowTitle("Анимация")
        self.boll = QWidget(self)
        self.boll.setStyleSheet(
            "background-color: purple;\
            border-radius: 25%;"
            )
        self.boll.resize(50, 50)
        self.anim = QPropertyAnimation(self.boll, b"pos")
        self.anim.setDuration(1500)


    def mousePressEvent(self, event):
        self.anim.setEndValue(QPoint(event.x(), event.y()))
        self.anim.start()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
