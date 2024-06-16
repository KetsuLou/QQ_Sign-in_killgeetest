import time, os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import configparser
#http://my.4399.com/forums/mtag-78097
#http://my.4399.com/jifen/

def main(is_head):
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
    url1 = 'http://my.4399.com/forums/mtag-78097'
    url2 = 'http://my.4399.com/jifen/'
    driver.get(url1)
    driver.switch_to_frame('popup_login_frame')#先跳转到iframe框架

    all_infor = []
    is_success = False
    is_success1 = False
    is_success2 = False
    try:
        #登录
        try:
            driver.find_element_by_xpath("//div[@class = 'sign_group']/a").click()#签到
        except:
            #未登录时
            WebDriverWait(driver, 2).until(lambda x: x.find_element_by_name('username')).send_keys(config['path_4399']['username'])
            #username = driver.find_element_by_name('username').send_keys(config['path_4399']['username'])
            driver.find_element_by_id('j-password').send_keys(config['path_4399']['password'])
           
            #登录
            driver.find_element_by_xpath("//div[@class = 'login_hor ux_login clearfix']/input").click()
        try:
            #密码错误
            infor = WebDriverWait(driver, 1).until(lambda x: x.find_element_by_xpath("//div[@id = 'Msg']")).text
            pwd = False
        except:
            pwd = True
            pass
        if not pwd:
            raise
        driver.switch_to.default_content()

        #url1签到
        try:
            try:
                infor = driver.find_element_by_xpath("//div[@class = 'sign_group sign_disabled']/a").text
                infor = "您已签到！"
            except:
                element = WebDriverWait(driver, 2).until(lambda x: x.find_element_by_xpath("//div[@class = 'sign_group']/a"))
                driver.execute_script("arguments[0].click();", element)
                infor = WebDriverWait(driver, 1).until(lambda x: x.find_element_by_xpath("//div[@class = 'sign_group sign_disabled']/a")).text
                infor += "!"
            is_success1 = True
            all_infor += [url1, infor]
        except:
            #若url1签到失败不影响url2签到
            infor = "签到失败！"

            all_infor += [url1, infor]
        
        #url2签到
        driver.get(url2)
        try:
            infor = WebDriverWait(driver, 1).until(lambda x: x.find_element_by_xpath("//div[@class = 'jf_checkin_box']/a/span"))
            if infor.text == "我要签到":
                infor.click()
                time.sleep(1.5)
                infor = "成功签到!"
                is_success2 = True
            elif infor.text == "查看签到记录":
                infor = "您已签到！"
                is_success2 = True
            else:
                infor = "签到失败!"

            all_infor += [url2, infor]
        except:
            infor = "签到失败!"
            all_infor += [url2, infor]
            
    except:
        if not pwd: all_infor += [url1, infor]
        else: all_infor += ["程序出错"]
    
    if is_success1 and is_success2: is_success = True
    driver.close()
    try: os.system('taskkill /im chromedriver.exe /F')
    except: pass
    all_infor += ['\n']
    return all_infor, is_success

if __name__ == "__main__":
    print(main(1))