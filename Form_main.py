#!/usr/bin/env python
#-*- coding:utf-8 -*-
#导入窗口
import Form_inf, Form_sys, Form_attention, Form_tools

#导入自动程序
import zdlz1, zdlz3
import zdqd2, sgsqd

#导入破解滑块验证码
import geecrack

import configparser
path_default_sys = r'.\path\path_sys.ini'
path_default_chrome = r'.\Google\Chrome\Application\chromedriver.exe'

global is_head, max_cs

max_cs = 0

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
        self.master.title('主界面')
        self.master.geometry('384x323')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Option_forever.TRadiobutton',font=('宋体',9))
        self.Option_forever = Radiobutton(self.top, text='验证    次', variable = var_cs, value='cs_given', style='Option_forever.TRadiobutton')
        self.Option_forever.place(relx=0.521, rely=0.712, relwidth=0.226, relheight=0.072)

        self.Text_csVar = StringVar(value='3')
        self.Text_cs = Entry(self.top, text='3', textvariable=self.Text_csVar, font=('宋体',9))
        self.Text_cs.place(relx=0.639, rely=0.72, relwidth=0.049, relheight=0.056)

        self.style.configure('Option_forever.TRadiobutton',font=('宋体',9))
        self.Option_forever = Radiobutton(self.top, text='无限验证',variable = var_cs, value='cs_forever', style='Option_forever.TRadiobutton')
        self.Option_forever.place(relx=0.747, rely=0.712, relwidth=0.208, relheight=0.072)

        self.style.configure('Button_attention.TButton',font=('宋体',9))
        self.Button_attention = Button(self.top, text='注意事项', command=self.Button_attention_Cmd, style='Button_attention.TButton')
        self.Button_attention.place(relx=0.792, rely=0.599, relwidth=0.174, relheight=0.103)

        self.style.configure('Frame_zdqd.TLabelframe',font=('宋体',9))
        self.Frame_zdqd = LabelFrame(self.top, text='自动签到', style='Frame_zdqd.TLabelframe')
        self.Frame_zdqd.place(relx=0.035, rely=0.268, relwidth=0.938, relheight=0.206)

        self.style.configure('Frame_zdlz.TLabelframe',font=('宋体',9))
        self.Frame_zdlz = LabelFrame(self.top, text='自动领赞', style='Frame_zdlz.TLabelframe')
        self.Frame_zdlz.place(relx=0.035, rely=0.021, relwidth=0.938, relheight=0.227)

        self.style.configure('Button_reset.TButton',font=('宋体',9))
        self.Button_reset = Button(self.top, text='应用设置', command=self.Button_reset_Cmd, style='Button_reset.TButton')
        self.Button_reset.place(relx=0.208, rely=0.495, relwidth=0.174, relheight=0.103)

        self.List_infVar = StringVar(value='')
        self.List_infFont = Font(font=('宋体',9))
        self.List_inf = Listbox(self.top, listvariable=self.List_infVar, font=self.List_infFont)
        self.List_inf.place(relx=0.035, rely=0.784, relwidth=0.938, relheight=0.198)

        self.style.configure('Button_run.TButton',font=('宋体',9))
        self.Button_run = Button(self.top, text='运行程序', command=self.Button_run_Cmd, style='Button_run.TButton')
        self.Button_run.place(relx=0.035, rely=0.495, relwidth=0.174, relheight=0.103)

        self.style.configure('Button_sys.TButton',font=('宋体',9))
        self.Button_sys = Button(self.top, text='系统设置', command=self.Button_sys_Cmd, style='Button_sys.TButton')
        self.Button_sys.place(relx=0.792, rely=0.495, relwidth=0.174, relheight=0.103)

        self.style.configure('Button_inf.TButton',font=('宋体',9))
        self.Button_inf = Button(self.top, text='信息配置', command=self.Button_inf_Cmd, style='Button_inf.TButton')
        self.Button_inf.place(relx=0.618, rely=0.495, relwidth=0.174, relheight=0.103)

        self.style.configure('Label_inf.TLabel',anchor='w', font=('宋体',9))
        self.Label_inf = Label(self.top, text='程序日志', style='Label_inf.TLabel')
        self.Label_inf.place(relx=0.035, rely=0.733, relwidth=0.156, relheight=0.045)

        self.style.configure('Button_tools.TButton',font=('宋体',9))
        self.Button_tools = Button(self.top, text='开发工具', command=self.Button_tools_Cmd, style='Button_tools.TButton')
        self.Button_tools.place(relx=0.618, rely=0.599, relwidth=0.174, relheight=0.103)

        self.Check_zdqd1Var = StringVar(value='1')
        self.style.configure('Check_zdqd1.TCheckbutton',font=('宋体',9))
        self.Check_zdqd1 = Checkbutton(self.Frame_zdqd, text='自动签到1', variable=self.Check_zdqd1Var, style='Check_zdqd1.TCheckbutton')
        self.Check_zdqd1.place(relx=0.037, rely=0.2, relwidth=0.222, relheight=0.4)

        self.Check_zdqd2Var = StringVar(value='1')
        self.style.configure('Check_zdqd2.TCheckbutton',font=('宋体',9))
        self.Check_zdqd2 = Checkbutton(self.Frame_zdqd, text='自动签到2', variable=self.Check_zdqd2Var, style='Check_zdqd2.TCheckbutton')
        self.Check_zdqd2.place(relx=0.278, rely=0.2, relwidth=0.222, relheight=0.4)

        self.Check_sgsqdVar = StringVar(value='1')
        self.style.configure('Check_sgsqd.TCheckbutton',font=('宋体',9))
        self.Check_sgsqd = Checkbutton(self.Frame_zdqd, text='三国杀签到', variable=self.Check_sgsqdVar, style='Check_sgsqd.TCheckbutton')
        self.Check_sgsqd.place(relx=0.519, rely=0.2, relwidth=0.241, relheight=0.4)

        self.Check_zdlz6Var = StringVar(value='1')
        self.style.configure('Check_zdlz6.TCheckbutton',font=('宋体',9))
        self.Check_zdlz6 = Checkbutton(self.Frame_zdlz, text='自动领赞6', variable=self.Check_zdlz6Var, style='Check_zdlz6.TCheckbutton')
        self.Check_zdlz6.place(relx=0.278, rely=0.455, relwidth=0.222, relheight=0.318)

        self.Check_zdlz5Var = StringVar(value='1')
        self.style.configure('Check_zdlz5.TCheckbutton',font=('宋体',9))
        self.Check_zdlz5 = Checkbutton(self.Frame_zdlz, text='自动领赞5', variable=self.Check_zdlz5Var, style='Check_zdlz5.TCheckbutton')
        self.Check_zdlz5.place(relx=0.037, rely=0.455, relwidth=0.222, relheight=0.318)

        self.Check_zdlz4Var = StringVar(value='1')
        self.style.configure('Check_zdlz4.TCheckbutton',font=('宋体',9))
        self.Check_zdlz4 = Checkbutton(self.Frame_zdlz, text='自动领赞4', variable=self.Check_zdlz4Var, style='Check_zdlz4.TCheckbutton')
        self.Check_zdlz4.place(relx=0.759, rely=0.182, relwidth=0.222, relheight=0.318)

        self.Check_zdlz3Var = StringVar(value='1')
        self.style.configure('Check_zdlz3.TCheckbutton',font=('宋体',9))
        self.Check_zdlz3 = Checkbutton(self.Frame_zdlz, text='自动领赞3', variable=self.Check_zdlz3Var, style='Check_zdlz3.TCheckbutton')
        self.Check_zdlz3.place(relx=0.519, rely=0.182, relwidth=0.222, relheight=0.318)

        self.Check_zdlz2Var = StringVar(value='1')
        self.style.configure('Check_zdlz2.TCheckbutton',font=('宋体',9))
        self.Check_zdlz2 = Checkbutton(self.Frame_zdlz, text='自动领赞2', variable=self.Check_zdlz2Var, style='Check_zdlz2.TCheckbutton')
        self.Check_zdlz2.place(relx=0.278, rely=0.182, relwidth=0.222, relheight=0.318)

        self.Check_zdlz1Var = StringVar(value='1')
        self.style.configure('Check_zdlz1.TCheckbutton',font=('宋体',9))
        self.Check_zdlz1 = Checkbutton(self.Frame_zdlz, text='自动领赞1', variable=self.Check_zdlz1Var, style='Check_zdlz1.TCheckbutton')
        self.Check_zdlz1.place(relx=0.037, rely=0.182, relwidth=0.222, relheight=0.318)

        self.Check_is_headVar = StringVar(value='1')
        self.style.configure('Check_is_head.TCheckbutton',font=('宋体',9))
        self.Check_is_head = Checkbutton(self.top, text='浏览器后台运行', variable=self.Check_is_headVar, style='Check_is_head.TCheckbutton')
        self.Check_is_head.place(relx=0.035, rely=0.599, relwidth=0.278, relheight=0.083)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        self.config = configparser.ConfigParser() # 类实例化
        self.config.read(path_default_sys)
        try:self.path = self.config['path']['path_ini']
        except:
            tkinter.messagebox.showinfo('提示','欢迎使用本软件！\n默认配置已设置完毕，请关闭弹出窗口！\n请注意还需要配置账号密码才能正常使用！')
            Form_sys.Form_sys_main()
            self.config.read(path_default_sys)
            self.path = self.config['path']['path_ini']
            
    def select(self, event=None):
        global max_cs
        try:
            if var_cs.get() == 'cs_forever':
                max_cs = 999
            elif var_cs.get() == 'cs_given':
                max_cs = int(self.Text_cs.get())
            else:
                raise
            return 1
        except: 
            tkinter.messagebox.showerror('错误','验证次数配置错误！')
            return 0


    def Button_reset_Cmd(self, event=None):
        self.__init__()
        self.List_inf.delete(0, END)
        self.List_inf.insert(END, '已成功应用新设置！')

    def Button_run_Cmd(self, event=None):
        global max_cs, is_head
        self.List_inf.delete(0, END)
        
        self.config.read(path_default_sys)
        self.path = self.config['path']['path_ini']
        self.offset_ = int(self.config['path']['offset_correction'])
        
        if self.Check_is_headVar.get() == '1': is_head = 0
        else: is_head = 1
        
        if self.select():
            try:
                if self.Check_zdlz1Var.get() == '1': 
                    self.List_inf.insert(END, "自动领赞1运行中，账号：" + self.config['path_lz']['username'])
                    if self.config['path_lz']['username'] == '' or self.config['path_lz']['password'] == '': raise
                    infor_zdlz1, is_success_zdlz1 = zdlz1.main(max_cs, is_head, self.offset_)
                    if is_success_zdlz1: self.Check_zdlz1Var.set(0)
                    for infor in infor_zdlz1:
                        self.List_inf.insert(END, infor)
                        
                        
                if self.Check_sgsqdVar.get() == '1': 
                    self.List_inf.insert(END, "三国杀签到运行中，账号：" + self.config['path_4399']['username'])
                    if self.config['path_4399']['username'] == '' or self.config['path_4399']['password'] == '': raise
                    infor_sgsqd, is_success_sgsqd = sgsqd.main(is_head)
                    if is_success_sgsqd: self.Check_sgsqdVar.set(0)
                    for infor in infor_sgsqd:
                        self.List_inf.insert(END, infor)    
    
                if self.Check_zdlz3Var.get() == '1': 
                    self.List_inf.insert(END, "自动领赞3运行中，账号：" + self.config['QQ_path']['QQ'])
                    if self.config['QQ_path']['QQ'] == '': raise
                    infor_zdlz3, is_success_zdlz3 = zdlz3.main(max_cs, is_head, self.offset_)
                    if is_success_zdlz3: self.Check_zdlz3Var.set(0)
                    for infor in infor_zdlz3:
                        self.List_inf.insert(END, infor)     
            
                if self.Check_zdqd2Var.get() == '1': 
                    self.List_inf.insert(END, "自动签到2运行中，账号：" + self.config['path_lz']['username'])
                    if self.config['path_lz']['username'] == '' or self.config['path_lz']['password'] == '': raise
                    infor_zdqd2, is_success_zdqd2 = zdqd2.main(is_head)
                    if is_success_zdqd2: self.Check_zdqd2Var.set(0)
                    for infor in infor_zdqd2:
                        self.List_inf.insert(END, infor) 
           
            
       
        
       
            except:
                tkinter.messagebox.showerror('错误','出错了，请联系开发者QQ408029164！')
        
    def Button_sys_Cmd(self, event=None):
        Form_sys.Form_sys_main()

    def Button_inf_Cmd(self, event=None):
        Form_inf.Form_inf_main()

    def Button_attention_Cmd(self, event=None):
        Form_attention.Form_attention_main()

    def Button_tools_Cmd(self, event=None):
        Form_tools.Form_tools_main()
    
def Form_main_main():
    if __name__ == "__main__": top = Tk()
    else: 
        top = Toplevel()
        top.wm_attributes('-topmost',1)
    global var_cs
    var_cs = StringVar()
    var_cs.set("cs_given")
    Application(top).mainloop()
    try: top.destroy()
    except: pass
        
if __name__ == "__main__":
    Form_main_main()