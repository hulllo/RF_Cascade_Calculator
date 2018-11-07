#coding = 'utf-8'

import sys
from PyQt5.QtWidgets import (QMainWindow,QTableWidget,QWidget, QPushButton, QApplication, QHBoxLayout, QVBoxLayout)
import about

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Init_UI()
    def Init_UI(self):
        compoundWidget = QWidget()

        table = QTableWidget()
        table.setColumnCount(6)
        table.setRowCount(11)

        layout = QVBoxLayout()
        layout.addWidget(QPushButton("Widget1"))
        layout.addWidget(QPushButton("Widget2"))
        layout.addWidget(table)
        compoundWidget.setLayout(layout)
        self.setCentralWidget(compoundWidget)


        self.setGeometry(300,300,400,300)
        self.setWindowTitle('学点编程吧')


        # hbox = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(bt1)
        # hbox.addWidget(bt2)
        # hbox.addWidget(bt3)

        # vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(hbox)

        # self.setLayout(vbox)

        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())