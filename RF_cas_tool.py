import math
import pickle
import sqlite3
import sys
import time
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QComboBox, QFileDialog,
                             QMainWindow, QPushButton, QTableWidget,
                             QTableWidgetItem, QVBoxLayout, QWidget, qApp)

import about


class MyTable(QMainWindow):

    def __init__(self):
        super().__init__()

        self.conn = sqlite3.connect('test.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("select type from component")
        self.types = self.cursor.fetchall()
        self.types = [x[0] for x in set(self.types)]
        self.init_ui()
        self.init_menubar()

    def init_ui(self, colc = 5):
        self.colc = colc
        self.setGeometry(200, 100, 900, 600)
        self.setWindowTitle('RF_cas_cal tool')

        compound_widget = QWidget()
        self.table1 = QTableWidget()
        self.table2 = QTableWidget()
        # self.table2.resize(50,50)  #设置表格尺寸
        # ===1:创建初始表格
        # self.colc = 5
        self.table1.setColumnCount(self.colc)
        self.table1.setRowCount(9)
        # self.table1.setStyleSheet()
        self.table2.setColumnCount(6)
        self.table2.setRowCount(4)
        # self.setShowGrid(False) #是否需要显示网格

        # hbox = QHBoxLayout()
        # hbox.addWidget(self.table2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.table1)
        # vbox.addStretch(1)
        vbox.addWidget(self.table2)
        vbox.setStretchFactor(self.table1, 2)
        vbox.setStretchFactor(self.table2, 1)
        compound_widget.setLayout(vbox)
        self.setCentralWidget(compound_widget)

        self.settableHeader()
        self.inputrow_class(self.colc)
        self.inputrow_model(self.colc)
        self.inputrow_frq(self.colc)
        self.inputrow4_5(self.colc)
        self.inputrow7_8(self.colc)
        self.inputrow9()
        self.inputrow10(self.colc)
        self.editsheet_label()
        self.editsheet_value_class()
        self.editsheet_value_model()
        self.editsheet_value_frq()
        self.editsheet_value_gain_nf()
        self.buttun_edit()
        self.settableHeaderVisible()
        # self.settableHeaderFontColor()
        # self.setCellFontColor()
        # self.setCellAlign()
        # self.setCellFontSize()
        # self.setCellFontColor()
        # self.setCellSpan()

        # layout = QHBoxLayout()
        # layout.addWidget(MyTable)
        # self.setLayout(layout)

        
        self.table1.itemChanged.connect(self.table1_item_textchanged)
        self.table2.itemChanged.connect(self.table2_item_textchanged)

    def init_menubar(self):

        #退出Action设置
        exit_action = QAction(
        QIcon('F:\\Python\\PyQt5\\MenusAndToolbar\\images\\exit.png'), '&退出', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('退出应用程序')
        exit_action.triggered.connect(qApp.quit)

        # 载入配置Action设置
        open_file_action = QAction(QIcon('2.png'), '&载入配置', self)
        open_file_action.setShortcut('ctrl+O')
        open_file_action.setStatusTip('载入配置')
        open_file_action.triggered.connect(self.fun_open_file)
        self.statusBar()
        # 保存配置Action设置
        save_file_action = QAction(QIcon('2.png'), '&保存配置', self)
        save_file_action.setShortcut('ctrl+S')
        save_file_action.setStatusTip('保存配置')
        save_file_action.triggered.connect(self.fun_save_file)
        self.statusBar()
        # 关于Action设置
        about_action = QAction(QIcon('2.png'), '&关于', self)
        # AboutAction.setShortcut('ctrl+S')
        about_action.setStatusTip('关于')
        about_action.triggered.connect(self.funabout)
        self.statusBar()

        # 图示Action设置
        graphics_view_action = QAction(QIcon('2.png'), '&图示', self)
        graphics_view_action.setStatusTip('图示')
        graphics_view_action.triggered.connect(self.graphics_view)
        self.statusBar()

        # menuBar设置
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&文件')
        file_menu.addAction(open_file_action)
        file_menu.addAction(save_file_action)
        file_menu.addAction(exit_action)
        file_menu = menubar.addMenu('&视图')
        file_menu.addAction(graphics_view_action)
        file_menu = menubar.addMenu('&帮助')
        file_menu.addAction(about_action)

    def graphics_view(self):
        datas = []
        for col in range(self.colc):
            data = self.table1.item(7,col).text()
            datas.append(float(data))
        x = list(range(self.colc))
        plt.plot(x,datas,'-o')  
        plt.show()  
        pass
    def fun_open_file(self):
        fname = QFileDialog.getOpenFileName(
            self, '载入配置', 'untitled.ca', '*.ca')
        if fname[0]:
            with open(fname[0], 'rb') as file:
                data = pickle.load(file)
            self.colc = int(len(data[:-3])/5)
            self.init_ui(self.colc)
            self.load_data(self.colc,data)

        self.statusBar().showMessage('载入成功')

    def fun_save_file(self):
        data = self.savedata()   
        fname = QFileDialog.getSaveFileName(self, '保存配置', 'untitled', '*.ca')
        if fname[0] == '':
            return False
        with open(fname[0], 'wb') as file:
            pickle.dump(data, file, -1)
        self.statusBar().showMessage('保存成功')

    def funabout(self):
        self.about1 = about.about()
        self.about1.show()

    def is_num(self, str_):
        try:
            float(str_)
            return True
        except:
            return False
    # 表格文字变化处理函数

    def savedata(self):
        save_items = []
        #保存当前数据
        for col in range(self.colc):
            for row in range(3):
                save_item = self.table1.cellWidget(row, col).currentText()
                save_items.append(save_item)
            for row in range(4, 6):
                save_item = self.table1.item(row, col).text()
                save_items.append(save_item)

        save_setting = [self.table2.item(1,x).text() for x in range(3)]
        # print(save_setting)
        return save_items+save_setting

    def table1_item_textchanged(self, item):
        row = item.row()
        item_text = item.text()
        if row == 4 or row == 5:
            if self.is_num(item_text):
                self.inputrow7_8(self.colc)
                self.inputrow10(self.colc)

    def table2_item_textchanged(self, item):
        item_text = item.text()
        if item.column() == 4:
            data = self.savedata()
            if self.is_num(item.text()):
                self.colc = int(item.text())   #设置级数
                self.init_ui(self.colc)
                self.load_data(self.colc,data)
            else:
                return False


        elif item.column() != 3:
            if self.is_num(item_text):
                self.inputrow10(self.colc)

    def load_data(self,col,data):
        save_items= data[:-3]
        # print(save_items)
        save_setting = data[-3:] 
        n = 0
        for col in range(col):
            for row in range(3):
                index = self.table1.cellWidget(row, col).findText(
                    save_items[n])  # 查找还原的数据是否在列表里
                if index != -1:
                    self.table1.cellWidget(row, col).setCurrentIndex(
                        index)  # 如果存在，则显示当前的数据
                else:
                    self.table1.cellWidget(row, col).insertItem(
                        10000, save_items[n])  # 否则，将数据添加到最后一行
                    maxCount = self.table1.cellWidget(row, col).count() #获取有多少行
                    self.table1.cellWidget(
                        row, col).setCurrentIndex(maxCount-1)  #显示最后一行
                n = n + 1
            for row in range(4, 6):
                #  增加还原第4，5行数据
                self.table1.setItem(row, col, QTableWidgetItem(str(save_items[n])))
                n = n + 1
        # 级数增大,列数超过了保存数据个数
            try: 
                save_items[n]
            except IndexError :
                break
        # 还原温度，带宽等信息
        for index, col in enumerate(range(3)):
            self.table2.setItem(1,col,QTableWidgetItem(str(save_setting[index])))

    # ===1:设置表格单元格尺寸
    def settableSize(self):
        """
    5  首先，可以指定某个行或者列的大小
        self.MyTable.setColumnWidth(2,50)  #将第2列的单元格，设置成50宽度
        self.MyTable.setRowHeight(2,60)      #将第2行的单元格，设置成60的高度
        还可以将行和列的大小设为与内容相匹配
        self.MyTable.resizeColumnsToContents()   #将列调整到跟内容大小相匹配
        self.MyTable.resizeRowsToContents()      #将行大小调整到跟内容的大学相匹配
        :return:
        """
        self.setColumnWidth(0, 50)
        self.setColumnWidth(3, 50)
        # self.setRowHeight(0,500)
        # 1.2 设置表格的行和列的大小与输入内容相匹配
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
    # ===2：设置表格的表头名称

    def settableHeader(self):
        #columnname = ['A','B','C','D','E']
        columnname = [str(x+1) for x in range(self.colc)]
        rowname = ['类型', '型号', '频率', '-', '增益',
                   '噪声', '-', 'Σ 增益', 'Σ 噪声', '-', '-']
        self.table1.setHorizontalHeaderLabels(columnname)
        self.table1.setVerticalHeaderLabels(rowname)
    # ===3:给表格输入初始化数据

    def settableInitData(self):
        for i in range(self.colc):
            for j in range(self.colc):
                # 1)直接在表格中添加数据
                self.table1.setItem(i, j, QTableWidgetItem(str(i)+str(j)))

                # 2）在表格的单元格中加入控件
                self.comBox = QComboBox()
                self.comBox.addItem("男")
                self.comBox.addItem("女")
                self.setCellWidget(i, j, self.comBox)

    def inputrow_class(self, n):
        for i in range(n):
            self.comBox = QComboBox()
            self.comBox.setEditable(True)
            self.comBox.addItems(sorted(self.types))
            self.comBox.setProperty('row', 0)
            self.comBox.setProperty('col', i)
            self.table1.setCellWidget(0, i, self.comBox)
            self.comBox.currentTextChanged.connect(
                self.Combo_textchanged)

    def inputrow_model(self, n, index=None):
        for i in range(n):  # 如果变化的数据是某一列，只更新该列数据
            if index:
                if i != index:
                    continue
            current_value = self.table1.cellWidget(0, i).currentText()
            self.cursor.execute(
                "select model from component where type=?", (current_value,))
            self.models = self.cursor.fetchall()
            self.models = [x[0] for x in set(self.models)]
            self.comBox = QComboBox()
            self.comBox.setEditable(True)
            self.comBox.addItems(sorted(self.models))
            self.comBox.setProperty('row', 1)
            self.comBox.setProperty('col', i)
            self.table1.setCellWidget(1, i, self.comBox)
            self.comBox.currentTextChanged.connect(
                self.Combo_textchanged)

    def inputrow_frq(self, n, index=None):
        for i in range(n):
            if index:
                if i != index:
                    # print(index)
                    continue
            current_type = self.table1.cellWidget(0, i).currentText()
            current_model = self.table1.cellWidget(1, i).currentText()
            self.cursor.execute(
                "select frq from component where type=? and model =?", (current_type, current_model))
            self.frq = self.cursor.fetchall()
            self.frq = [x[0] for x in set(self.frq)]
            self.comBox = QComboBox()
            self.comBox.setEditable(True)
            self.comBox.addItems(self.frq)
            self.comBox.setProperty('row', 2)
            self.comBox.setProperty('col', i)
            self.table1.setCellWidget(2, i, self.comBox)
            self.comBox.currentTextChanged.connect(
                self.Combo_textchanged)

            # 初始化3，4行
    def inputrow4_5(self, n, index=None):
        for i in range(n):
            if index:
                if i != index:
                    continue
            current_type = self.table1.cellWidget(0, i).currentText()
            current_model = self.table1.cellWidget(1, i).currentText()
            current_frq = self.table1.cellWidget(2, i).currentText()
            self.cursor.execute("select gain from component where type=? and model =? and frq =?", (
                current_type, current_model, current_frq))
            self.gain = self.cursor.fetchall()
            if self.gain == []:
                self.table1.setItem(4, i, QTableWidgetItem(str(0)))
                self.table1.setItem(5, i, QTableWidgetItem(str(0)))
                continue
            self.gain = self.gain[0][0]
            self.cursor.execute("select nf from component where type=? and model =? and frq =?", (
                current_type, current_model, current_frq))
            self.nf = self.cursor.fetchall()[0][0]
            self.table1.setItem(4, i, QTableWidgetItem(str(self.gain)))
            self.table1.setItem(5, i, QTableWidgetItem(str(self.nf)))

    def inputrow7_8(self, n):
        for i in range(n):
            if i == 0:
                totalgain = self.table1.item(4, 0).text()
                totalnf = self.table1.item(5, 0).text()
            else:
                if self.table1.item(7, i-1).text() == '[]':
                    return False
                totalgain = float(self.table1.item(4, i).text()) + \
                    float(self.table1.item(7, i-1).text())
                totalgain = round(totalgain, 1)
                totalnf = 10*math.log10(10**(float(self.table1.item(8, i-1).text())/10)+(10**(float(
                    self.table1.item(5, i).text())/10)-1)/10**(float(self.table1.item(7, i-1).text())/10))
                totalnf = round(totalnf, 1)
                
            self.table1.setItem(7, i, QTableWidgetItem(str(totalgain)))
            self.table1.item(7, i).setFlags(Qt.ItemIsEnabled)
            self.table1.setItem(8, i, QTableWidgetItem(str(totalnf)))
            self.table1.item(8, i).setFlags(Qt.ItemIsEnabled)

    def inputrow9(self):
        self.table2.setItem(0, 0, QTableWidgetItem(str('温度(℃)')))
        self.table2.item(0, 0).setFlags(Qt.ItemIsEnabled)
        self.table2.setItem(1, 0, QTableWidgetItem(str('20')))
        self.table2.setItem(0, 1, QTableWidgetItem(str('带宽(MHz)')))
        self.table2.item(0, 1).setFlags(Qt.ItemIsEnabled)
        self.table2.setItem(1, 1, QTableWidgetItem(str('10')))
        self.table2.setItem(0, 2, QTableWidgetItem(str('信噪比(dB)')))
        self.table2.item(0, 2).setFlags(Qt.ItemIsEnabled)
        self.table2.setItem(1, 2, QTableWidgetItem(str('-1')))
        self.table2.setItem(0, 3, QTableWidgetItem(str('灵敏度(dB)')))
        self.table2.item(0, 3).setFlags(Qt.ItemIsEnabled)
        self.table2.setItem(0, 4, QTableWidgetItem(str('级数')))
        self.table2.item(0, 4).setFlags(Qt.ItemIsEnabled)

    def inputrow10(self, n):
        K = 1.3806505*(10**(-20))
        T = float(self.table2.item(1, 0).text()) + 273.15
        BW = float(self.table2.item(1, 1).text()) * 1000000
        NF = float(self.table1.item(8, n-1).text())
        SNR = float(self.table2.item(1, 2).text())
        sens = 10*math.log10(K*T*BW) + NF + SNR
        sens = round(sens, 2)
        self.table2.setItem(1, 3, QTableWidgetItem(str(sens)))
        self.table2.item(1, 3).setFlags(Qt.ItemIsEnabled)

    def editsheet_label(self):
        self.table2.setItem(2, 0, QTableWidgetItem(str('类型')))
        self.table2.item(2, 0).setFlags(Qt.ItemIsEnabled)
        self.table2.setItem(2, 1, QTableWidgetItem(str('型号')))
        self.table2.item(2, 1).setFlags(Qt.ItemIsEnabled)
        self.table2.setItem(2, 2, QTableWidgetItem(str('频率')))
        self.table2.item(2, 2).setFlags(Qt.ItemIsEnabled)
        self.table2.setItem(2, 3, QTableWidgetItem(str('增益')))
        self.table2.item(2, 3).setFlags(Qt.ItemIsEnabled)
        self.table2.setItem(2, 4, QTableWidgetItem(str('噪声')))
        self.table2.item(2, 4).setFlags(Qt.ItemIsEnabled)

    def editsheet_value_class(self):
        comBox = QComboBox()
        comBox.setEditable(True)
        comBox.addItems(sorted(self.types))
        comBox.setProperty('row', 0)
        comBox.setProperty('col', 0)
        self.table2.setCellWidget(3, 0, comBox)
        comBox.currentTextChanged.connect(
            self.editsheet_Combo_textchanged)

    def editsheet_value_model(self):
        current_value = self.table2.cellWidget(3, 0).currentText()  # 获取类型
        self.cursor.execute(
            "select model from component where type=?", (current_value,))
        models = self.cursor.fetchall()
        models = [x[0] for x in set(models)]
        comBox = QComboBox()
        comBox.setEditable(True)
        comBox.addItems(sorted(models))
        comBox.setProperty('row', 3)
        comBox.setProperty('col', 1)
        self.table2.setCellWidget(3, 1, comBox)
        comBox.currentTextChanged.connect(
            self.editsheet_Combo_textchanged)

    def editsheet_value_frq(self):
        current_type = self.table2.cellWidget(3, 0).currentText()
        current_model = self.table2.cellWidget(3, 1).currentText()
        self.cursor.execute(
            "select frq from component where type=? and model =?", (current_type, current_model))
        frq = self.cursor.fetchall()
        frq = [x[0] for x in set(frq)]
        comBox = QComboBox()
        comBox.setEditable(True)
        comBox.addItems(frq)
        comBox.setProperty('row', 3)
        comBox.setProperty('col', 2)
        self.table2.setCellWidget(3, 2, comBox)
        comBox.currentTextChanged.connect(
            self.editsheet_Combo_textchanged)

        # 初始化3，4行
    def editsheet_value_gain_nf(self):
        current_type = self.table2.cellWidget(3, 0).currentText()
        current_model = self.table2.cellWidget(3, 1).currentText()
        current_frq = self.table2.cellWidget(3, 2).currentText()
        self.cursor.execute("select gain from component where type=? and model =? and frq =?",
                            (current_type, current_model, current_frq))
        gain = self.cursor.fetchall()
        if gain == []:
            return False
        gain = gain[0][0]
        self.cursor.execute("select nf from component where type=? and model =? and frq =?",
                            (current_type, current_model, current_frq))
        nf = self.cursor.fetchall()[0][0]
        self.table2.setItem(3, 3, QTableWidgetItem(str(gain)))
        self.table2.setItem(3, 4, QTableWidgetItem(str(nf)))

    def buttun_edit(self):
        butten_del = QPushButton('删除器件')
        butten_add = QPushButton('增加器件')
        self.table2.setCellWidget(3, 5, butten_del)
        self.table2.setCellWidget(2, 5, butten_add)
        butten_del.clicked.connect(self.del_component)
        butten_add.clicked.connect(self.add_component)

    def Combo_textchanged(self):
        combo = self.sender()
        row = combo.property('row')
        col = combo.property('col')
        if row == 0:
            self.inputrow_model(self.colc, col)
            self.inputrow_frq(self.colc, col)
            self.inputrow4_5(self.colc, col)
            self.inputrow7_8(self.colc)
        elif row == 1:
            self.inputrow_frq(self.colc, col)
            self.inputrow4_5(self.colc, col)
            self.inputrow7_8(self.colc)
        elif row == 2:
            self.inputrow4_5(self.colc, col)
            self.inputrow7_8(self.colc)

    def editsheet_Combo_textchanged(self):
        combo = self.sender()
        col = combo.property('col')
        if col == 0:
            self.editsheet_value_model()
            self.editsheet_value_frq()
            if self.editsheet_value_gain_nf():
                return
        elif col == 1:
            self.editsheet_value_frq()
            if self.editsheet_value_gain_nf():
                return
        elif col == 2:
            if self.editsheet_value_gain_nf():
                return

    def del_component(self):
        class_ = self.table2.cellWidget(3, 0).currentText()
        if class_ == '':
            self.statusBar().showMessage('未输入类型！')
            return
        model = self.table2.cellWidget(3, 1).currentText()
        if model == '':
            self.statusBar().showMessage('未输入型号！')
            return
        frq = self.table2.cellWidget(3, 2).currentText()
        if frq == '':
            self.statusBar().showMessage('未输入频率！')
            return
        self.cursor.execute("select * from component")
        db_tupelist = self.cursor.fetchall()
        len_ = str(len(db_tupelist))
        # cur.execute('PRAGMA table_info(component)')
        self.cursor.execute(
            "select * from component where type = '%s' and model = '%s' and frq = '%s'" % (class_, model, frq))
        data_existed = self.cursor.fetchall()
        if data_existed == []:
            print('不存在该器件')
            self.statusBar().showMessage('不存在该器件')
        else:
            self.cursor.execute(
                "delete from component where type = '%s' and model = '%s' and frq = '%s'" % (class_, model, frq))
            self.cursor.execute(
                "select * from component where type = '%s' and model = '%s' and frq = '%s'" % (class_, model, frq))
            data_existed = self.cursor.fetchall()
            if data_existed == []:
                print('删除成功')
                self.statusBar().showMessage('删除成功')
                self.conn.commit()
                self.editsheet_value_class()
                self.editsheet_value_model()

    def add_component(self):
        class_ = self.table2.cellWidget(3, 0).currentText()
        if class_ == '':
            self.statusBar().showMessage('未输入类型！')
            return
        model = self.table2.cellWidget(3, 1).currentText()
        if model == '':
            self.statusBar().showMessage('未输入型号！')
            return
        frq = self.table2.cellWidget(3, 2).currentText()
        if frq == '':
            self.statusBar().showMessage('未输入频率！')
            return
        gain = self.table2.item(3, 3).text()
        if gain == '':
            self.statusBar().showMessage('未输入增益！')
            return
        elif not self.is_num(gain):
            self.statusBar().showMessage('需输入数字！')
            return
        nf = self.table2.item(3, 4).text()
        if frq == '':
            self.statusBar().showMessage('未输入噪声系数！')
            return
        elif not self.is_num(nf):
            self.statusBar().showMessage('需输入数字！')
            return
        self.cursor.execute("select * from component")
        db_tupelist = self.cursor.fetchall()
        # print(db_tupelist)
        len_ = str(int(db_tupelist[-1][0])+1)
        print(len_)
        # cur.execute('PRAGMA table_info(component)')
        self.cursor.execute(
            "select * from component where type = '%s' and model = '%s' and frq = '%s'" % (class_, model, frq))
        data_existed = self.cursor.fetchall()
        if data_existed:
            print('器件存在:', data_existed)
            self.statusBar().showMessage('器件存在:{0}'.format(data_existed))

        else:
            self.cursor.execute("select * from component")
            self.cursor.execute("insert into component (id, type,model,frq,gain,nf) values ('%s','%s','%s','%s','%f','%f')" % (
                len_, class_, model, frq, float(gain), float(nf)))
            # self.cursor.execute("select * from component")
            self.cursor.execute("select * from component where id = '%s' and type = '%s' and model = '%s' and frq = '%s' and gain = '%f' and nf = '%f'" %
                                (len_, class_, model, frq, float(gain), float(nf)))
            data_existed = self.cursor.fetchall()
            if data_existed != []:
                print(data_existed)
                print('添加成功')
                self.statusBar().showMessage('添加成功')
                self.conn.commit()
                self.editsheet_value_class()
                self.editsheet_value_model()
    """在单元格里加入控件QComboBox"""

    def addwidgettocell(self):
        comBox = QComboBox()
        comBox.addItem("男")
        comBox.addItem("女")
        self.setCellWidget(0, 1, comBox)

    # ===4:表格的其他相关属性设置
    """设置表格是否可编辑"""

    def settableEditTrigger(self):
        """使用格式说明：
                在默认情况下，表格里的字符是可以更改的，
                比如双击一个单元格，就可以修改原来的内容，
                如果想禁止用户的这种操作，让这个表格对用户只读，可以这样：
           QAbstractItemView.NoEditTriggers和QAbstractItemView.EditTrigger枚举中的一个，
           都是触发修改单元格内容的条件：
            QAbstractItemView.NoEditTriggers    0   No editing possible. 不能对表格内容进行修改
            QAbstractItemView.CurrentChanged    1   Editing start whenever current item changes.任何时候都能对单元格修改
            QAbstractItemView.DoubleClicked     2   Editing starts when an item is double clicked.双击单元格
            QAbstractItemView.SelectedClicked   4   Editing starts when clicking on an already selected item.单击已选中的内容
            QAbstractItemView.EditKeyPressed    8   Editing starts when the platform edit key has been pressed over an item.
            QAbstractItemView.AnyKeyPressed     16  Editing starts when any key is pressed over an item.按下任意键就能修改
            QAbstractItemView.AllEditTriggers   31  Editing starts for all above actions.以上条件全包括
        """
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
    """设置表格为整行选择"""

    def settableSelect(self):
        """
        QAbstractItemView.SelectionBehavior枚举还有如下类型
        Constant                      Value        Description
        QAbstractItemView.SelectItems   0   Selecting single items.选中单个单元格
        QAbstractItemView.SelectRows    1   Selecting only rows.选中一行
        QAbstractItemView.SelectColumns 2   Selecting only columns.选中一列
        """
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
    """单个选中和多个选中的设置"""

    def settableSelectMode(self):
        """
        setSelectionMode(QAbstractItemView.ExtendedSelection)  #设置为可以选中多个目标
        该函数的参数还可以是：
        QAbstractItemView.NoSelection      不能选择
        QAbstractItemView.SingleSelection  选中单个目标
        QAbstractItemView.MultiSelection    选中多个目标
        QAbstractItemView.ExtendedSelection和ContiguousSelection
        的区别不明显，要功能是正常情况下是单选，但按下Ctrl或Shift键后，可以多选
        :return:
        """
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
    """表头显示与隐藏"""

    def settableHeaderVisible(self):
        """对于水平或垂直方法的表头，可以用以下方式进行 隐藏/显示 的设置：
        self.MyTable.verticalHeader().setVisible(False)
        self.MyTable.horizontalHeader().setVisible(False)
        """
        # 4.3 隐藏表头
        self.table2.verticalHeader().setVisible(False)
        self.table2.horizontalHeader().setVisible(False)
    """对表头文字的字体、颜色进行设置"""

    def settableHeaderFontColor(self):
        """
        PyQt5中没有如下设置背景颜色和字体颜色函数
        headItem.setBackgroundColor(QColor(c))  # 设置单元格背景颜色
        headItem.setTextColor(QColor(200, 111, 30))  # 设置文字颜色
        :return:
        有（设置字体颜色）：
        headItem.setForeground(QBrush(Qt.red))
        headItem.setForeground(QBrush(QColor(128,255,0)))
        """
        f, ok = QFontDialog.getFont()

        for x in range(self.columnCount()):
            headItem = self.horizontalHeaderItem(x)  # 获得水平方向表头的Item对象
            # headItem.setFont(QFont("song",12,QFont.Bold))
            if ok:
                headItem.setFont(f)  # 设置字体
            # 设置表头字体颜色
            # headItem.setForeground(QBrush(Qt.red))
            headItem.setForeground(QBrush(QColor(128, 255, 0)))

            headItem.setTextAlignment(Qt.AlignLeft)

    def settableproperty(self):
        # 4.2 选中表格中的某一行
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
    """动态插入行列 """

    def addcolColumn(self):
        """当初始的行数或者列数不能满足需要的时候，
        我们需要动态的调整表格的大小，如入动态的插入行：
        insertColumn()动态插入列。
        insertRow(int)、
        insertColumn(int)，指定位置插入行或者列
        """
        colcount = self.colCount()
        self.insertRow(colcount)
    """动态移除行列 """

    def removecolColumn(self):
        """
        removeColumn(int column) 移除column列及其内容。
        removeRow(int row)移除第row行及其内容。
        :return:
        """
        colcount = self.colCount()
        self.removeRow(colcount-1)
    # =========第2部分：对单元格的进行设置=============
    """1.单元格设置字体颜色和背景颜色"""
    """2.设置单元格中的字体和字符大小"""
    """3.设置单元格内文字的对齐方式："""
    """4.合并单元格效果的实现："""
    """5.设置单元格的大小(见settableSize()函数)"""
    """6 单元格Flag的实现"""

    def setCellFontColor(self):
        newItem = self.table1.item(0, 1)
        newItem.setBackground(Qt.red)
        #newItem.setBackground(QColor(0, 250, 10))
        # newItem.(QColor(200, 111, 100))

    def setCellFontSize(self):
        """
        首先，先生成一个字体QFont对象，并将其字体设为宋体，大小设为12，并且加粗
        再利用单元格的QTableWidgetItem类中的setFont加载给特定的单元格。
        如果需要对所有的单元格都使用这种字体，则可以使用
        self.MyTable.setFont(testFont)
        #利用QTableWidget类中的setFont成员函数，将所有的单元格都设成该字体
        :return:
        """
        textFont = QFont("song", 12, QFont.Bold)

        newItem = QTableWidgetItem("张三")
        # newItem.setBackgroundColor(QColor(0,60,10))
        # newItem.setTextColor(QColor(200,111,100))
        newItem.setFont(textFont)
        self.table1.setItem(0, 0, newItem)

    def setCellAlign(self):
        """
        这个比较简单，使用newItem.setTextAlignment()函数即可，
        该函数的参数为单元格内的对齐方式，和字符输入顺序是自左相右还是自右向左。
        水平对齐方式有：
        Constant         Value  Description
        Qt.AlignLeft    0x0001  Aligns with the left edge.
        Qt.AlignRight   0x0002  Aligns with the right edge.
        Qt.AlignHCenter 0x0004  Centers horizontally in the available space.
        Qt.AlignJustify 0x0008  Justifies the text in the available space.
        垂直对齐方式：
        Constant        Value   Description
        Qt.AlignTop     0x0020  Aligns with the top.
        Qt.AlignBottom  0x0040  Aligns with the bottom.
        Qt.AlignVCenter 0x0080  Centers vertically in the available space.
        如果两种都要设置，只要用 Qt.AlignHCenter |  Qt.AlignVCenter 的方式即可
        :return:
        """
        newItem = QTableWidgetItem("张三")
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.table1.setItem(0, 0, newItem)

    def setCellSpan(self):
        """
        self.MyTable.setSpan(0, 0, 3, 1)
        # 其参数为： 要改变单元格的   1行数  2列数
        要合并的  3行数  4列数
        :return:
        """
        self.setSpan(0, 0, 3, 1)

    def update_item_data(self, data):
        """更新内容"""
        self.table1.setItem(0, 0, QTableWidgetItem(data))  # 设置表格内容(行， 列) 文字


class UpdateData(QThread):
    """更新数据类"""
    update_date = pyqtSignal(str)

    def run(self):
        cnt = 0
        while True:
            cnt += 1
            self.update_date.emit(str(cnt))
            time.sleep(1)


if __name__ == '__main__':
    # 实例化表格
    app = QApplication(sys.argv)
    myTable = MyTable()
    # 启动更新线程
    # update_data_thread = UpdateData()
    # update_data_thread.update_date.connect(myTable.update_item_data)  # 链接信号
    # update_data_thread.start()

    # 显示在屏幕中央
    # desktop = QApplication.desktop()  # 获取坐标
    # x = (desktop.width() - myTable.width()) // 2
    # y = (desktop.height() - myTable.height()) // 2
    # myTable.move(x, y)  # 移动

    # 显示表格
    myTable.show()

    app.exit(app.exec_())
