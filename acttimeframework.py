from genericlib.baseclass import BaseClass
from genericlib import fileutil
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import unittest
class User(BaseClass, unittest.TestCase):
    def test_createuser(self):
        print("-------create user")
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[text()='USERS']/..").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[text()='Add User']/..").click()
        time.sleep(3)
        self.driver.find_element_by_name('firstName').send_keys(fileutil.readExelData(2,1,0))
        time.sleep(4)
        self.driver.find_element_by_name("lastName").send_keys(fileutil.readExelData(2,1,1))
        time.sleep(3)
        self.driver.find_element_by_name("email").send_keys(fileutil.readExelData(2,1,2))
        time.sleep(3)
        self.driver.find_element_by_name("username").send_keys(fileutil.readExelData(2,1,3))
        time.sleep(3)
        self.driver.find_element_by_name("password").send_keys(fileutil.readExelData(2,1,4))
        time.sleep(3)
        self.driver.find_element_by_name("passwordCopy").send_keys(fileutil.readExelData(2,1,5))
        time.sleep(3)
        self.driver.find_element_by_id("userDataLightBox_commitBtn").click()
    def test_modifyuser(self):
        print("Modify User")

if __name__ == '__main__' :
    unittest.main()

