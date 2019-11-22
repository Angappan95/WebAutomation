from ui_automation.pages.Signup import *
import unittest
import random
import time
from selenium import webdriver


class CreateAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        cls.driver = webdriver.Chrome(executable_path='../helpers/chromedriver.exe', options=options)
        cls.driver.get('http://automationpractice.com/index.php')
        cls.driver.set_page_load_timeout(5)
        cls.driver.implicitly_wait(10)

        cls.email = f'xyz123@mail{random.randint(1, 1000)}.com'
        cls.fname = 'abx'
        cls.lname = 'gdfg'
        cls.alias = 'john'
        cls.address = "1 xyz street"
        cls.city = "Alexander City"
        cls.zip_code = 35010
        cls.pwd = '12345678'
        cls.phone = 567891234

    def test_signup(self):
        self.driver.find_element_by_partial_link_text('Sign in').click()
        assert self.driver.title == 'Login - My Store', "Title not matching"
        driver = self.driver
        signup = HomePage(driver)
        signup.click_signin_btn()
        signup.create_account(self.email)

        create_acc = CreateAccountPage(self.driver)
        create_acc.fill_personal_info(self.fname, self.lname, self.email, self.pwd)
        create_acc.fill_address(self.fname, self.lname, self.address, self.city, self.zip_code, self.phone,
                                self.alias)
        create_acc.register()
        create_acc.validate_login()
        create_acc.validate_signout_option()

    def test_order(self):
        pass

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.close()
