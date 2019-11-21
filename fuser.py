import time
from genericlib import fileutil
from selenium.webdriver import Chrome
import xlrd
username=fileutil.readExelData(0,1,0)
password=fileutil.readExelData(0,1,1)
print(username)
print(password)

driver=Chrome('D:\\selenium_Drivers\\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://localhost/login.do')
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_name('pwd').send_keys(password)
driver.find_element_by_id('loginButton').click()

