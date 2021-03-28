#!/usr/bin/env python
#-*- coding:utf-8 -*-

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
        self.master.title('信息配置')
        self.master.geometry('291x228')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Option_sgs.TRadiobutton',font=('宋体',9))
        self.Option_sgs = Radiobutton(self.top, text='三国杀', variable = var_choose, value = 'sgs', style='Option_sgs.TRadiobutton', command = self.select)
        self.Option_sgs.place(relx=0.321, rely=0.614, relwidth=0.229, relheight=0.117)

        self.style.configure('Option_1and2.TRadiobutton',font=('宋体',9))
        self.Option_1and2 = Radiobutton(self.top, text='自动领赞配置', variable = var_choose, value='zdlz', style='Option_1and2.TRadiobutton', command = self.select)
        self.Option_1and2.place(relx=0.573, rely=0.614, relwidth=0.344, relheight=0.117)

        self.style.configure('Option_QQ.TRadiobutton',font=('宋体',9))
        self.Option_QQ = Radiobutton(self.top, text='QQ号', variable = var_choose, value='QQ', style='Option_QQ.TRadiobutton', command = self.select)
        self.Option_QQ.place(relx=0.069, rely=0.614, relwidth=0.229, relheight=0.117)

        self.Text_QQVar = StringVar(value='')
        self.Text_QQ = Entry(self.top, textvariable=self.Text_QQVar, font=('宋体',9))
        self.Text_QQ.place(relx=0.046, rely=0.146, relwidth=0.916, relheight=0.088)

        self.Text_input1Var = StringVar(value='')
        self.Text_input1 = Entry(self.top, textvariable=self.Text_input1Var, font=('宋体',9))
        self.Text_input1.place(relx=0.046, rely=0.322, relwidth=0.916, relheight=0.088)

        self.Text_input2Var = StringVar(value='')
        self.Text_input2 = Entry(self.top, textvariable=self.Text_input2Var, font=('宋体',9))
        self.Text_input2.place(relx=0.046, rely=0.497, relwidth=0.916, relheight=0.088)

        self.style.configure('Button_OK.TButton',font=('宋体',9))
        self.Button_OK = Button(self.top, text='配置', command=self.Button_OK_Cmd, style='Button_OK.TButton')
        self.Button_OK.place(relx=0.183, rely=0.789, relwidth=0.229, relheight=0.146)

        self.style.configure('Button_close.TButton',font=('宋体',9))
        self.Button_close = Button(self.top, text='关闭', command=self.Button_close_Cmd, style='Button_close.TButton')
        self.Button_close.place(relx=0.596, rely=0.789, relwidth=0.229, relheight=0.146)

        self.style.configure('Label_QQ.TLabel',anchor='w', font=('宋体',12))
        self.Label_QQ = Label(self.top, text='QQ：', style='Label_QQ.TLabel')
        self.Label_QQ.place(relx=0.046, rely=0.058, relwidth=0.457, relheight=0.088)

        self.style.configure('Label_input1.TLabel',anchor='w', font=('宋体',12))
        self.Label_input1 = Label(self.top, text='输入框1：', style='Label_input1.TLabel')
        self.Label_input1.place(relx=0.046, rely=0.234, relwidth=0.457, relheight=0.088)

        self.style.configure('Label_input2.TLabel',anchor='w', font=('宋体',12))
        self.Label_input2 = Label(self.top, text='输入框2：', style='Label_input2.TLabel')
        self.Label_input2.place(relx=0.046, rely=0.409, relwidth=0.457, relheight=0.088)

class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        self.config = configparser.ConfigParser() # 类实例化
        self.config.read(path_default_sys)
        self.path = self.config['path']['path_ini']
        #读取配置ini信息，没有对应的Section则新建
        try:
            self.config.read(self.path)
            try:
                self.config.add_section('QQ_path')
                self.config.set('QQ_path', 'QQ', '')
            except:
                pass
            
            try:
                self.config.add_section('path_4399')
                self.config.set('path_4399', 'username', '')
                self.config.set('path_4399', 'password', '')
            except:
                pass
            try:
                self.config.add_section('path_lz')
                self.config.set('path_lz', 'username', '')
                self.config.set('path_lz', 'password', '')
            except:
                pass
            self.config.write(open(path_default_sys, 'r+'))
            #显示QQ信息
            self.Text_QQ.insert(0, self.config['QQ_path']['QQ'])

        except:
            tkinter.messagebox.showerror('错误','配置加载错误！')     

    def Button_OK_Cmd(self, event=None):
        self.config.read(self.path)
        if var_choose.get() == 'sgs':
            try:
                #保存数据
                if self.Text_input1.get() == '' or self.Text_input2.get() == '': raise
                self.config.set('path_4399','username', self.Text_input1.get())
                self.config.set('path_4399','password', self.Text_input2.get())
                self.config.write(open(self.path, 'r+'))
                tkinter.messagebox.showinfo('提示','三国杀配置保存成功！')
            except:
                tkinter.messagebox.showerror('错误','三国杀配置保存失败！')
        elif var_choose.get() == 'zdlz':
            try:
                #保存数据
                if self.Text_input1.get() == '' or self.Text_input2.get() == '': raise
                self.config.set('path_lz','username', self.Text_input1.get())
                self.config.set('path_lz','password', self.Text_input2.get())
                self.config.write(open(self.path, 'r+'))
                tkinter.messagebox.showinfo('提示','领赞配置保存成功！')
            except:
                tkinter.messagebox.showerror('错误','领赞配置保存失败！')
        elif var_choose.get() == 'QQ':
            try:
                #保存数据
                if self.Text_QQ.get() == '': raise
                self.config.set('QQ_path','QQ', self.Text_QQ.get())
                self.config.write(open(self.path, 'r+'))
                tkinter.messagebox.showinfo('提示','QQ配置保存成功！')
            except:
                tkinter.messagebox.showerror('错误','QQ配置保存失败！')
        else:
            tkinter.messagebox.showerror('错误','未知错误！')

    def Button_close_Cmd(self, event=None):
        self.master.destroy()
        
    def select(self, event=None):    
        self.Text_QQ.delete(0, END)
        self.Text_input1.delete(0, END)
        self.Text_input2.delete(0, END)
        try:
            if var_choose.get() == 'sgs':
                self.Label_input1.config(text = "4399账号：")
                self.Label_input2.config(text = "密码：")          
                self.Text_input1.insert(0, self.config['path_4399']['username'])
                self.Text_input2.insert(0, self.config['path_4399']['password'])
                if self.Text_input1.get() == '' or self.Text_input2.get() == '': raise
            elif var_choose.get() == 'zdlz':
                self.Label_input1.config(text = "领赞账号：")
                self.Label_input2.config(text = "密码：")
                self.Text_input1.insert(0, self.config['path_lz']['username'])
                self.Text_input2.insert(0, self.config['path_lz']['password'])
                if self.Text_input1.get() == '' or self.Text_input2.get() == '': raise
            elif var_choose.get() == 'QQ':
                self.Label_input1.config(text = "输入框1：")
                self.Label_input2.config(text = "输入框2：")
                self.Text_QQ.insert(0, self.config['QQ_path']['QQ'])
                if self.Text_QQ.get() == '': raise
            else:
                self.Label_QQ.config(text = "QQ:")
                self.Label_input1.config(text = "输入框1")
                self.Label_input2.config(text = "输入框2")     
        except:
            tkinter.messagebox.showerror('错误','ini未配置有效信息！')
            
        
def Form_inf_main():
    if __name__ == "__main__": top = Tk()
    else: 
        top = Toplevel()
        top.wm_attributes('-topmost',1)

    global var_choose
    var_choose = StringVar()
    var_choose.set("QQ")
    Application(top).mainloop()
    try: top.destroy()
    except: pass

if __name__ == "__main__":
    Form_inf_main()