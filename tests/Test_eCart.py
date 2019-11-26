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

    def test_signup(self):
        self.driver.find_element_by_partial_link_text('Sign in').click()
        assert self.driver.title == 'Login - My Store', "Title not matching"
        driver = self.driver
        self.email = f'xyz123@mail{random.randint(1, 1000)}.com'
        self.fname = 'Jack'
        self.lname = 'Matt'
        self.alias = 'john'
        self.address = "1 xyz street"
        self.city = "Alexander City"
        self.zip_code = 35010
        self.pwd = '12345678'
        self.phone = 567891234

        signuppage = HomePage(driver)
        signuppage.click_signin_btn()
        signuppage.create_account(self.email)

        create_acc = CreateAccountPage(self.driver)
        create_acc.fill_personal_info(self.fname, self.lname, self.email, self.pwd)
        create_acc.fill_address(self.fname, self.lname, self.address, self.city, self.zip_code, self.phone,
                                self.alias)
        create_acc.register()
        create_acc.validate_login()
        create_acc.validate_signout_option()

    def test_order(self):
        self.email = 'abc@xyxacz.com'
        self.pwd = '12345678'
        driver = self.driver
        loginpage = HomePage(driver)
        loginpage.click_signin_btn()
        loginpage.login_valid(self.email, self.pwd)
        accountpage = AccountsPage(driver)
        accountpage.add_to_cart()
        accountpage.order()
        accountpage.validate_order_confirmation()

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.close()
