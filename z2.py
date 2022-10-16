#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PySide2.QtWidgets import QApplication, QWidget, \
    QVBoxLayout,  QLineEdit, QListWidget
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # вызываем конструктор базового класса
        self.list =QListWidget()
        self.list.itemDoubleClicked.connect(self.in_line)
        self.line = QLineEdit()
        self.line.returnPressed.connect(self.in_list)
        self.initialize_ui()
        

    def initialize_ui(self):
        self.setGeometry(110, 100, 200, 300)
        self.setWindowTitle("Работа с текстом")
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.line)
        v_layout.addWidget(self.list)
        self.setLayout(v_layout)
        self.show()
    

    def in_list(self):
        self.list.addItem(self.line.text())
        self.line.clear()


    def in_line(self):
        listItems = self.list.selectedItems()
        for item in listItems:
            self.line.setText(item.text())

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
