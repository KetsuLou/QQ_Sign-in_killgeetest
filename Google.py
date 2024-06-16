import time, os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import def_killgeetest
import waitalert
import configparser
#http://www.dayuaa.cn/?cid=86&tid=1941


def main(max_cs, is_test, is_head, offset_):
    #设置请求头
    headers=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")

    config = configparser.ConfigParser() # 类实例化
    path_default_sys = r'.\path\path_sys.ini'
    path_default_chrome = r'.\Google\Chrome\Application\chromedriver.exe'
    config.read(path_default_sys)
    path = config['path']['path_ini']
    config.read(path)
        
    #打开一个Chrome浏览器
    if is_head:
        #浏览器显示
        #driver = webdriver.Chrome(config['path']['path_chrome']) #还可以指定路径
        chrome_path = config['path']['path_chrome']
        option = webdriver.ChromeOptions()
        option.add_argument(r"user-data-dir=C:\Users\40802\AppData\Local\Google\Chrome\User Data")
        driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=option)
    else:
        #无头模式
        chrome_path = config['path']['path_chrome']
        option = webdriver.ChromeOptions()
        option.add_argument('headless') # 设置option
        driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=option)
        
    driver.get(r'https://s.taobao.com/search?q=%E6%8B%8D%E5%8D%96&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.1000386.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306')

if __name__ == "__main__":
    print(main(10, 0, 1, -2))