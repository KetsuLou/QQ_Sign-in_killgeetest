import time, os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
# Geettest 验证码
import geecrack
#https://www.geetest.com/show

def main(driver, offset_):
    try:
        while True: WebDriverWait(driver, 1, 0.2).until(lambda x: x.find_element_by_class_name('geetest_radar_tip')).click()               
    except: 
        time.sleep(1)
        geecrack.main(driver, 30, offset_)
    #是否验证成功
    try: 
        if WebDriverWait(driver, 1, 0.01).until(lambda x: x.find_element_by_xpath('//*[@class="geetest_slider geetest_fail"]')).text == '':
            while True: 
                try: 
                    driver.find_element_by_xpath('//*[@class="geetest_slider geetest_ready"]')
                    break
                except: pass
            time.sleep(0.5)
            driver.find_element_by_xpath('//*[@class="geetest_refresh_1"]').click()
    except: pass
        