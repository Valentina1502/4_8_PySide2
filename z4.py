#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random
from PySide2.QtCore import Qt, QPoint
from PySide2.QtGui import QPainter, QBrush, QPen, QPolygon
from PySide2.QtWidgets import QApplication, QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Рисунок")
        self.setGeometry(150, 50, 600, 550)


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(Qt.cyan))
        painter.drawRect(0, 0, 600, 500)
        painter.setPen(QPen(Qt.darkGreen))
        painter.setBrush(QBrush(Qt.darkGreen))
        painter.drawRect(0, 420, 600, 130)

        painter.setPen(QPen(Qt.darkRed, 2, Qt.SolidLine))
        painter.setBrush(Qt.gray)
        painter.drawRect(35, 186, 278, 268)
        painter.setPen(QPen(Qt.darkRed, 3, Qt.SolidLine))
        painter.setBrush((QBrush(Qt.darkCyan)))
        painter.drawRect(68, 209, 86, 81)
        painter.drawRect(194, 209, 86, 81)
        painter.setBrush((QBrush(Qt.darkRed)))
        painter.drawRect(130, 318, 86, 135)
        painter.setBrush((QBrush(Qt.darkMagenta)))
        points = QPolygon([
            QPoint(11, 186),
            QPoint(174, 29),
            QPoint(335,186)
        ])
        painter.drawPolygon(points)
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        painter.setPen(QPen(Qt.yellow, 3, Qt.SolidLine))
        painter.drawEllipse(473, 17, 80, 80)
        painter.drawLine(459, 35, 392, 21)
        painter.drawLine(484, 97, 444, 149)
        painter.drawLine(540, 107, 578, 178)
        painter.drawLine(463, 66, 428, 85)
        painter.drawLine(511, 112, 510, 148)
        self.drawGrass(painter)
        self.drawCat(painter)


    def drawGrass(self, painter):
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.green, 2, Qt.SolidLine))
        painter.setBrush(Qt.green)
        for i in range(30):
            painter.drawArc(random.randint(1, 8), 300, i * 20, 430, 0 * 200, random.randint(15, 45) * 10)


    def drawCat(self, painter):
        painter.begin(self)
        points1 = QPolygon([
            QPoint(360, 338),
            QPoint(403, 296),
            QPoint(403, 327),
            QPoint(433, 327),
            QPoint(433, 296),
            QPoint(474, 337),
            QPoint(439, 313),
            QPoint(439, 388),
            QPoint(397, 388),
            QPoint(397, 312)
        ])
        points2 = QPolygon([
            QPoint(399, 405),
            QPoint(385, 405),
            QPoint(385, 431),
            QPoint(375, 431),
            QPoint(375, 445),
            QPoint(399, 445)
        ])
        points3 = QPolygon([
            QPoint(437, 405),
            QPoint(452, 405),
            QPoint(452, 431),
            QPoint(463, 431),
            QPoint(463, 445),
            QPoint(437, 445)
        ])
        painter.setPen(QPen(Qt.black))
        painter.setBrush(QBrush(Qt.darkGray))
        painter.drawPolygon(points1)
        painter.drawPolygon(points2)
        painter.drawPolygon(points3)
        painter.drawRect(399, 388, 38, 55)
        painter.drawRect(395, 436, 23, 15)
        painter.drawRect(418, 436, 23, 15)
        painter.drawLine(378, 437, 378, 444)
        painter.drawLine(403, 444, 403, 451)
        painter.drawLine(433, 444, 433, 451)
        painter.drawLine(455, 437, 455, 444)
        painter.setPen(QPen(Qt.red))
        painter.setBrush(QBrush(Qt.darkRed))
        painter.drawRect(412, 388, 13, 23)
        painter.drawLine(418, 389, 418, 399)
        painter.drawEllipse(406, 359, 25, 20)
        painter.setPen(QPen(Qt.black))
        painter.setBrush(QBrush(Qt.white))
        painter.drawEllipse(388, 336, 22, 20)
        painter.drawEllipse(424, 336, 22, 20)
        painter.setPen(QPen(Qt.black))
        painter.setBrush(QBrush(Qt.black))
        painter.drawEllipse(398, 343, 6, 6)
        painter.drawEllipse(430, 343, 6, 6)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    