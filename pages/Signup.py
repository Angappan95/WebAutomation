from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.ele_signin_id = 'Sign in'
        self.ele_create_enter_mail_id = 'email_create'
        self.btn_create_account_xpath = '//i[@class="icon-user left"]'
        self.ele_registered_mail_id = 'email'
        self.ele_registered_password_id = 'passwd'
        self.ele_registered_signin_id = 'SubmitLogin'

    def click_signin_btn(self):
        self.driver.find_element_by_partial_link_text(self.ele_signin_id).click()

    def create_account(self, data):
        self.driver.find_element_by_id(self.ele_create_enter_mail_id).send_keys(data)
        self.driver.find_element_by_xpath(self.btn_create_account_xpath).click()

    def login_valid(self, mail, password):
        self.driver.find_element_by_id(self.ele_registered_mail_id).send_keys(mail)
        self.driver.find_element_by_id(self.ele_registered_password_id).send_keys(password)
        self.driver.find_element_by_id(self.ele_registered_signin_id).click()
        assert self.driver.title == 'My account - My Store', f'Something went wrong. Site is in {self.driver.title} page'


class CreateAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.chk_title_id = 'id_gender1'
        self.ele_fname_id = 'customer_firstname'
        self.ele_lname_id = 'customer_lastname'

        self.ele_email_id = 'email'
        self.ele_password_id = 'passwd'
        self.dd_day_id = 'days'
        self.dd_month_id = 'months'
        self.dd_year_id = 'years'

        self.ele_add_fname_id = 'firstname'
        self.ele_add_lname_id = 'lastname'
        self.ele_address_id = 'address1'
        self.ele_city_id = 'city'
        self.ele_state_id = 'id_state'
        self.ele_phone_id = 'phone_mobile'
        self.ele_zipcode_id = 'postcode'
        self.ele_alais_id = 'alias'
        self.btn_register_xpath = '//span[text()="Register"]'

    def fill_personal_info(self, fname, lname, email, pwd):
        self.driver.find_element_by_id(self.chk_title_id).click()
        self.driver.find_element_by_id(self.ele_fname_id).send_keys(fname)
        self.driver.find_element_by_id(self.ele_lname_id).send_keys(lname)

        # Assert that email id given in create account page is retrived in email id box
        email_value = self.driver.find_element_by_id(self.ele_email_id).get_attribute('value')
        assert email_value == email, f"Entered email is not matching. {email} | {email_value}"

        self.driver.find_element_by_id(self.ele_password_id).send_keys(pwd)
        select_day = Select(self.driver.find_element_by_id(self.dd_day_id))
        select_day.select_by_value('1')

        select_month = Select(self.driver.find_element_by_id(self.dd_month_id))
        select_month.select_by_value('1')

        select_year = Select(self.driver.find_element_by_id(self.dd_year_id))
        select_year.select_by_value('1990')

    def fill_address(self, fname, lname, address, city, zip_code, phone, alias):
        fname_value = self.driver.find_element_by_id(self.ele_add_fname_id).get_attribute('value')
        assert fname_value == fname, f"{fname_value}|{fname}"

        lname_value = self.driver.find_element_by_id(self.ele_add_lname_id).get_attribute('value')
        assert lname_value == lname, f"{lname_value}|{lname}"

        self.driver.find_element_by_id(self.ele_address_id).send_keys(address)
        self.driver.find_element_by_id(self.ele_city_id).send_keys(city)

        # Select State
        select_state = Select(self.driver.find_element_by_id(self.ele_state_id))
        select_state.select_by_value('1')

        self.driver.find_element_by_id(self.ele_zipcode_id).send_keys(zip_code)
        self.driver.find_element_by_id(self.ele_phone_id).send_keys(phone)
        ele_alais = self.driver.find_element_by_id(self.ele_alais_id)
        ele_alais.clear()
        ele_alais.send_keys(alias)

    def register(self):
        self.driver.find_element_by_xpath(self.btn_register_xpath).click()

    def validate_login(self):
        assert self.driver.title == 'My account - My Store', f'Something went wrong with the title, {self.driver.title}'

    def validate_signout_option(self):
        try:
            self.driver.find_element_by_class_name('logout')
        except NoSuchElementException:
            assert False, "Sign out option is not displayed"


class AccountsPage:
    def __init__(self, driver):
        self.driver = driver
        self.ele_women_section_link = 'Women'
        self.ele_product_xpath = '//div[h5[a[contains(text(),"Faded Short Sleeve T-shirts")]]]'
        self.btn_add_to_cart_link = 'Add to cart'
        self.ele_confirmation_msg_xpath = '//h2[contains(.,"Product successfully added to your shopping cart")]'
        self.btn_checkout_xpath = '//span[contains(text(),"Proceed to checkout")]'
        self.ele_summary_checkout_xpath = '(//span[contains(text(),"Proceed to checkout")])[2]'
        self.ele_address_checkout_xpath = '(//span[contains(text(),"Proceed to checkout")])[2]'
        self.ele_terms_xpath = '(//span[contains(text(),"Proceed to checkout")])[2]'
        self.ele_wire_pay_xpath = '//a[contains(text(),"Pay by bank wire")]'
        self.ele_confirm_order_xpath = '//span[text()="I confirm my order"]'
        self.title_order_confirmation = 'Order confirmation - My Store'

    def add_to_cart(self):
        self.driver.find_element_by_partial_link_text(self.ele_women_section_link).click()
        ele_product = self.driver.find_element_by_xpath(self.ele_product_xpath)
        ActionChains(self.driver).move_to_element(ele_product).perform()

        # Click on Add to Cart button
        ele_product.find_element_by_link_text(self.btn_add_to_cart_link).click()

        try:
            self.driver.find_element_by_xpath(self.ele_confirmation_msg_xpath)

        except NoSuchElementException:
            assert False, 'Product confirmation message not displayed'

        # Click on Proceed to Checkout option
        ele_checkout = self.driver.find_element_by_xpath(self.btn_checkout_xpath)

        # Click on checkout button in Confirmation page
        ele_checkout.click()

        # Click on checkout button in Summary page
        WebDriverWait(self.driver, 5).until(
            ec.presence_of_element_located((By.XPATH, self.ele_summary_checkout_xpath))).click()

        # Click on checkout button in Address page
        WebDriverWait(self.driver, 5).until(
            ec.presence_of_element_located((By.XPATH, self.ele_address_checkout_xpath))).click()

    def order(self):
        self.driver.find_element_by_id('cgv').click()
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.ele_terms_xpath))).click()

        self.driver.find_element_by_xpath(self.ele_wire_pay_xpath).click()

        self.driver.find_element_by_xpath(self.ele_confirm_order_xpath).click()

    def validate_order_confirmation(self):
        assert self.driver.title == self.title_order_confirmation, 'Confirmation page is not loaded'
