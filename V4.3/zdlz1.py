import time, os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import def_killgeetest
import configparser
#http://176.111dsw.com/user/order?gid=3145


def main(max_cs, is_head, offset_):
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

    all_infor = []
    is_success = False
    # 请求网站
    url = 'http://176.111dsw.com/user/order?gid=3145'
    driver.get(url)
    try:
        try:
            choose_product = driver.find_element_by_name('gid')#寻找商品
        except:#未登录时
            WebDriverWait(driver, 2, 0.1).until(lambda x: x.find_element_by_name('username')).send_keys(config['path_lz']['username'])
            driver.find_element_by_name('password').send_keys(config['path_lz']['password'])

            driver.find_element_by_xpath("//div[@class = 'form-group']/input").click()
            try:
                #密码错误
                infor = WebDriverWait(driver, 1, 0.1).until(lambda x: x.find_element_by_xpath("//*[@class='layui-layer-content layui-layer-padding']")).text
                if '密码错误' in infor: pwd = False
                else: raise
            except:
                pwd = True
                pass
            if not pwd:
                raise
            try:
                while(1): 
                    #WebDriverWait(driver, 2).until(lambda x: x.find_element_by_xpath("//div[@class = 'layui-layer-btn layui-layer-btn-']/a")).click()
                    driver.find_element_by_xpath("//div[@class = 'layui-layer-btn layui-layer-btn-']/a").click()
                    time.sleep(1)
            except:
                pass
            
        #输入账号
        QQnumber = driver.find_element_by_name('value[0]')
        QQnumber.send_keys(config['QQ_path']['QQ'])
        Label1 = driver.find_element_by_name('value[1]')
        Label2 = driver.find_element_by_name('value[2]')
        Label1_input = Label1.get_attribute('placeholder')
        Label2_input = Label2.get_attribute('placeholder')
        Label1.send_keys(Label1_input.replace('输入 ', ''))
        Label2.send_keys(Label2_input.replace('输入 ', ''))
        driver.find_element_by_xpath("//div[@class = 'btn-group btn-group-justified form-group']/a").click()
        
        time.sleep(1)
        try:
            #已领
            infor = WebDriverWait(driver, 3, 0.15).until(lambda x: x.find_element_by_xpath('//*[@class="layui-layer-content layui-layer-padding"]')).text
            all_infor += [url, infor]
            is_success = True
        except:
            #未领
            #尝试自动滑块认证
            time.sleep(1)
            for cs in range(max_cs):
                def_killgeetest.main(driver, offset_)
                try:
                    infor = WebDriverWait(driver, 3, 0.1).until(lambda x: x.find_element_by_xpath('//*[@class = "layui-layer-content layui-layer-padding"]')).text
                    #infor = WebDriverWait(driver, 3, 0.15).until(lambda x: x.find_element_by_xpath("//*[@class='layui-layer-content']")).text
                    if '下单成功' in infor or '已免费领取' in infor:
                        all_infor += [url, infor]
                        is_success = True
                        break
                except: pass
                if cs == (max_cs - 1): all_infor += [url, "验证次数过多！"]
    except:
        if not pwd: all_infor += [url, infor]
        else: all_infor += ["程序出错"]
    driver.close()
    try: os.system('taskkill /im chromedriver.exe /F')
    except: pass
    all_infor += ['\n']
    return all_infor, is_success

if __name__ == "__main__":
    print(main(10, 1, -2))
    