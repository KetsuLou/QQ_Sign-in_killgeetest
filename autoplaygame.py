import time, os, sys
from autokeyboard import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
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
    from tkinter import filedialog
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('自动游戏')
        self.master.geometry('232x130')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.Text_goalVar = StringVar(value='599')
        self.Text_goal = Entry(self.top, textvariable=self.Text_goalVar, font=('宋体',9))
        self.Text_goal.place(relx=0.069, rely=0.297, relwidth=0.841, relheight=0.154)

        self.style.configure('Label_goal.TLabel',anchor='w', font=('宋体',12))
        self.Label_goal = Label(self.top, text='请设置分数：', style='Label_goal.TLabel')
        self.Label_goal.place(relx=0.069, rely=0.123, relwidth=0.418, relheight=0.154)

        self.style.configure('Button_run.TButton',font=('宋体',9))
        self.Button_run = Button(self.top, text='运行程序', command=self.Button_run_Cmd, style='Button_run.TButton')
        self.Button_run.place(relx=0.552, rely=0.615, relwidth=0.287, relheight=0.256)

        self.style.configure('Button_web.TButton',font=('宋体',9))
        self.Button_web = Button(self.top, text='打开网页', command=self.Button_web_Cmd, style='Button_web.TButton')
        self.Button_web.place(relx=0.172, rely=0.615, relwidth=0.287, relheight=0.256)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        #设置请求头
        self.headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
        self.config = configparser.ConfigParser() # 类实例化
        self.path_default_sys = r'.\path\path_sys.ini'
        self.path_default_chrome = r'.\Google\Chrome\Application\chromedriver.exe'
        self.config.read(self.path_default_sys)
        self.path = self.config['path']['path_ini']
        self.config.read(self.path)

    def Button_web_Cmd(self, event=None):
        #打开一个Chrome浏览器
        #浏览器显示
        self.driver = webdriver.Chrome(self.config['path']['path_chrome']) #还可以指定路径
        
        #请求网站
        url1 = 'http://my.4399.com/forums/mtag-78097'
        url2 = 'http://my.4399.com/events/2021/twelveyear/index?s=78097'
    
        try:
            driver = self.driver
            driver.get(url1)
            driver.switch_to_frame('popup_login_frame')#先跳转到iframe框架
            #登录
            try:
                driver.find_element_by_xpath("//div[@class = 'sign_group']/a").click()#签到
            except:
                #未登录时
                WebDriverWait(driver, 2, 0.1).until(lambda x: x.find_element_by_name('username')).send_keys(self.config['path_4399']['username'])
                #username = driver.find_element_by_name('username').send_keys(config['path_4399']['username'])
                driver.find_element_by_id('j-password').send_keys(self.config['path_4399']['password'])
               
                #登录
                driver.find_element_by_xpath("//div[@class = 'login_hor ux_login clearfix']/input").click()
            try:
                #密码错误
                infor = WebDriverWait(driver, 1, 0.1).until(lambda x: x.find_element_by_xpath("//div[@id = 'Msg']")).text
                pwd = False
            except:
                pwd = True
                pass
            if not pwd:
                raise
            driver.switch_to.default_content()
    
            #game start
            driver.get(url2)
            tkinter.messagebox.showinfo('提示', '打开网站成功！')
        except:
            if not pwd: pass
            else: infor = "程序出错"
            tkinter.messagebox.showinfo('提示', infor)
    
    def Button_run_Cmd(self, event=None):
        driver = self.driver
        tkinter.messagebox.showinfo('提示', '确认后脚本将在2s后开始，\n请确保网页在最前端显示！')
        time.sleep(2)
        goal = int(self.Text_goal.get())
        show = ''
        while goal > 0:
            key = WebDriverWait(driver, 1, 0.005).until(lambda x: x.find_element_by_xpath("//*[@class='g_row g_row_waiting g_active']/span[@class='g_block g_block_b']")).get_attribute('bid')
            if key == '1': key_press('A')
            elif key == '2': key_press('S')
            elif key == '3': key_press('D')
            elif key == '4': key_press('F')
            else: raise
            if goal % 10 == 0:
                show = driver.find_element_by_xpath("//*[@id='game_over_panel']").get_attribute('style')
            if show == 'display: block;': break
            goal -= 1
        tkinter.messagebox.showinfo('提示', '游戏结束！')
            
def Form_autoplaygame_main():
    if __name__ == "__main__": top = Tk()
    else: 
        top = Toplevel()
        top.wm_attributes('-topmost',1)
    Application(top).mainloop()
    try: top.destroy()
    except: pass

if __name__ == "__main__":
    Form_autoplaygame_main()