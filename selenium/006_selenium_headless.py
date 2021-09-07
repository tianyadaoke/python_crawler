from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# options=Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# path=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
# options.binary_location=path
# browser=webdriver.Chrome(options=options)
#
# url='http://www.baidu.com'
# browser.get(url)
# browser.save_screenshot('baidu.png')

#封装headless
def share_browser():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    options.binary_location = path
    browser = webdriver.Chrome(options=options)
    return browser

browser=share_browser()
url = 'http://www.baidu.com'
browser.get(url)
browser.save_screenshot('baidu.png')