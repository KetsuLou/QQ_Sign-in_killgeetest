#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time, sys, os, tkinter
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#临时修改环境变量
base_dir=os.path.dirname(__file__)
sys.path.append(base_dir)

path_default_sys = r'.\path\path_sys.ini'
path_default_chrome = r'.\Google\Chrome\Application\chromedriver.exe'

import geecrack, configparser
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

global driver

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('geetest验证杀手')
        self.master.geometry('304x223')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Button_saveoffset.TButton',font=('宋体',9))
        self.Button_saveoffset = Button(self.top, text='保存', command=self.Button_saveoffset_Cmd, style='Button_saveoffset.TButton')
        self.Button_saveoffset.place(relx=0.658, rely=0.801, relwidth=0.115, relheight=0.09)

        self.style.configure('Button_quit.TButton',font=('宋体',9))
        self.Button_quit = Button(self.top, text='关闭界面', command=self.Button_quit_Cmd, style='Button_quit.TButton')
        self.Button_quit.place(relx=0.636, rely=0.61, relwidth=0.273, relheight=0.149)

        self.Text_offsetVar = StringVar(value='')
        self.Text_offset = Entry(self.top, textvariable=self.Text_offsetVar, font=('宋体',9))
        self.Text_offset.place(relx=0.548, rely=0.813, relwidth=0.077, relheight=0.081)

        self.style.configure('Button_geetest.TButton',font=('宋体',9))
        self.Button_geetest = Button(self.top, text='geetest杀手', command=self.Button_geetest_Cmd, style='Button_geetest.TButton')
        self.Button_geetest.place(relx=0.351, rely=0.61, relwidth=0.273, relheight=0.149)

        self.style.configure('Button_chrome.TButton',font=('宋体',9))
        self.Button_chrome = Button(self.top, text='打开浏览器', command=self.Button_chrome_Cmd, style='Button_chrome.TButton')
        self.Button_chrome.place(relx=0.066, rely=0.61, relwidth=0.273, relheight=0.149)

        self.style.configure('Label_setoffset.TLabel',anchor='w', font=('宋体',9))
        self.Label_setoffset = Label(self.top, text='滑块偏移量设置：', style='Label_setoffset.TLabel')
        self.Label_setoffset.place(relx=0.219, rely=0.795, relwidth=0.319, relheight=0.112)

        self.style.configure('Label_inf.TLabel',anchor='w', font=('宋体',9))
        self.Label_inf = Label(self.top, text='文本', style='Label_inf.TLabel')
        self.Label_inf.place(relx=0.066, rely=0.072, relwidth=0.878, relheight=0.435)

class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        self.Label_inf.config(text = message)
        self.config = configparser.ConfigParser() # 类实例化
        self.config.read(path_default_sys)
        self.path = self.config['path']['path_ini']
        self.config.read(self.path)
        try: self.Text_offset.insert(0, self.config['path']['offset_correction'])
        except: self.Text_offset.insert(0, '0')

    def Button_chrome_Cmd(self, event=None):
        self.driver = webdriver.Chrome(self.config['path']['path_chrome'])
        
        url = 'https://www.geetest.com/show'
        self.driver.get(url)
        locator = (By.LINK_TEXT, 'CSDN')
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='tab-item tab-item-1']"))).click()
       
    def Button_geetest_Cmd(self, event=None):
        try:
            try:
                WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_xpath("//div[@class='geetest_radar_tip']")).click()
                time.sleep(1.5)
            except: pass
            geecrack.main(self.driver, 30, int(self.Text_offset.get()))
            try:
                text = WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_xpath("//div[@class='geetest_success_radar_tip']/span")).text
                if text != '': tkinter.messagebox.showinfo('提示', text)
            except:
                pass
        except:
            tkinter.messagebox.showerror('错误','出错了！')

    def Button_quit_Cmd(self, event=None):
        try:
            self.driver.close()
            try: os.system('taskkill /im chromedriver.exe /F')
            except: pass
            tkinter.messagebox.showinfo('提示', '浏览器已关闭！开发工具即将退出！')
        except:
            pass
        self.master.destroy()

    def Button_saveoffset_Cmd(self, event=None):
        try:
            self.config.add_section('path')
            self.config.set('path', 'offset_correction', '')
        except: pass
        try:
            self.config.set('path', 'offset_correction', self.Text_offset.get())
            self.config.write(open(self.path, 'r+'))
            tkinter.messagebox.showinfo('提示','偏移量修正保存成功！')
        except: tkinter.messagebox.showerror('错误','偏移量修正保存出错！')
     
        
def Form_killgeetest_main():
    if __name__ == "__main__": top = Tk()
    else: 
        top = Toplevel()
        top.wm_attributes('-topmost',1)

    global message
    message = "注意：\n" + \
            "1.首先点击按钮打开配置好的浏览器。\n" + \
            "2.程序会自动访问指定网址。\n" + \
            "3.按下geetest杀手按钮进行滑块认证。\n" + \
            "4.默认滑块偏移量为0，可根据实际效果进\n" + \
            "  行滑块偏移量的增减。\n" + \
            "5.程序未响应系正常现象。"    
            
    Application(top).mainloop()
    try: top.destroy()
    except: pass

if __name__ == "__main__":
    Form_killgeetest_main()