from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import HtmlTestRunner
from POMDemo.Pages.loginPage import loginPage
from POMDemo.Pages.homePage import HomePage



class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        login = loginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        home = HomePage(driver)
        home.click_welcome()
        home.click_logout()
        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()

        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Logout").click()

    def test_login_invalid_password(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com/')
        login = loginPage(driver)
        login.enter_username("Admin123")
        login.enter_password("admin123")
        login.click_login()
        message = login.check_invalid_username_message()
        self.assertEqual(message,'Invalid credentials')

        # home = HomePage(driver)
        # home.click_welcome()
        # home.click_logout()
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))

