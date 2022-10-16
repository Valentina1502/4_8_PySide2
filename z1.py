#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PySide2.QtWidgets import QApplication, QWidget, QPushButton,\
    QAbstractItemView, QVBoxLayout, QHBoxLayout, QListWidget
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()  # вызываем конструктор базового класса
        self.list1 = QListWidget()
        self.list1.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list1.addItems(products)
        self.button1 = QPushButton("Добавить", self)
        self.button2 = QPushButton("Убрать", self)
        self.list2 = QListWidget()
        self.list2.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.initialize_ui()
        


    def initialize_ui(self):
        self.setGeometry(110, 100, 400, 200)
        self.setWindowTitle("Покупки")
        self.button1.setStyleSheet("background: #B9F73E")
        self.button2.setStyleSheet("background: #FF7373")
        self.button1.clicked.connect(self.add_product)
        self.button2.clicked.connect(self.delete_product)

        self.show()
    

    def add_product(self):
        listItems = self.list1.selectedItems()
        for item in listItems:
            self.list1.takeItem(self.list1.row(item))
            self.list2.addItem(item)


    def delete_product(self):
        listItems = self.list2.selectedItems()
        for item in listItems:
            self.list2.takeItem(self.list2.row(item))
            self.list1.addItem(item)


    def align(self):
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        hbox.addWidget(self.list1)
        hbox.addLayout(vbox)
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        hbox.addWidget(self.list2)
        self.setLayout(hbox)


if __name__ == '__main__':
    products = ["Хлеб", "Молоко", "Чай", "Картошка", "Яйца",\
        "Яблоки", "Масло", "Помидоры", "Шоколад", "Печенье"]
    products.sort()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.align()
    sys.exit(app.exec_())
