import time, os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import configparser
#http://www.aizy.cc/?cid=1&tid=449


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
        
    all_infor = []
    is_success = False
    # 请求网站
    url = 'http://www.aizy.cc/?cid=1&tid=449'
    driver.get(url)
    try:
        WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//*[@class='layui-layer-btn0']")).click()

        driver.find_element_by_xpath("//*[@id='inputvalue']").send_keys(config['QQ_path']['QQ'])
        text = driver.find_element_by_xpath("//*[@id='inputname2']").text
        if text == "本站地址":
            driver.find_element_by_xpath("//*[@id='inputvalue2']").send_keys('http://www.aizy.cc/')
        else: raise
        time.sleep(0.5)
        driver.find_element_by_xpath("//*[@class='btn btn-block btn-primary']").click()
    
        try:
            #已领
            infor = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//*[@class='layui-layer-content']")).text
            all_infor += [url, infor]
            is_success = True
        except:
            alert = WebDriverWait(driver, 10).until(lambda x: x.switch_to_alert())
            #获取警告对话框的内容
            infor = alert.text
            alert.accept()#alert对话框属于警告对话框，我们这里只能接受弹窗
            all_infor += [url, infor]
            is_success = True

    except:
        all_infor += [url, "程序出错"]

    driver.close()
    try: os.system('taskkill /im chromedriver.exe /F')
    except: pass
    all_infor += ['\n']
    return all_infor, is_success

if __name__ == "__main__":
    print(main(1))