import time, os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import configparser

import def_killgeetest
#http://176.111dsw.com/user/sign

def main(max_cs, is_test, is_head, offset_):
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
    url = 'http://176.111dsw.com/user/sign'
    all_infor = []
    is_success = False


    try:
        driver.get(url)
        #登录
        try:
            WebDriverWait(driver, 2, 0.1).until(lambda x: x.find_element_by_xpath("//*[@class='btn btn-info btn-block']")).click()#签到
        except:
            #未登录时
            WebDriverWait(driver, 2, 0.1).until(lambda x: x.find_element_by_xpath("//*[@name='username']")).send_keys(config['path_lz']['username'])
            driver.find_element_by_xpath("//*[@name='password']").send_keys(config['path_lz']['password'])

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
        
        WebDriverWait(driver, 3, 0.1).until(lambda x: x.find_element_by_xpath("//*[@class='layui-layer-btn0']")).click()
        time.sleep(0.5)
        try: WebDriverWait(driver, 3, 0.1).until(lambda x: x.find_element_by_xpath("//*[@class='layui-layer-btn1']")).click()
        except: pass
        
        #签到
        try:
            try:
                infor = WebDriverWait(driver, 2, 0.1).until(lambda x: x.find_element_by_xpath("//*[@class='layui-btn-group']/button[@disabled='disabled']")).text
                if infor == '已签到': is_success = True
                else: raise
            except:
                WebDriverWait(driver, 2, 0.1).until(lambda x: x.find_element_by_xpath("//*[@class='btn btn-success']")).click()
                try:
                    infor = WebDriverWait(driver, 3, 0.6).until(lambda x: x.find_element_by_xpath("//*[@class='layui-layer-content']")).text
                except:
                    try:
                        while driver.find_element_by_xpath("//*[@class='layui-layer-content']").text == '': pass
                    except: pass
                    WebDriverWait(driver, 5, 0.1).until(lambda x: x.find_element_by_class_name('geetest_radar_tip'))
                    for cs in range(max_cs):
                        def_killgeetest.main(driver, offset_)
                        try:
                            try:
                                while True: driver.find_element_by_xpath("//*[@class='layui-layer-content layui-layer-loading2']")
                            except: pass
                            #infor = WebDriverWait(driver, 3, 0.1).until(lambda x: x.find_element_by_xpath('//*[@class = "layui-layer-content layui-layer-padding"]')).text
                            WebDriverWait(driver, 3, 0.1).until(lambda x: x.find_element_by_xpath('//*[@class = "layui-layer-btn layui-layer-btn-"]')).text
                            try: infor = driver.find_element_by_xpath('//*[@class = "layui-layer-content layui-layer-padding"]').text
                            except: pass
                            try: infor = driver.find_element_by_xpath('//*[@class = "layui-layer-content"]').text
                            except: pass
                            if '下单成功' in infor or '已免费领取' in infor:
                                all_infor += [url, infor]
                                is_success = True
                                break
                        except: pass
                        if cs == (max_cs - 1): all_infor += [url, "验证次数过多！"]
                #time.sleep(1)
            if '签到成功' in infor: is_success = True
            all_infor += [url, infor]
        except:
            infor = "签到失败！"
            all_infor += [url, infor]
            
    except:
        try: 
            if not pwd: all_infor += [url, infor]
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
    print(main(10, 0, 1, -2))