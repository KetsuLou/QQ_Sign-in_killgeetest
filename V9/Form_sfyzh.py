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
        self.master.title('三丰云配置')
        self.master.geometry('255x171')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Label_sfyusername.TLabel',anchor='w', font=('宋体',12))
        self.Label_sfyusername = Label(self.top, text='账号：', style='Label_sfyusername.TLabel')
        self.Label_sfyusername.place(relx=0.063, rely=0.094, relwidth=0.522, relheight=0.117)

        self.Text_sfyusernameVar = StringVar(value='')
        self.Text_sfyusername = Entry(self.top, textvariable=self.Text_sfyusernameVar, font=('宋体',9))
        self.Text_sfyusername.place(relx=0.063, rely=0.234, relwidth=0.859, relheight=0.117)

        self.style.configure('Label_sfypwd.TLabel',anchor='w', font=('宋体',12))
        self.Label_sfypwd = Label(self.top, text='密码：', style='Label_sfypwd.TLabel')
        self.Label_sfypwd.place(relx=0.063, rely=0.374, relwidth=0.522, relheight=0.117)

        self.Text_sfypwdVar = StringVar(value='')
        self.Text_sfypwd = Entry(self.top, textvariable=self.Text_sfypwdVar, font=('宋体',9))
        self.Text_sfypwd.place(relx=0.063, rely=0.515, relwidth=0.859, relheight=0.117)

        self.style.configure('Button_save.TButton',font=('宋体',9))
        self.Button_save = Button(self.top, text='配置', command=self.Button_save_Cmd, style='Button_save.TButton')
        self.Button_save.place(relx=0.188, rely=0.702, relwidth=0.261, relheight=0.195)

        self.style.configure('Button_close.TButton',font=('宋体',9))
        self.Button_close = Button(self.top, text='关闭', command=self.Button_close_Cmd, style='Button_close.TButton')
        self.Button_close.place(relx=0.565, rely=0.702, relwidth=0.261, relheight=0.195)

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
            try: self.config.add_section('path_sfy')
            except: pass
                
            try:
                #显示账号信息
                self.Text_sfyusername.insert(0, self.config['path_sfy']['username'])
                self.Text_sfypwd.insert(0, self.config['path_sfy']['password'])
            except:
                self.config.set('path_sfy', 'username', '')
                self.config.set('path_sfy', 'password', '')
                self.config.write(open(path_default_sys, 'r+'))
                #显示账号信息
                self.Text_sfyusername.insert(0, self.config['path_sfy']['username'])
                self.Text_sfypwd.insert(0, self.config['path_sfy']['password'])

        except:
            tkinter.messagebox.showerror('错误','配置加载错误！')     

    def Button_save_Cmd(self, event=None):
        self.config.read(self.path)
        try:
            #保存数据
            if self.Text_sfyusername.get() == '' or self.Text_sfypwd.get() == '': raise
            self.config.set('path_sfy','username', self.Text_sfyusername.get())
            self.config.set('path_sfy','password', self.Text_sfypwd.get())
            self.config.write(open(self.path, 'r+'))
            tkinter.messagebox.showinfo('提示','保存成功！')
        except:
            tkinter.messagebox.showerror('错误','保存失败！')

    def Button_close_Cmd(self, event=None):
        self.master.destroy()

def Form_sfyzh_main():
    if __name__ == "__main__": top = Tk()
    else: 
        top = Toplevel()
        top.wm_attributes('-topmost',1)

    Application(top).mainloop()
    try: top.destroy()
    except: pass

if __name__ == "__main__":
    Form_sfyzh_main()
