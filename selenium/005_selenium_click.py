# coding: utf-8
# @Time: 2021/9/6 22:34
# @Author: Bing
# @File: 005_selenium_click
# @Project: study
from selenium import webdriver

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
url = 'https://www.baidu.com'
browser.get(url)

import time

time.sleep(2)
#输入周杰伦
input=browser.find_element_by_id('kw')
input.send_keys('周杰伦')
time.sleep(2)
#点击百度一下
button=browser.find_element_by_id("su")
button.click()
time.sleep(2)
#滑到底部
js_buttom='document.documentElement.scrollTop=100000'
browser.execute_script(js_buttom)
time.sleep(2)
#获取下一页的按钮
next=browser.find_element_by_xpath('//a[@class="n"]')
#点击
next.click()
time.sleep(2)
#回到上一页
browser.back()
time.sleep(2)
#回去
browser.forward()
time.sleep(3)
#退出
browser.quit()
