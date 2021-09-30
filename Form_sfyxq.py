#!/usr/bin/env python
#-*- coding:utf-8 -*-
import time, sys, os, random, tkinter
import Form_webset, Form_sfyzh
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

#https://www.geetest.com/show
#临时修改环境变量
base_dir=os.path.dirname(__file__)
sys.path.append(base_dir)

path_default_sys = r'.\path\path_sys.ini'
#path_default_chrome = r'..\Google\Chrome\Application\chromedriver.exe'

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

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('三丰云续期')
        self.master.geometry('363x244')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Button_sfyzh.TButton',font=('宋体',9))
        self.Button_sfyzh = Button(self.top, text='三丰云配置', command=self.Button_sfyzh_Cmd, style='Button_sfyzh.TButton')
        self.Button_sfyzh.place(relx=0.749, rely=0.642, relwidth=0.229, relheight=0.102)

        self.style.configure('Button_save.TButton',font=('宋体',9))
        self.Button_save = Button(self.top, text='保存', command=self.Button_save_Cmd, style='Button_save.TButton')
        self.Button_save.place(relx=0.749, rely=0.459, relwidth=0.11, relheight=0.135)

        self.style.configure('Button_rand.TButton',font=('宋体',9))
        self.Button_rand = Button(self.top, text='随机', command=self.Button_rand_Cmd, style='Button_rand.TButton')
        self.Button_rand.place(relx=0.837, rely=0.787, relwidth=0.14, relheight=0.082)

        self.style.configure('Button_cdimg.TButton',font=('宋体',9))
        self.Button_cdimg = Button(self.top, text='浏览', command=self.Button_cdimg_Cmd, style='Button_cdimg.TButton')
        self.Button_cdimg.place(relx=0.837, rely=0.885, relwidth=0.14, relheight=0.082)

        self.style.configure('Button_inf.TButton',font=('宋体',9))
        self.Button_inf = Button(self.top, text='信息配置', command=self.Button_inf_Cmd, style='Button_inf.TButton')
        self.Button_inf.place(relx=0.507, rely=0.459, relwidth=0.229, relheight=0.137)

        self.style.configure('Button_quit.TButton',font=('宋体',9))
        self.Button_quit = Button(self.top, text='关闭', command=self.Button_quit_Cmd, style='Button_quit.TButton')
        self.Button_quit.place(relx=0.865, rely=0.459, relwidth=0.113, relheight=0.135)

        self.Text_imgVar = StringVar(value='')
        self.Text_img = Entry(self.top, textvariable=self.Text_imgVar, font=('宋体',9))
        self.Text_img.place(relx=0.22, rely=0.885, relwidth=0.598, relheight=0.082)

        self.Text_webVar = StringVar(value='')
        self.Text_web = Entry(self.top, textvariable=self.Text_webVar, font=('宋体',9))
        self.Text_web.place(relx=0.22, rely=0.787, relwidth=0.598, relheight=0.082)

        self.style.configure('Button_cs.TButton',font=('宋体',9))
        self.Button_cs = Button(self.top, text='云服务器续约', command=self.Button_cs_Cmd, style='Button_cs.TButton')
        self.Button_cs.place(relx=0.022, rely=0.459, relwidth=0.229, relheight=0.137)

        self.style.configure('Button_vh.TButton',font=('宋体',9))
        self.Button_vh = Button(self.top, text='虚拟主机续约', command=self.Button_vh_Cmd, style='Button_vh.TButton')
        self.Button_vh.place(relx=0.264, rely=0.459, relwidth=0.229, relheight=0.137)

        self.style.configure('Label_img.TLabel',anchor='w', font=('宋体',9))
        self.Label_img = Label(self.top, text='本地图片：', style='Label_img.TLabel')
        self.Label_img.place(relx=0.022, rely=0.885, relwidth=0.185, relheight=0.07)

        self.style.configure('Label_web.TLabel',anchor='w', font=('宋体',9))
        self.Label_web = Label(self.top, text='发帖网址：', style='Label_web.TLabel')
        self.Label_web.place(relx=0.022, rely=0.787, relwidth=0.185, relheight=0.07)

        self.style.configure('Label_inf.TLabel',anchor='w', font=('宋体',9))
        self.Label_inf = Label(self.top, text='text', style='Label_inf.TLabel')
        self.Label_inf.place(relx=0.022, rely=0.033, relwidth=0.959, relheight=0.377)

        self.Check_is_headVar = StringVar(value='1')
        self.style.configure('Check_is_head.TCheckbutton',font=('宋体',9))
        self.Check_is_head = Checkbutton(self.top, text='浏览器后台运行', variable=self.Check_is_headVar, style='Check_is_head.TCheckbutton')
        self.Check_is_head.place(relx=0.022, rely=0.628, relwidth=0.294, relheight=0.109)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        self.Label_inf.config(text = message)
        self.config = configparser.ConfigParser() # 类实例化
        self.config.read(path_default_sys)
        self.path = self.config['path']['path_ini']
        #读取配置ini信息，没有对应的Section则新建
        try:
            self.config.read(self.path)
            try:
                self.config.add_section('path_sfy')
                self.config.set('path_sfy', 'sfyweb', 'https://zhuanlan.zhihu.com/p/301243397')
                self.config.set('path_sfy', 'sfyimg', os.getcwd() + '\\path\\sfyimg.png')
            except:
                pass
            self.config.write(open(path_default_sys, 'r+'))
            #显示信息
            self.Text_web.insert(0, self.config['path_sfy']['sfyweb'])
            self.Text_img.insert(0, self.config['path_sfy']['sfyimg'])

        except:
            tkinter.messagebox.showerror('错误','配置加载错误！')     

    
    def Button_cs_Cmd(self, event=None):
        self.config.read(self.path)
        if self.Check_is_headVar.get() == '1': is_head = 0
        else: is_head = 1
        if is_head:
            #浏览器显示
            self.driver = webdriver.Chrome(self.config['path']['path_chrome']) #还可以指定路径
        else:
            #无头模式
            chrome_path = self.config['path']['path_chrome']
            option = webdriver.ChromeOptions()
            option.add_argument('headless') # 设置option
            self.driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=option)
        
        driver = self.driver
        
        url_index = 'https://www.sanfengyun.com/login/'
        driver.get(url_index)
        try:
            WebDriverWait(driver, 2, 0.1).until(lambda x: x.find_element_by_xpath("//*[@name='username']")).send_keys(self.config['path_sfy']['username'])
            #WebDriverWait(driver, 2, 0.1).until(lambda x: x.find_element_by_xpath("//*[@name='username']")).send_keys('13136104733')
            WebDriverWait(driver, 2, 0.1).until(lambda x: x.find_element_by_xpath("//*[@name='password']")).send_keys(self.config['path_sfy']['password'])
            #WebDriverWait(driver, 2, 0.1).until(lambda x: x.find_element_by_xpath("//*[@name='password']")).send_keys('LJJljj123')
            WebDriverWait(driver, 2, 0.1).until(lambda x: x.find_element_by_xpath("//*[@id='loginSubmit']")).click()
            time.sleep(0.5)
            driver.get(self.config['web']['sfycs'])
            #WebDriverWait(driver, 2, 0.1).until(lambda x: x.find_element_by_xpath("//*[@id='tab-seven']")).click()
            WebDriverWait(driver, 2, 0.1).until(lambda x: x.find_element_by_xpath("//*[@class='el-button el-button--primary el-button--small']/span[text()='免费延期']")).click()
            WebDriverWait(driver, 2, 0.1).until(lambda x: x.find_element_by_xpath("//*[@class='el-input el-input--small']/input[@placeholder='请输入发帖网址http://']")).send_keys(self.Text_web.get())
            WebDriverWait(driver, 2, 0.1).until(lambda x: x.find_element_by_xpath("//*[@id='fileImg1']")).send_keys(self.Text_img.get().replace('\\',"/"))
            WebDriverWait(driver, 2, 0.1).until(lambda x: x.find_element_by_xpath("//*[@class='el-button z-margin-top-20-precent el-button--primary el-button--small']")).click()
        except:
            #未到续期时间
            try: 
                inf = WebDriverWait(driver, 2, 0.1).until(lambda x: x.find_element_by_xpath("//*[@class='delaybox']")).text
                tkinter.messagebox.showinfo('提示', inf)
            except:
                tkinter.messagebox.showerror('错误','出错了！')
    '''
    def Button_cs_Cmd(self, event=None):
        self.driver = webdriver.Chrome(self.config['path']['path_chrome'])
        driver = self.driver
        driver.get(os.getcwd()+'\\test.html')
        WebDriverWait(driver, 2, 0.1).until(lambda x: x.find_element_by_xpath("//*[@id='file']")).send_keys(self.Text_img.get().replace('\\',"/"))
    '''  
    
    def Button_vh_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Button_inf_Cmd(self, event=None):
        Form_webset.Form_webset_main()

    def Button_cdimg_Cmd(self, event=None):
        file_path_img = filedialog.askopenfilename(initialfile = 'sfyimg.png', initialdir='.', filetypes=[('所有文件', '*')], title='请选择需要上传的图片')
        if file_path_img != '':
            self.Text_img.delete(0, END)
            self.Text_img.insert(0, str(file_path_img).replace('/',"\\"))

    def Button_rand_Cmd(self, event=None):
        self.Text_web.delete(0, END)
        self.Text_web.insert(0, 'https://zhuanlan.zhihu.com/p/' + str(int(random.random()*200000000)))

    def Button_save_Cmd(self, event=None):
        try:
            self.path = self.config['path']['path_ini']
            self.config.read(path_default_sys)
            #date = config.add_section("path")
            #写入数据
            self.config.set('path_sfy','sfyweb', self.Text_web.get())
            self.config.set('path_sfy','sfyimg', self.Text_img.get())
            #保存数据
            #with open(path_default_sys , 'w') as f:f.close()
            self.config.write(open(path_default_sys, 'w'))
            tkinter.messagebox.showinfo('提示','保存成功！')
        except:
            tkinter.messagebox.showerror('错误','保存出错！')


    def Button_sfyzh_Cmd(self, event=None):
        Form_sfyzh.Form_sfyzh_main()

    def Button_quit_Cmd(self, event=None):
        try:
            self.driver.quit()
            try: os.system('taskkill /im chromedriver.exe /F')
            except: pass
            tkinter.messagebox.showinfo('提示', '浏览器已关闭！开发工具即将退出！')
        except:
            pass
        self.master.destroy()
            
def Form_sfyxq_main():
    if __name__ == "__main__": top = Tk()
    else: 
        top = Toplevel()
        top.wm_attributes('-topmost',1)

    global message
    message = "注意：\n" + \
            "1.三丰云云服务器续约。\n" + \
            "2.三丰云虚拟主机续约。（待完善）"  
            
    Application(top).mainloop()
    try: top.destroy()
    except: pass

if __name__ == "__main__":
    Form_sfyxq_main()