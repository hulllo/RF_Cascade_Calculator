#coding=utf-8

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu,QPushButton
from PyQt5.QtGui import QIcon
import sys
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()
    def InitUI(self):
        self.statusBar().showMessage('准备就绪')

        self.setGeometry(300,300,400,300)
        # self.setWindowTitle('关注微信公众号：学点编程吧--上下文菜单')
        self.bt = QPushButton('abc')
        self.bt.move(300,300)
        self.show()
    
    def contextMenuEvent(self, event):

       cmenu = QMenu(self)

       newAct = cmenu.addAction("新建")
       opnAct = cmenu.addAction("保存")
       quitAct = cmenu.addAction("退出")
       action = cmenu.exec_(self.mapToGlobal(event.pos()))
       print(event.pos())
       if action == quitAct:
           qApp.quit()
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())