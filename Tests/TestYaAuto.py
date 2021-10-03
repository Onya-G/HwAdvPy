import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

LOGIN = 'your login'
PASSWD = 'your password'


class TestYaLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_log_ya(self):
        self.driver.get('https://passport.yandex.ru/auth/')
        elem1 = self.driver.find_element_by_name('login')
        elem1.send_keys(LOGIN)
        elem1.send_keys(Keys.RETURN)
        time.sleep(3)
        elem2 = self.driver.find_element_by_name('passwd')
        elem2.send_keys(PASSWD)
        elem2.send_keys(Keys.RETURN)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
