#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PySide2.QtWidgets import QApplication, QWidget, QLineEdit,\
     QHBoxLayout, QVBoxLayout, QPushButton, QTextEdit
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # вызываем конструктор базового класса
        QApplication.instance().focusChanged.connect(self.on_focus)
        self.line_edit1 = QLineEdit()
        self.line_edit2 = QLineEdit()
        self.line_edit1.returnPressed.connect(self.edit_size)
        self.line_edit2.returnPressed.connect(self.edit_size)
        self.button1 = QPushButton("Изменить размер", self)
        self.textbox = QTextEdit()
        self.initialize_ui()


    def initialize_ui(self):
        self.setGeometry(110, 100, 400, 200)
        self.setWindowTitle("Размеры")
        self.button1.setStyleSheet("background: #B9F73E")
        self.button1.clicked.connect(self.edit_size)
        hlay = QHBoxLayout()
        vlay = QVBoxLayout()
        hlay.addWidget(self.line_edit1)
        hlay.addWidget(self.line_edit2)
        vlay.addLayout(hlay)
        vlay.addWidget(self.button1)
        vlay.addWidget(self.textbox)
        self.setLayout(vlay)
        self.show()
    

    def edit_size(self):
        self.textbox.resize(
            int(self.line_edit1.text()),
            int(self.line_edit2.text())
        )


    def on_focus(self, old, new):
        if self.textbox == new:
            self.textbox.setStyleSheet(f"background-color: #fff;")
        elif self.textbox == old:
            self.textbox.setStyleSheet(f"background-color: #d3d3d3;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
