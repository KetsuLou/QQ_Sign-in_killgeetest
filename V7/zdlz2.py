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
    url1 = url2 = config['web']['zdlz2']
    '''
    url1 = 'http://www.dsw.zfanw.cn/user/login.php'
    url2 = 'http://www.dsw.zfanw.cn/user/shop.php?cid=25&tid=330'
    '''
    
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

        #领赞
        driver.get(url2)
        try:
            i = 0
            #print(driver.current_url)
            while 'dsw.zfanw.cn/user/shop.php?cid' not in driver.current_url and i < 10:
                driver.get(url2)
                time.sleep(1)
                i += 1
        except: pass
        try:
            while True: driver.find_element_by_xpath("//*[@class='layui-layer-content layui-layer-loading2']")
        except: pass
        driver.find_element_by_xpath("//*[@class='layui-layer-btn0']").click()
        driver.find_element_by_name('inputvalue').send_keys(config['QQ_path']['QQ'])
        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
        try:
            while True: driver.find_element_by_xpath("//*[@class='layui-layer-content layui-layer-loading2']")
        except: pass
        #infor = WebDriverWait(driver, 3, 0.1).until(lambda x: x.find_element_by_xpath('//*[@class = "layui-layer-content layui-layer-padding"]')).text
        WebDriverWait(driver, 3, 0.1).until(lambda x: x.find_element_by_xpath('//*[@class = "layui-layer-btn layui-layer-btn-"]')).text
        try: infor = driver.find_element_by_xpath('//*[@class = "layui-layer-content layui-layer-padding"]').text
        except: pass
        try: infor = driver.find_element_by_xpath('//*[@class = "layui-layer-content"]').text
        except: pass
        if '下单成功' in infor or '已领取' in infor:
            all_infor += [url2, infor]
            is_success = True
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