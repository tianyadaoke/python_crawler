# coding: utf-8
# @Time: 2021/9/6 22:20
# @Author: Bing
# @File: 004_selenium_element
# @Project: study
from selenium import webdriver

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
url = 'http://www.baidu.com'
browser.get(url)
input = browser.find_element_by_id('su')
print(input.get_attribute('class'))
print(input.tag_name)
print(input.text)