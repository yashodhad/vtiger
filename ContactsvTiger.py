from genericlib import fileutilvTiger
from genericlib.baseclassvTiger import BaseClass
from genericlib import webdrivercommonlib
from genericlib.webdrivercommonlib import webdriverFeature
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver import Chrome,Firefox,Ie

import time
import unittest
class Contacts(BaseClass, unittest.TestCase):
    def test_CreateContacts(self):
        we = webdriverFeature
        print("-------Contacts")
       # we.normalwait(3)
        time.sleep(4)
        self.driver.find_element_by_xpath('//a[text()="Contacts"]').click()
        #we.normalwait(3)
        time.sleep(4)
        self.driver.find_element_by_xpath('//img[@src="themes/softed/images/btnL3Add.gif"]').click()
        #we.normalwait(3)
        time.sleep(4)
        self.driver.find_element_by_name('firstname').send_keys(fileutilvTiger.readExelData(0,1,0))
        self.driver.find_element_by_xpath('lastname').send_keys(fileutilvTiger.readExelData(0,1,0))
        #we.normalwait(3)
if __name__ == '__main__' :
    unittest.main()