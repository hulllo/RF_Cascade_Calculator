from PyQt5.QtWidgets import QWidget,QLabel
class about(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('关于')
        self.resize(200,200)
        self.move(200,200)
        self.lb = QLabel(self)
        self.lb.setText('copyright(c)yuchuang.pan\n版权所有：yuchuang.pan')
