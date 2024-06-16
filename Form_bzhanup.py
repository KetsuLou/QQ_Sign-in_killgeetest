#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time, sys, os, tkinter
import Form_webset
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

#https://www.geetest.com/show
#临时修改环境变量
base_dir=os.path.dirname(__file__)
sys.path.append(base_dir)

path_default_sys = r'.\path\path_sys.ini'
path_default_chrome = r'..\Google\Chrome\Application\chromedriver.exe'

import configparser
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
        self.master.title('B站刷经验')
        self.master.geometry('304x223')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()
        
        self.style.configure('Label_inf.TLabel',anchor='w', font=('宋体',9))
        self.Label_inf = Label(self.top, text='文本', style='Label_inf.TLabel')
        self.Label_inf.place(relx=0.066, rely=0.072, relwidth=0.878, relheight=0.435)

        self.style.configure('Button_chrome.TButton',font=('宋体',9))
        self.Button_chrome = Button(self.top, text='打开浏览器', command=self.Button_chrome_Cmd, style='Button_chrome.TButton')
        self.Button_chrome.place(relx=0.066, rely=0.61, relwidth=0.273, relheight=0.149)

        self.style.configure('Button_quit.TButton',font=('宋体',9))
        self.Button_quit = Button(self.top, text='关闭界面', command=self.Button_quit_Cmd, style='Button_quit.TButton')
        self.Button_quit.place(relx=0.636, rely=0.61, relwidth=0.273, relheight=0.149)

        self.style.configure('Button_bzhanup.TButton',font=('宋体',9))
        self.Button_bzhanup = Button(self.top, text='开始刷经验', command=self.Button_bzhanup_Cmd, style='Button_bzhanup.TButton')
        self.Button_bzhanup.place(relx=0.351, rely=0.61, relwidth=0.273, relheight=0.149)
        
        self.style.configure('Label_setoffset.TLabel',anchor='w', font=('宋体',9))
        self.Label_setoffset = Label(self.top, text='QQ：', style='Label_setoffset.TLabel')
        self.Label_setoffset.place(relx=0.198, rely=0.785, relwidth=0.319, relheight=0.112)
        
        self.Text_QQVar = StringVar(value='')
        self.Text_QQ = Entry(self.top, textvariable=self.Text_QQVar, font=('宋体',9))
        self.Text_QQ.place(relx=0.298, rely=0.803, relwidth=0.277, relheight=0.081)
        
        self.style.configure('Button_inf.TButton',font=('宋体',9))
        self.Button_inf = Button(self.top, text='信息配置', command=self.Button_inf_Cmd, style='Button_inf.TButton')
        self.Button_inf.place(relx=0.636, rely=0.767, relwidth=0.273, relheight=0.149)
        
class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        self.Label_inf.config(text = message)
        self.config = configparser.ConfigParser() # 类实例化
        self.config.read(path_default_sys)
        self.path = self.config['path']['path_ini']
        self.config.read(self.path)
        try: self.Text_QQ.insert(0, self.config['QQ_path']['qq'])
        except: self.Text_QQ.insert(0, '')

    def Button_chrome_Cmd(self, event=None):
        self.driver = webdriver.Chrome(self.config['path']['path_chrome'])
        
        
        url = 'https://www.bilibili.com'
        self.driver.get(url)
        WebDriverWait(self.driver, 3, 0.15).until(lambda x: x.find_element_by_xpath('//*[@class="unlogin-avatar"]')).click()
        # hand = self.driver.window_handles#获取当前的所有句柄
        self.driver.switch_to_window(self.driver.window_handles[1])#转换窗口至最高的句柄
        WebDriverWait(self.driver, 3, 0.15).until(lambda x: x.find_element_by_xpath('//*[@class="btn qq"]')).click()
        self.driver.switch_to_window(self.driver.window_handles[1])#转换窗口至最高的句柄
        try: 
            time.sleep(2)
            #self.driver.get(self.driver.current_url)
            self.driver.switch_to_frame('ptlogin_iframe')#先跳转到iframe框架
        except: pass
        WebDriverWait(self.driver, 6, 0.15).until(lambda x: x.find_element_by_xpath('//*[@id="img_out_'+self.Text_QQ.get()+'"]')).click()
        self.driver.switch_to_window(self.driver.window_handles[1])#转换窗口至最高的句柄
       
    def Button_bzhanup_Cmd(self, event=None):
        try:
            def_killgeetest.main(self.driver, int(self.Text_QQ.get()))
            try:
                text = WebDriverWait(self.driver, 3, 0.15).until(lambda x: x.find_element_by_xpath("//div[@class='geetest_success_radar_tip']/span")).text
                if text != '': tkinter.messagebox.showinfo('提示', text)
            except:
                pass
        except:
            tkinter.messagebox.showerror('错误','出错了！')

    def Button_quit_Cmd(self, event=None):
        try:
            self.driver.quit()
            try: os.system('taskkill /im chromedriver.exe /F')
            except: pass
            tkinter.messagebox.showinfo('提示', '浏览器已关闭！开发工具即将退出！')
        except:
            pass
        self.master.destroy()
        
    def Button_inf_Cmd(self, event=None):
        Form_webset.Form_webset_main()
        
def Form_bzhanup_main():
    if __name__ == "__main__": top = Tk()
    else: 
        top = Toplevel()
        top.wm_attributes('-topmost',1)

    global message
    message = "注意：\n" + \
            "1.首先记得登录QQ。\n" + \
            "2.首先点击按钮打开配置好的浏览器。\n" + \
            "3.程序会自动访问指定网址。\n" + \
            "4.按下按钮开始刷经验。\n" + \
            "5.程序未响应系正常现象。"    
            
    Application(top).mainloop()
    try: top.destroy()
    except: pass

if __name__ == "__main__":
    Form_bzhanup_main()