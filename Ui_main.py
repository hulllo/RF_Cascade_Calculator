# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\python\test_create\test_create.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog  
import math
import sqlite3
stage = 8
global config_data
global data
global type_list
class Ui_Dialog(object): 
    for i in range(stage):#批量生产槽,当更改type,model随着更改
        def1 = '''
def changed_type'''+str(i)+'''(self):
    global flag_
    if flag_ == 1:
        return
    type_now = self.combobox_'''+str(i)+'''.currentText()
    print('type now is .',type_now)
    model_ = []
    for n in data:
        if type_now == n[0]:

            model_.append(n[1])
    model_ = list(set(model_))
    model_.sort()
    print('model now is .',model_)
    self.combobox_'''+str(10+i)+'''.clear()
    self.combobox_'''+str(10+i)+'''.addItems(model_)
    flag_ = 0
    return model_
    '''   
        exec(def1)

    for i in range(stage):#批量生产槽,当更改model,frq随着更改
        def2 = '''
def changedmodel'''+str(i)+'''(self):
        global flag_
        if flag_ == 1:
            return
        a = self.combobox_'''+str(i)+'''.currentText()
        b = self.combobox_'''+str(10+i)+'''.currentText()
        frq_ = []
        for n in data:
#            print(n)
            if a == n[0] and b == n[1]:
                frq_.append(n[2])
        self.combobox_'''+str(20+i)+'''.clear()
        self.combobox_'''+str(20+i)+'''.addItems(frq_)
        flag_ == 0
        return frq_
    '''   
        exec(def2)
    global NF_list 
    global gain_list
    global config_data
    config_data = ''
    gain_list = []    
    NF_list = []    
    for i in range(stage):#批量生产槽,当更改model,frq随着更改
        NF_list.append('')
        gain_list.append('')
        def3 = '''
def changedfrq'''+str(i)+'''(self): 

        a = self.combobox_'''+str(i)+'''.currentText()
        b = self.combobox_'''+str(10+i)+'''.currentText()
        c = self.combobox_'''+str(20+i)+'''.currentText()
        gain_ = ''
        for n in data:
            if a == n[0] and b == n[1] and c == n[2]:
                gain_ = n[3]

        NF_ = ''
        for n in data:
            if a == n[0] and b == n[1] and c == n[2]:
                NF_ = n[4]
      
        self.lineedit_v'''+str(i)+'''.setText(str(gain_))
        self.lineedit_v'''+str(10+i)+'''.setText(str(NF_))
        NF_list['''+str(i)+'''] = NF_
#        gain_list['''+str(i)+'''] = gain_
#        print('NF_list',NF_list)
#        print('gain_list',gain_list)
        self.calc_gain()
        self.cal_NF()
    '''   
        exec(def3)
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(8*(width_+20), 400)
        Dialog.setSizeGripEnabled(True)
        self.label_tpye = QtWidgets.QLabel(Dialog)
        self.label_tpye.setGeometry(QtCore.QRect(21, 70, 24, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)

        self.pe_red = QPalette()  
        self.pe_red.setColor(QPalette.WindowText,Qt.red)  
        # self.label.setAutoFillBackground(True)  
        self.pe_red.setColor(QPalette.Window,Qt.blue)  
        self.pe_green = QPalette()  
        self.pe_green.setColor(QPalette.WindowText,Qt.green)  
        # self.label.setAutoFillBackground(True)  
        self.pe_green.setColor(QPalette.Window,Qt.blue)  
        #设置label
        self.label_tpye.setFont(font)
        self.label_tpye.setMouseTracking(False)
        self.label_tpye.setScaledContents(False)
        self.label_tpye.setWordWrap(False)
        self.label_tpye = QtWidgets.QLabel(Dialog)
        self.label_tpye.setGeometry(QtCore.QRect(21, 70, 24, 16))
        self.label_tpye.setObjectName("label_tpye")   #类型标签
        self.label_model = QtWidgets.QLabel(Dialog)
        self.label_model.setGeometry(QtCore.QRect(21, 93, 24, 16))
        self.label_model.setObjectName("label_model")   #型号标签
        self.label_frq = QtWidgets.QLabel(Dialog)
        self.label_frq.setGeometry(QtCore.QRect(21, 116, 24, 16))
        self.label_frq.setObjectName("label_frq")         #频率标签
        self.label_gain = QtWidgets.QLabel(Dialog)
        self.label_gain.setGeometry(QtCore.QRect(20, 160, 24, 16))
        self.label_gain.setObjectName("label_gain")   #增益标签
        self.label_NF = QtWidgets.QLabel(Dialog)
        self.label_NF.setGeometry(QtCore.QRect(20, 190, 24, 16))
        self.label_NF.setObjectName("label_NF")   #NF标签
        self.label_gaintotal = QtWidgets.QLabel(Dialog)
        self.label_gaintotal.setGeometry(QtCore.QRect(20, 230, 30, 16))
        self.label_gaintotal.setObjectName("label_gain")     #Σ增益标签
        self.label_NFtotal = QtWidgets.QLabel(Dialog)
        self.label_NFtotal.setGeometry(QtCore.QRect(20, 255, 30, 16))
        self.label_NFtotal.setObjectName("label_NF")       #ΣNF标签    
        self.label_opresult = QtWidgets.QLabel(Dialog)
        self.label_opresult.setGeometry(QtCore.QRect(70+7*103, 330+23, 200, 23))
        self.label_opresult.setObjectName("opresult")       #操作结果标签     
       
       
        self.pushButton_save = QtWidgets.QPushButton(Dialog)   #保存按钮
        self.pushButton_save.setGeometry(QtCore.QRect(70, 10, 75, 23))
        self.pushButton_save.setObjectName("pushButton")
        self.pushButton_save.clicked.connect(self.saveconf)

        self.pushButton_load = QtWidgets.QPushButton(Dialog)   #载入按钮
        self.pushButton_load.setGeometry(QtCore.QRect(70+103, 10, 75, 23))
        self.pushButton_load.setObjectName("pushButton")        
        self.pushButton_load.clicked.connect(self.openconf)
         
        self.label_tpye_add = QtWidgets.QLabel(Dialog)
        self.label_tpye_add.setGeometry(QtCore.QRect(100, 330, 24, 16))
        self.label_tpye_add.setObjectName("label_tpye")   #类型标签
        self.label_model_add = QtWidgets.QLabel(Dialog)
        self.label_model_add.setGeometry(QtCore.QRect(100+103, 330, 24, 16))
        self.label_model_add.setObjectName("label_model")   #型号标签
        self.label_frq_add = QtWidgets.QLabel(Dialog)
        self.label_frq_add.setGeometry(QtCore.QRect(100+2*103, 330, 24, 16))
        self.label_frq_add.setObjectName("label_frq")         #频率标签
        self.label_gain_add = QtWidgets.QLabel(Dialog)
        self.label_gain_add.setGeometry(QtCore.QRect(100+3*103, 330, 24, 16))
        self.label_gain_add.setObjectName("label_gain")   #增益标签
        self.label_NF_add = QtWidgets.QLabel(Dialog)
        self.label_NF_add.setGeometry(QtCore.QRect(100+4*103, 330, 24, 16))
        self.label_NF_add.setObjectName("label_NF")   #NF标签
        
        self.combobox_type_add = QtWidgets.QComboBox(Dialog)#‘添加类型’combobox
        self.combobox_type_add.setGeometry(QtCore.QRect(70, 330+23, 100, 22)) 
        self.combobox_type_add.setEditable(True)
        self.combobox_type_add.setObjectName("comboBox")   
        self.combobox_type_add.addItems(type_list)
        self.combobox_type_add.currentTextChanged.connect(self.load_add_model)
        
        self.combobox_model_add = QtWidgets.QComboBox(Dialog)
        self.combobox_model_add.setGeometry(QtCore.QRect(70+103, 330+23, 100, 22)) #‘添加类型’combobox
        self.combobox_model_add.setEditable(True)
        self.combobox_model_add.setObjectName("comboBox")  
        
        self.combobox_frq_add = QtWidgets.QComboBox(Dialog)#‘添加类型’combobox
        self.combobox_frq_add.setGeometry(QtCore.QRect(70+2*103, 330+23, 100, 22)) 
        self.combobox_frq_add.setEditable(True)
        self.combobox_frq_add.setObjectName("comboBox")     
      
        self.lineedit_add_gain = QtWidgets.QLineEdit(Dialog)  #'添加增益'lineedit
        self.lineedit_add_gain.setGeometry(QtCore.QRect(70+3*103, 330+23, 100, 22))
        self.lineedit_add_gain.setObjectName("lineEdit")
        
        self.lineedit_add_NF = QtWidgets.QLineEdit(Dialog)  #'添加NF'lineedit
        self.lineedit_add_NF.setGeometry(QtCore.QRect(70+4*103, 330+23, 100, 22))
        self.lineedit_add_NF.setObjectName("lineEdit")      
      
        self.pushButton_add = QtWidgets.QPushButton(Dialog)   #添加按钮
        self.pushButton_add.setGeometry(QtCore.QRect(70+5*103, 330+23, 75, 23))
        self.pushButton_add.setObjectName("pushButton")        
        self.pushButton_add.clicked.connect(self.add)

        self.pushButton_del = QtWidgets.QPushButton(Dialog)   #添加按钮
        self.pushButton_del.setGeometry(QtCore.QRect(70+6*103, 330+23, 75, 23))
        self.pushButton_del.setObjectName("pushButton")        
        self.pushButton_del.clicked.connect(self.dele)    

        for x in range(3):#批量生成combobox type,model,frq
            for i in range(stage):
                setattr(self,'combobox_'+str(x*10+i),QtWidgets.QComboBox(Dialog))
    
                exec("self.combobox_"+str(x*10+i)+".setGeometry(QtCore.QRect(70+i*(width_+3), 70+x*23, width_, 22))")
                exec('self.combobox_'+str(x*10+i)+'.setEditable(True)')
                exec('self.combobox_'+str(x*10+i)+'.setObjectName("comboBox")')
#                if x == 0:
#                    exec('self.combobox_'+str(x*10+i)+'.addItems(type_list)')
                
        for x in range(2):#批量生成editline,gain NF
            for i in range(stage):
                setattr(self,'lineedit_v'+str(x*10+i),QtWidgets.QLineEdit(Dialog))
                exec("self.lineedit_v"+str(x*10+i)+".setGeometry(QtCore.QRect(70+i*(width_+3), 70+4*23+x*23, width_, 22))")
                exec('self.lineedit_v'+str(x*10+i)+'.setObjectName("lineEdit")')
     
        for i in range(stage):#批量生产信号，当更改type,model随着更改                
            exec('self.combobox_'+str(i)+'.currentTextChanged["QString"].connect(self.changed_type'+str(i)+')')
        for i in range(stage):#批量生产信号，当更改model,frq随着更改                
            exec('self.combobox_'+str(10+i)+'.currentTextChanged["QString"].connect(self.changedmodel'+str(i)+')')
        for i in range(stage):#批量生产信号，当更改frq,gain&NF随着更改                
            exec('self.combobox_'+str(20+i)+'.currentTextChanged["QString"].connect(self.changedfrq'+str(i)+')')  
            
        for x in range(2):
            for i in range(stage):#批量生产信号，当更改gain&NF,cal随着更改                
                exec('self.lineedit_v'+str(x*10+i)+'.editingFinished.connect(self.cal_NF)')  
                exec('self.lineedit_v'+str(x*10+i)+'.editingFinished.connect(self.calc_gain)')  

        #设置gaintotal结果显示 
        for i in range(stage):
            setattr(self,'lineedit_gaintotal'+str(i),QtWidgets.QLineEdit(Dialog))
            exec("self.lineedit_gaintotal"+str(i)+".setGeometry(QtCore.QRect(70+i*(width_+3), 70+4*23+3*23, width_, 22))")
            exec('self.lineedit_gaintotal'+str(i)+'.setObjectName("lineEdit")')
            

        #设置NFtotal结果显示 
        for i in range(stage):
            setattr(self,'lineedit_NFtotal'+str(i),QtWidgets.QLineEdit(Dialog))
            exec("self.lineedit_NFtotal"+str(i)+".setGeometry(QtCore.QRect(70+i*(width_+3), 70+4*23+4*23, width_, 22))")
            exec('self.lineedit_NFtotal'+str(i)+'.setObjectName("lineEdit")')

        #设置sens结果显示 
        
        self.lineedit_sens = QtWidgets.QLineEdit(Dialog)
        self.lineedit_sens.setGeometry(QtCore.QRect(70+7*(width_+3), 70+4*23+5*23, width_, 22))
        self.lineedit_sens.setObjectName("lineEdit")

        for i in range(stage): #初始化批量载入类型  
            exec('self.combobox_'+str(i)+'.addItems(type_list)')
            
            
        self.retranslateUi(Dialog)
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "RF计算工具"))
        self.label_tpye.setText(_translate("Dialog", "类型"))
        self.label_model.setText(_translate("Dialog", "型号"))
        self.label_frq.setText(_translate("Dialog", "频率"))
        self.label_gain.setText(_translate("Dialog", "增益"))
        self.label_NF.setText(_translate("Dialog", "NF"))
        self.label_gaintotal.setText(_translate("Dialog", "Σ增益"))
        self.label_NFtotal.setText(_translate("Dialog", "ΣNF"))
        self.pushButton_save.setText(_translate("Dialog", "保存配置"))
        self.pushButton_load.setText(_translate("Dialog", "载入配置"))
        self.label_tpye_add.setText(_translate("Dialog", "类型"))
        self.label_model_add.setText(_translate("Dialog", "型号"))
        self.label_frq_add.setText(_translate("Dialog", "频率"))
        self.label_gain_add.setText(_translate("Dialog", "增益"))
        self.label_NF_add.setText(_translate("Dialog", "NF"))        
        self.pushButton_add.setText(_translate("Dialog", "添加器件"))
        self.pushButton_del.setText(_translate("Dialog", "删除器件"))        
        self.label_opresult.setText(_translate("Dialog", "操作结果"))         
        
        
    def calc_gain(self):
        for i in range(stage):
            exec('gain_list['+str(i)+'] = (self.lineedit_v'+str(i)+'.text())')
        gain_total = 0
        global gain_totallist
        gain_totallist = []
        for n in range(stage):
            if gain_list[n] == '':
                return
        for n in range(stage):
            gain_total = gain_total + float(gain_list[n])
            gain_totallist.append(round(gain_total, 2))
            exec('self.lineedit_gaintotal'+str(n)+'.setText(str(gain_totallist[n]))')
    def cal_NF(self):
        for i in range(stage):
            exec('NF_list['+str(i)+'] = (self.lineedit_v'+str(10+i)+'.text())')
        NF_total = 0
        global NF_totallist
        NF_totallist = []
        for n in range(stage):
            if NF_list[n] == '':
                return
        for n in range(stage):
            if n == 0:
                NF_total = float(NF_list[0])
            else:    
                NF_total = self.mwtodb(self.dbtomw(NF_total) + (self.dbtomw(float(NF_list[n]))-1)/self.dbtomw(float(gain_totallist[n-1])))
#                NF_total = NF_total+float(NF_list[n])
            NF_totallist.append(round(NF_total, 2))
            exec('self.lineedit_NFtotal'+str(n)+'.setText(str(NF_totallist[n]))')
        self.calsen()
    def load_current_additems(self):    
        self.type_add  = self.combobox_type_add.currentText()
        self.model_add  = self.combobox_model_add.currentText()
        self.frq_add  = self.combobox_frq_add.currentText()
        self.gain_add = self.lineedit_add_gain.text()
        self.NF_add = self.lineedit_add_NF.text()
        return self.type_add, self.model_add, self.frq_add, self.gain_add, self.NF_add
    def add(self):    
        self.type_add, self.model_add, self.frq_add, self.gain_add, self.NF_add = self.load_current_additems()
        savetodb('test.db')
    def dele(self):
        self.type_add, self.model_add, self.frq_add, self.gain_add, self.NF_add = self.load_current_additems()
        delformdb('test.db')       
    def mwtodb(self, argv):    
        return 10*math.log(argv, 10)
    def dbtomw(self, argv):    
        return 10**(argv/10)
    def calsen(self):
        k_ =1.3806505*(10**(-20))
        bw = 9*(10**6)
        t = 298
        kbt = k_*bw*t
        sens = 10*math.log(kbt, 10)+NF_totallist[-1]-1
        print(sens)
        self.lineedit_sens.setText(str(round(sens, 2)))


    def saveconf(self):
        self.filename,_ = QFileDialog.getSaveFileName(Dialog,"选取文件","", "Text Files (*.txt)");
        if self.filename == '':
            return
        with open(self.filename, 'w', encoding = 'utf-8') as config_:
            for x in range(3):#批量打开combobox type,model,frq
                for i in range(stage):
                    exec('self.config_data = self.combobox_'+str(10*x+i)+'.currentText()')
                    config_.write(self.config_data+'\n')


    def openconf(self):
        self.filename,_ = QFileDialog.getOpenFileName(Dialog,"选取文件","", "Text Files (*.txt)");
        if self.filename == '':
            return
        with open(self.filename, 'r', encoding = 'utf-8') as config_:
            config_data_list=[]
            exec('n = 0')
            for i in config_.readlines():
                i = i.strip('\n')
                config_data_list.append(i)
            for x in range(3):#批量打开combobox type,model,frq
                for i in range(stage):
                    flag_ = 1
                    exec('m = self.combobox_'+str(10*x+i)+'.findText(config_data_list[n])')
                    exec('self.combobox_'+str(10*x+i)+'.setCurrentIndex(m)')
                    flag_ = 0
#                    config_.write(self.config_data+'\n')
                    exec('n=n+1')
    def load_add_model(self):
        self.add_model_list = []        
        for w in data:
            if w[0] == self.combobox_type_add.currentText():
                self.add_model_list.append(w[1])
            self.add_model_list = list(set(self.add_model_list))
        print(self.add_model_list)


    


def opendatabase():
    data_ = []
    with open('database.txt', 'r', encoding = 'utf-8') as data:
        for line in data.readlines():
            a = line.split()
            data_.append(a)
    return data_

def get_typelist():
    type_ = []
    for n in data:
        type_.append(n[0])
    type_ = list(set(type_))
    type_.sort()
    return(type_)

def savetodb(dbname, tablename = ''):
    if ui.type_add == '':
        ui.label_opresult.setText ('无类型数据')
        ui.label_opresult.setPalette(ui.pe_red)  
        return
    elif ui.model_add == '':
        ui.label_opresult.setText('无型号数据')
        ui.label_opresult.setPalette(ui.pe_red) 
        return
    elif ui.frq_add == '':
        ui.label_opresult.setText('无频率数据')
        ui.label_opresult.setPalette(ui.pe_red) 
        return
    elif ui.gain_add == '':
        ui.label_opresult.setText('无增益数据')
        ui.label_opresult.setPalette(ui.pe_red) 
        return
    elif ui.NF_add == '':
        ui.label_opresult.setText('无NF数据')
        ui.label_opresult.setPalette(ui.pe_red) 
        return
    try:
        float(ui.gain_add)
    except ValueError as e:
        ui.label_opresult.setText('输入的增益为非数字')
        ui.label_opresult.setPalette(ui.pe_red)
        return
    try:
        float(ui.NF_add)
    except ValueError as e:
        ui.label_opresult.setText('输入的NF为非数字')
        ui.label_opresult.setPalette(ui.pe_red)
        return
             
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("select * from component")
    db_tupelist = cur.fetchall()
    # print(db_tupelist)
    len_ = str(int(db_tupelist[-1][0])+1)
    print(len_)
    # cur.execute('PRAGMA table_info(component)')
    cur.execute("select * from component where type = '%s' and model = '%s' and frq = '%s'" % (ui.type_add,ui.model_add,ui.frq_add))
    data_existed = cur.fetchall()
    if data_existed:
        print ('器件存在:',data_existed)
        ui.label_opresult.setText('器件存在')
        ui.label_opresult.setPalette(ui.pe_red) 
    else:    
        cur.execute("select * from component")
        cur.execute("insert into component (id, type,model,frq,gain,nf) values ('%s','%s','%s','%s','%f','%f')" % (len_, ui.type_add,ui.model_add,ui.frq_add,float(ui.gain_add),float(ui.NF_add)))
        # cur.execute("select * from component")
        cur.execute("select * from component where id = '%s' and type = '%s' and model = '%s' and frq = '%s' and gain = '%f' and nf = '%f'" % (len_, ui.type_add,ui.model_add,ui.frq_add,float(ui.gain_add),float(ui.NF_add)))
        data_existed = cur.fetchall()
        if data_existed != []:
            print(data_existed)
            print('添加成功')
            ui.label_opresult.setText('添加成功') 
            ui.label_opresult.setPalette(ui.pe_green) 
        cur.close()
        conn.commit()
        conn.close()
    global data
    global type_list        
    data, type_list = initdata()

    return db_tupelist   
 
def delformdb(dbname,tablename = ''):
    if ui.type_add == '':
        ui.label_opresult.setText ('无类型数据')
        ui.label_opresult.setPalette(ui.pe_red)  
        return
    elif ui.model_add == '':
        ui.label_opresult.setText('无型号数据')
        ui.label_opresult.setPalette(ui.pe_red) 
        return
    elif ui.frq_add == '':
        ui.label_opresult.setText('无频率数据')
        ui.label_opresult.setPalette(ui.pe_red) 
        return    
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("select * from component")
    db_tupelist = cur.fetchall()
    # print(db_tupelist)
    len_ = str(len(db_tupelist))
    # cur.execute('PRAGMA table_info(component)')
    cur.execute("select * from component where type = '%s' and model = '%s' and frq = '%s'" % (ui.type_add,ui.model_add,ui.frq_add))
    data_existed = cur.fetchall()
    if data_existed == []:
        print('不存在该器件')
        ui.label_opresult.setText('不存在该器件')  
        ui.label_opresult.setPalette(ui.pe_red)
    else:
        cur.execute("delete from component where type = '%s' and model = '%s' and frq = '%s'" % (ui.type_add,ui.model_add,ui.frq_add))
        cur.execute("select * from component where type = '%s' and model = '%s' and frq = '%s'" % (ui.type_add,ui.model_add,ui.frq_add))
        data_existed = cur.fetchall()
        if data_existed == []:
            print('删除成功')
            ui.label_opresult.setText('删除成功') 
            ui.label_opresult.setPalette(ui.pe_green) 

    cur.close()
    conn.commit()
    conn.close()
    global data
    global type_list
    data, type_list = initdata()

def opendb(dbname, tablename = ''):    
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("select type,model,frq,gain,nf from component")
    db_tupelist = cur.fetchall()
    return db_tupelist

def typelist(tupelist):
    l = []
    for t in tupelist:
        l.append(t[0])
    l = list(set(l))    #去重
    l.sort()    #排序
    return l
def initdata():
    data = opendb('test.db')
    type_list = typelist(data)
    return data, type_list

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    global data
    global type_list
    data, type_list = initdata()
    # data = opendb('test.db')
    # type_list = typelist(data)
    flag_ = 0
#    data = opendatabase()
#    print('data:', data)
    width_ = 100 
#    type_list = get_typelist() #with open text
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    sys.exit(app.exec_())

