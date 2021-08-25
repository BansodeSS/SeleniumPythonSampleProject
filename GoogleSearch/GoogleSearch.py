from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_gitrepo(self):
        self.driver.get('https://www.google.com')
        self.driver.find_element_by_name("q").send_keys("GitHUB")
        self.driver.find_element_by_name("btnK").click()

    def test_search_repo(self):
        self.driver.get('https://www.google.com')
        self.driver.find_element_by_name("q").send_keys("BansodeSS ")
        self.driver.find_element_by_name("btnK").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))


