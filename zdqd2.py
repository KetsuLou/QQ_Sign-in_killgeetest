import time, os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import configparser
#http://www.dsw.zfanw.cn/user/login.php
#http://www.dsw.zfanw.cn/user/qiandao.php

def main(is_test, is_head):
    #设置请求头
    headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    
    config = configparser.ConfigParser() # 类实例化
    path_default_sys = r'.\path\path_sys.ini'
    path_default_chrome = r'.\Google\Chrome\Application\chromedriver.exe'
    config.read(path_default_sys)
    path = config['path']['path_ini']
    config.read(path)
    
    #打开一个Chrome浏览器
    if is_head:
        #浏览器显示
        driver = webdriver.Chrome(config['path']['path_chrome']) #还可以指定路径
    else:
        #无头模式
        chrome_path = config['path']['path_chrome']
        option=webdriver.ChromeOptions()
        option.add_argument('headless') # 设置option
        driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=option)
        
    # 请求网站
    url1 = 'http://www.dsw.zfanw.cn/user/login.php'
    url2 = 'http://www.dsw.zfanw.cn/user/qiandao.php'
    
    all_infor = []
    is_success = False

    try:
        #网页被拦截
        i = 0
        while 'dsw.zfanw.cn/user' not in driver.current_url and i < 10:
            driver.get(url1)
            try: 
                if driver.find_element_by_xpath("//h2/b").text == '用户登录': break
            except: pass
            time.sleep(1)
            i += 1
        #网页刷新
        WebDriverWait(driver, 3, 0.1).until(lambda x: x.find_element_by_xpath("//h2/b"))
        '''
        while True:
            try: 
                if driver.find_element_by_xpath("//h2/b").text == '用户登录': break
            except: pass
        '''
        #登录
        try:
            WebDriverWait(driver, 2, 0.1).until(lambda x: x.find_element_by_xpath("//*[@class='btn btn-info btn-block']")).click()#签到
        except:
            #未登录时
            WebDriverWait(driver, 2, 0.1).until(lambda x: x.find_element_by_xpath("//*[@name='user']")).send_keys(config['path_lz']['username'])
            driver.find_element_by_xpath("//*[@name='pass']").send_keys(config['path_lz']['password'])

            #登录
            driver.find_element_by_xpath("//*[@class = 'btn btn-primary btn-block']").click()
        try:
            #密码错误
            infor = WebDriverWait(driver, 3, 0.1).until(lambda x: x.find_element_by_xpath("//*[@class='layui-layer-content layui-layer-padding']")).text
            if '密码错误' in infor: pwd = False
            else: raise
        except:
            pwd = True
            pass
        if not pwd:
            raise

        #签到
        driver.get(url2)
        try:
            i = 0
            #print(driver.current_url)
            while 'dsw.zfanw.cn/user/qiandao' not in driver.current_url and i < 10:
                driver.get(url2)
                time.sleep(1)
                i += 1
        except: pass
        try:
            try:
                infor = WebDriverWait(driver, 2, 0.1).until(lambda x: x.find_element_by_xpath("//span[@style='font-size:16px']/b")).text
                if '已签到' in infor: is_success = True
                else: raise
            except:
                WebDriverWait(driver, 2, 0.1).until(lambda x: x.find_element_by_xpath("//*[@class='btn btn-info btn-block']")).click()
                infor = WebDriverWait(driver, 3, 0.6).until(lambda x: x.find_element_by_xpath("//*[@class='layui-layer-content layui-layer-padding']")).text
                #time.sleep(1)
            if '签到成功' in infor or '已经签到' in infor: is_success = True
            all_infor += [url2, infor]
        except:
            infor = "签到失败！"
            all_infor += [url2, infor]
            
    except:
        try: 
            if not pwd: all_infor += [url2, infor]
            else: all_infor += ["程序出错"]
        except:
            all_infor += ["程序出错"]
    

    if not is_test:
        driver.close()
        try: os.system('taskkill /im chromedriver.exe /F')
        except: pass
    all_infor += ['\n']
    return all_infor, is_success

if __name__ == "__main__":
    print(main(0, 1))