#!/usr/bin/env python
#-*- coding:utf-8 -*-
import configparser

path_default_sys = r'.\path\path_sys.ini'
path_default_chrome = r'.\Google\Chrome\Application\chromedriver.exe'
path_default_offset = '0'

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
        self.master.title('系统设置')
        self.master.geometry('291x201')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.Text_inipathVar = StringVar(value='')
        self.Text_inipath = Entry(self.top, textvariable=self.Text_inipathVar, font=('宋体',9))
        self.Text_inipath.place(relx=0.046, rely=0.166, relwidth=0.916, relheight=0.1)

        self.style.configure('Button_OK.TButton',font=('宋体',9))
        self.Button_OK = Button(self.top, text='配置', command=self.Button_OK_Cmd, style='Button_OK.TButton')
        self.Button_OK.place(relx=0.183, rely=0.73, relwidth=0.229, relheight=0.166)

        self.style.configure('Button_close.TButton',font=('宋体',9))
        self.Button_close = Button(self.top, text='关闭', command=self.Button_close_Cmd, style='Button_close.TButton')
        self.Button_close.place(relx=0.596, rely=0.73, relwidth=0.229, relheight=0.166)

        self.style.configure('Label_inipath.TLabel',anchor='w', font=('宋体',12))
        self.Label_inipath = Label(self.top, text='ini路径地址：', style='Label_inipath.TLabel')
        self.Label_inipath.place(relx=0.046, rely=0.066, relwidth=0.457, relheight=0.1)

        self.Text_chromepathVar = StringVar(value='')
        self.Text_chromepath = Entry(self.top, textvariable=self.Text_chromepathVar, font=('宋体',9))
        self.Text_chromepath.place(relx=0.046, rely=0.398, relwidth=0.916, relheight=0.1)

        self.style.configure('Label_chromepath.TLabel',anchor='w', font=('宋体',12))
        self.Label_chromepath = Label(self.top, text='chrome路径地址：', style='Label_chromepath.TLabel')
        self.Label_chromepath.place(relx=0.046, rely=0.299, relwidth=0.457, relheight=0.1)


       

class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        self.config = configparser.ConfigParser() # 类实例化
        self.config.read(path_default_sys)
        self.path = self.config['path']['path_ini']
        try:
            self.config.read(path_default_sys)
            path = self.config['path']['path_ini']
        except:
            pass
        
        self.config.read(path_default_sys)
        self.Text_inipath.insert(0, self.config['path']['path_ini'])
        self.Text_chromepath.insert(0, self.config['path']['path_chrome'])

    def Button_OK_Cmd(self, event=None):
        try:
            if self.Text_inipath.get() != '': path_ini = self.Text_inipath.get()
            else: raise
            if self.Text_chromepath.get() != '': path_chrome = self.Text_chromepath.get()
            else: raise
            self.path = self.config['path']['path_ini']
            self.config.read(path_default_sys)
            #date = config.add_section("path")
            #写入数据
            self.config.set('path','path_ini', path_ini)
            self.config.set('path','path_chrome', path_chrome)
            #保存数据
            #with open(path_default_sys , 'w') as f:f.close()
            self.config.write(open(path_default_sys, 'w'))
            tkinter.messagebox.showinfo('提示','系统配置保存成功！')
        except:
            tkinter.messagebox.showerror('错误','系统配置保存出错！')
   
    def Button_close_Cmd(self, event=None):
        self.master.destroy()
    
    
def Form_sys_main():
    if __name__ == "__main__": top = Tk()
    else: 
        top = Toplevel()
        top.wm_attributes('-topmost',1)
          
    try:
        #读取ini配置，chrome配置
        try:
            #成功
            config = configparser.ConfigParser()
            config.read(path_default_sys)
            config['path']['path_ini']
            config['path']['path_chrome']
            config['path']['offset_correction']
        except:
            config.add_section('path')
            config.set('path', 'path_ini', path_default_sys)
            config.set('path', 'path_chrome', path_default_chrome)
            config.set('path', 'offset_correction', path_default_offset)
            config.write(open(path_default_sys, 'w'))
            #with open(path_default_ini , 'w') as f:f.close()
                
    except:
        tkinter.messagebox.showerror('错误','系统配置出现问题！')
    Application(top).mainloop()
    try: top.destroy()
    except: pass

if __name__ == "__main__":
    Form_sys_main()