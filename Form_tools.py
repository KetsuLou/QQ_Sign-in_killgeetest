#!/usr/bin/env python
#-*- coding:utf-8 -*-

import Form_killgeetest, Form_sfyxq

path_default_sys = r'.\path\path_sys.ini'
path_default_chrome = r'.\Google\Chrome\Application\chromedriver.exe'
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
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('开发工具')
        self.master.geometry('246x201')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Button_killgeetest.TButton',font=('宋体',9))
        self.Button_killgeetest = Button(self.top, text='geetest杀手', command=self.Button_killgeetest_Cmd, style='Button_killgeetest.TButton')
        self.Button_killgeetest.place(relx=0.081, rely=0.1, relwidth=0.407, relheight=0.166)

        self.style.configure('Button_sfyxq.TButton',font=('宋体',9))
        self.Button_sfyxq = Button(self.top, text='三丰云续费', command=self.Button_sfyxq_Cmd, style='Button_sfyxq.TButton')
        self.Button_sfyxq.place(relx=0.488, rely=0.1, relwidth=0.407, relheight=0.166)

class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Button_killgeetest_Cmd(self, event=None):
        Form_killgeetest.Form_killgeetest_main()
        
    def Button_sfyxq_Cmd(self, event=None):
        #TODO, Please finish the function here!
        Form_sfyxq.Form_sfyxq_main()

def Form_tools_main():
    if __name__ == "__main__": top = Tk()
    else: 
        top = Toplevel()
        top.wm_attributes('-topmost',1)
        
    Application(top).mainloop()
    try: top.destroy()
    except: pass

if __name__ == "__main__":
    Form_tools_main()