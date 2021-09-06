# coding: utf-8
# @Time: 2021/9/6 22:07
# @Author: Bing
# @File: 003_selenium_locate
# @Project: study
from selenium import webdriver
path="chromedriver.exe"
#浏览器对象
browser=webdriver.Chrome(path)
url="https://www.baidu.com"
browser.get(url)

#元素定位 找到百度一下button
# button=browser.find_element_by_id('su')
# print(button)

#根据标签属性的属性值获取input对象
# input=browser.find_element_by_name('wd')
# print(input)

#根据xpath找到对象
# button=browser.find_elements_by_xpath('//input[@id="su"]')
# print(button)

#根据tagname
# inputs=browser.find_elements_by_tag_name('input')
# print(inputs)

#使用css选择器
# button=browser.find_element_by_css_selector("#su")
# print(button)

#根据链接文字
button=browser.find_element_by_link_text('直播')
print(button)