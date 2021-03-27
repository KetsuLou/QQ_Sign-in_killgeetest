import time, os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# Geettest 验证码
import geecrack
import configparser
#https://www.ieqq.net/?cid=222&tid=5584


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
    url = 'https://www.ieqq.net/?cid=222&tid=5584'
    driver.get(url)
    try:
        WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//*[@name='inputvalue']")).send_keys(config['QQ_path']['QQ'])
        buy = WebDriverWait(driver, 2).until(lambda x: x.find_element_by_xpath("//input[@id='submit_buy']"))
        buy.click()
        try:
            #未领
            #尝试自动滑块认证
            for cs in range(max_cs):
                try:
                    WebDriverWait(driver, 5).until(lambda x: x.find_element_by_class_name('geetest_radar_tip')).click()
                    time.sleep(1.5)
                except:
                    pass
                geecrack.main(driver, 30, offset_)
                #是否验证成功
                try:
                    infor = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//*[@class='layui-layer-content layui-layer-padding']")).text
                    all_infor += [url, infor]
                    is_success = True
                    break
                except: pass
                if cs == (max_cs - 1): all_infor += [url, "验证次数过多！"]
        except:
            #已领或未知错误
            infor = WebDriverWait(driver, 3).until(lambda x: x.find_element_by_xpath('//*[@class="layui-layer-content"]')).text
            if len(infor) >= 28: infor = infor[:28] + '....'
            all_infor += [url, infor]
            if "已添加过" in infor :is_success = True
    except:
        all_infor += [url, "程序出错"]

    driver.close()
    try: os.system('taskkill /im chromedriver.exe /F')
    except: pass
    all_infor += ['\n']
    return all_infor, is_success

if __name__ == "__main__":
    print(main(3, 1, 0))