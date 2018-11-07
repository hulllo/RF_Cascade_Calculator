#-*- coding:utf-8 -*-
'''
PushButton
'''
__author__ = 'Tony Zhu'

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMenu,QAction
from PyQt5.QtGui import QIcon,QCursor
from PyQt5.QtCore import Qt,QPoint
import sys

class PushButton(QWidget):
    def __init__(self):
        super(PushButton,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("PushButton")
        self.setGeometry(400,400,300,260)

        self.closeButton = QPushButton(self)
        self.closeButton.setText("Close")          #text
        self.closeButton.setIcon(QIcon("close.png")) #icon
        self.closeButton.setShortcut('Ctrl+D')  #shortcut key
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setToolTip("Close the widget") #Tool tip
        self.closeButton.move(100,100)

        self.closeButton.setContextMenuPolicy(Qt.CustomContextMenu)
        self.closeButton.customContextMenuRequested[QPoint].connect(self.myListWidgetContext)

    def myListWidgetContext(self):
        popMenu = QMenu()
        popMenu.addAction(QAction(u'字体放大', self))
        popMenu.addAction(QAction(u'字体减小', self))
        popMenu.triggered[QAction].connect(self.processtrigger)
        popMenu.exec_(QCursor.pos())

    #右键按钮事件
    def processtrigger(self, q):
        # text = self.newTextEdit.toPlainText()
        # if not text.strip():
        #     return
        # 输出那个Qmenu对象被点击
        if q.text() == "字体放大":
            self.fontSize += 1
        elif q.text() == "字体减小":
            self.fontSize -= 1

    # def contextMenuEvent(self, event):

    #    cmenu = QMenu(self)

    #    newAct = cmenu.addAction("新建")
    #    opnAct = cmenu.addAction("保存")
    #    quitAct = cmenu.addAction("退出")
    #    action = cmenu.exec_(self.mapToGlobal(event.pos()))
    #    print(event.pos())
    #    if action == quitAct:
    #        qApp.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PushButton()
    ex.show()
    sys.exit(app.exec_()) 
