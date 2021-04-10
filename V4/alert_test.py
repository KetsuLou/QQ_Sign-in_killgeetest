import time, os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import waitalert

import configparser
#https://www.qvvvvv.com/?cid=1&tid=309


#设置请求头
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")

config = configparser.ConfigParser() # 类实例化
path_default_sys = r'.\path\path_sys.ini'
path_default_chrome = r'.\Google\Chrome\Application\chromedriver.exe'
config.read(path_default_sys)
path = config['path']['path_ini']
config.read(path)
    
#打开一个Chrome浏览器
driver = webdriver.Chrome(config['path']['path_chrome']) #还可以指定路径

    
all_infor = []
is_success = False
# 请求网站
url = r'E:\desk\life\my python\自动填入网站（未完成\python\V4\test.html'
driver.get(url)
WebDriverWait(driver, 3, 0.1).until(lambda x: x.find_element_by_xpath('//*[@onclick="duihua()"]')).click()
try:
    alert = waitalert.waitalert(driver, 6, 0.1)
    #获取警告对话框的内容
    infor = alert.text
    #alert对话框属于警告对话框，我们这里只能接受弹窗
    alert.accept()
    time.sleep(1)
except: infor = ''
print('infor=%s' %infor)
driver.close()
try: os.system('taskkill /im chromedriver.exe /F')
except: pass