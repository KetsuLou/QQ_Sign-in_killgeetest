#!/usr/bin/env python
#-*- coding:utf-8 -*-
#默认网站配置在Form_sys.py里面！！！！！！！！！！
import configparser
path_default_sys = r'.\path\path_sys.ini'

import os, sys
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    import tkinter
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('网站配置')
        self.master.geometry('458x582')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()
        #----------------------------------------------------------------------------------
        self.Text_zdlz1Var = StringVar(value='')
        self.Text_zdlz1 = Entry(self.top, textvariable=self.Text_zdlz1Var, font=('宋体',9))
        self.Text_zdlz1.place(relx=0.044, rely=0.069, relwidth=0.902, relheight=0.034)

        self.Text_zdlz2Var = StringVar(value='')
        self.Text_zdlz2 = Entry(self.top, textvariable=self.Text_zdlz2Var, font=('宋体',9))
        self.Text_zdlz2.place(relx=0.044, rely=0.137, relwidth=0.902, relheight=0.034)

        self.Text_zdlz3Var = StringVar(value='')
        self.Text_zdlz3 = Entry(self.top, textvariable=self.Text_zdlz3Var, font=('宋体',9))
        self.Text_zdlz3.place(relx=0.044, rely=0.206, relwidth=0.902, relheight=0.034)

        self.Text_zdlz4Var = StringVar(value='')
        self.Text_zdlz4 = Entry(self.top, textvariable=self.Text_zdlz4Var, font=('宋体',9))
        self.Text_zdlz4.place(relx=0.044, rely=0.275, relwidth=0.902, relheight=0.034)

        self.Text_zdlz5Var = StringVar(value='')
        self.Text_zdlz5 = Entry(self.top, textvariable=self.Text_zdlz5Var, font=('宋体',9))
        self.Text_zdlz5.place(relx=0.044, rely=0.344, relwidth=0.902, relheight=0.034)

        self.Text_zdlz6Var = StringVar(value='')
        self.Text_zdlz6 = Entry(self.top, textvariable=self.Text_zdlz6Var, font=('宋体',9))
        self.Text_zdlz6.place(relx=0.044, rely=0.412, relwidth=0.902, relheight=0.034)

        self.Text_zdqd1Var = StringVar(value='')
        self.Text_zdqd1 = Entry(self.top, textvariable=self.Text_zdqd1Var, font=('宋体',9))
        self.Text_zdqd1.place(relx=0.044, rely=0.481, relwidth=0.902, relheight=0.034)

        self.Text_zdqd2Var = StringVar(value='')
        self.Text_zdqd2 = Entry(self.top, textvariable=self.Text_zdqd2Var, font=('宋体',9))
        self.Text_zdqd2.place(relx=0.044, rely=0.55, relwidth=0.902, relheight=0.034)

        self.Text_sgsqd1Var = StringVar(value='')
        self.Text_sgsqd1 = Entry(self.top, textvariable=self.Text_sgsqd1Var, font=('宋体',9))
        self.Text_sgsqd1.place(relx=0.044, rely=0.619, relwidth=0.902, relheight=0.034)

        self.Text_sgsqd2Var = StringVar(value='')
        self.Text_sgsqd2 = Entry(self.top, textvariable=self.Text_sgsqd2Var, font=('宋体',9))
        self.Text_sgsqd2.place(relx=0.044, rely=0.687, relwidth=0.902, relheight=0.034)
        
        self.Text_sfycsVar = StringVar(value='')
        self.Text_sfycs = Entry(self.top, textvariable=self.Text_sfycsVar, font=('宋体',9))
        self.Text_sfycs.place(relx=0.044, rely=0.756, relwidth=0.902, relheight=0.034)

        self.Text_sfyvhVar = StringVar(value='')
        self.Text_sfyvh = Entry(self.top, textvariable=self.Text_sfyvhVar, font=('宋体',9))
        self.Text_sfyvh.place(relx=0.044, rely=0.825, relwidth=0.902, relheight=0.034)
        #----------------------------------------------------------------------------------
        self.style.configure('Label_zdlz1.TLabel',anchor='w', font=('宋体',12))
        self.Label_zdlz1 = Label(self.top, text='自动领赞1：', style='Label_zdlz1.TLabel')
        self.Label_zdlz1.place(relx=0.044, rely=0.034, relwidth=0.29, relheight=0.034)

        self.style.configure('Label_zdlz2.TLabel',anchor='w', font=('宋体',12))
        self.Label_zdlz2 = Label(self.top, text='自动领赞2：', style='Label_zdlz2.TLabel')
        self.Label_zdlz2.place(relx=0.044, rely=0.103, relwidth=0.29, relheight=0.034)
        
        self.style.configure('Label_zdlz3.TLabel',anchor='w', font=('宋体',12))
        self.Label_zdlz3 = Label(self.top, text='自动领赞3：', style='Label_zdlz3.TLabel')
        self.Label_zdlz3.place(relx=0.044, rely=0.172, relwidth=0.29, relheight=0.034)

        self.style.configure('Label_zdlz4.TLabel',anchor='w', font=('宋体',12))
        self.Label_zdlz4 = Label(self.top, text='自动领赞4：', style='Label_zdlz4.TLabel')
        self.Label_zdlz4.place(relx=0.044, rely=0.241, relwidth=0.29, relheight=0.034)

        self.style.configure('Label_zdlz5.TLabel',anchor='w', font=('宋体',12))
        self.Label_zdlz5 = Label(self.top, text='自动领赞5：', style='Label_zdlz5.TLabel')
        self.Label_zdlz5.place(relx=0.044, rely=0.309, relwidth=0.29, relheight=0.034)

        self.style.configure('Label_zdlz6.TLabel',anchor='w', font=('宋体',12))
        self.Label_zdlz6 = Label(self.top, text='自动领赞6：', style='Label_zdlz6.TLabel')
        self.Label_zdlz6.place(relx=0.044, rely=0.378, relwidth=0.29, relheight=0.034)
        
        self.style.configure('Label_zdqd1.TLabel',anchor='w', font=('宋体',12))
        self.Label_zdqd1 = Label(self.top, text='自动签到1：', style='Label_zdqd1.TLabel')
        self.Label_zdqd1.place(relx=0.044, rely=0.447, relwidth=0.29, relheight=0.034)

        self.style.configure('Label_zdqd2.TLabel',anchor='w', font=('宋体',12))
        self.Label_zdqd2 = Label(self.top, text='自动签到2：', style='Label_zdqd2.TLabel')
        self.Label_zdqd2.place(relx=0.044, rely=0.515, relwidth=0.29, relheight=0.034)

        self.style.configure('Label_sgsqd1.TLabel',anchor='w', font=('宋体',12))
        self.Label_sgsqd1 = Label(self.top, text='三国杀签到1：', style='Label_sgsqd1.TLabel')
        self.Label_sgsqd1.place(relx=0.044, rely=0.584, relwidth=0.29, relheight=0.034)

        self.style.configure('Label_sgsqd2.TLabel',anchor='w', font=('宋体',12))
        self.Label_sgsqd2 = Label(self.top, text='三国杀签到2：', style='Label_sgsqd2.TLabel')
        self.Label_sgsqd2.place(relx=0.044, rely=0.653, relwidth=0.29, relheight=0.034)

        self.style.configure('Label_sfycs.TLabel',anchor='w', font=('宋体',12))
        self.Label_sfycs = Label(self.top, text='三丰云云服务器：', style='Label_sfycs.TLabel')
        self.Label_sfycs.place(relx=0.044, rely=0.722, relwidth=0.29, relheight=0.034)

        self.style.configure('Label_sfyvh.TLabel',anchor='w', font=('宋体',12))
        self.Label_sfyvh = Label(self.top, text='三丰云虚拟主机：', style='Label_sfyvh.TLabel')
        self.Label_sfyvh.place(relx=0.044, rely=0.79, relwidth=0.29, relheight=0.034)
        #----------------------------------------------------------------------------------
        self.style.configure('Button_close.TButton',font=('宋体',9))
        self.Button_close = Button(self.top, text='关闭', command=self.Button_close_Cmd, style='Button_close.TButton')
        self.Button_close.place(relx=0.611, rely=0.916, relwidth=0.146, relheight=0.057)

        self.style.configure('Button_OK.TButton',font=('宋体',9))
        self.Button_OK = Button(self.top, text='配置', command=self.Button_OK_Cmd, style='Button_OK.TButton')
        self.Button_OK.place(relx=0.247, rely=0.916, relwidth=0.146, relheight=0.057)

class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        self.config = configparser.ConfigParser() # 类实例化
        self.config.read(path_default_sys)
        self.path = self.config['path']['path_ini']
        self.load()

    def Button_close_Cmd(self, event=None):
        self.master.destroy()

    def Button_OK_Cmd(self, event=None):
        self.config.read(path_default_sys)
        self.path = self.config['path']['path_ini']
        # self.config.read(self.path)
        try:
            '''
            if self.Text_zdlz1.get() == '': raise
            if self.Text_zdlz2.get() == '': raise
            if self.Text_zdlz3.get() == '': raise
            if self.Text_zdlz4.get() == '': raise
            if self.Text_zdlz5.get() == '': raise
            if self.Text_zdlz6.get() == '': raise
            if self.Text_zdqd1.get() == '': raise
            if self.Text_zdqd2.get() == '': raise
            if self.Text_sgsqd1.get() == '': raise
            if self.Text_sgsqd2.get() == '': raise
            '''
            #保存数据
            self.config.set('web','zdlz1', self.Text_zdlz1.get())
            self.config.set('web','zdlz2', self.Text_zdlz2.get())
            self.config.set('web','zdlz3', self.Text_zdlz3.get())
            self.config.set('web','zdlz4', self.Text_zdlz4.get())
            self.config.set('web','zdlz5', self.Text_zdlz5.get())
            self.config.set('web','zdlz6', self.Text_zdlz6.get())
            self.config.set('web','zdqd1', self.Text_zdqd1.get())
            self.config.set('web','zdqd2', self.Text_zdqd2.get())
            self.config.set('web','sgsqd1', self.Text_sgsqd1.get())                                                                       
            self.config.set('web','sgsqd2', self.Text_sgsqd2.get())
            self.config.set('web','sfycs', self.Text_sfycs.get())                                                                       
            self.config.set('web','sfyvh', self.Text_sfyvh.get())
            self.config.write(open(self.path, 'r+'))
            tkinter.messagebox.showinfo('提示','网站配置保存成功！')
        except:
            tkinter.messagebox.showerror('错误','网站配置保存失败！')
        
    def load(self, event=None):
        #读取网站配置ini信息
        try:
            self.Text_zdlz1.insert(0, self.config['web']['zdlz1'])
            self.Text_zdlz2.insert(0, self.config['web']['zdlz2'])
            self.Text_zdlz3.insert(0, self.config['web']['zdlz3'])
            self.Text_zdlz4.insert(0, self.config['web']['zdlz4'])
            self.Text_zdlz5.insert(0, self.config['web']['zdlz5'])
            self.Text_zdlz6.insert(0, self.config['web']['zdlz6'])
            self.Text_zdqd1.insert(0, self.config['web']['zdqd1'])
            self.Text_zdqd2.insert(0, self.config['web']['zdqd2'])
            self.Text_sgsqd1.insert(0, self.config['web']['sgsqd1'])
            self.Text_sgsqd2.insert(0, self.config['web']['sgsqd2'])
            self.Text_sfycs.insert(0, self.config['web']['sfycs'])
            self.Text_sfuvh.insert(0, self.config['web']['sfuvh'])
        except: pass

def Form_webset_main():
    if __name__ == "__main__": top = Tk()
    else: 
        top = Toplevel()
        top.wm_attributes('-topmost',1)

    Application(top).mainloop()
    try: top.destroy()
    except: pass

if __name__ == "__main__":
    Form_webset_main()