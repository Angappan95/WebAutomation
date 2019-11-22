from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random

import time

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')

driver = webdriver.Chrome(executable_path='../helpers/chromedriver.exe', options=options)

driver.get('http://automationpractice.com/index.php')
driver.set_page_load_timeout(5)
driver.implicitly_wait(10)

# Click on Sign in option
driver.find_element_by_partial_link_text('Sign in').click()
assert driver.title == 'Login - My Store', "Title not matching"

# Create Account
email = f'xyz123@mail{random.randint(1, 1000)}.com'
fname = 'abx'
lname = 'gdfg'
alias = 'john'
address = "1 xyz street"
city = "Alexander City"
zip_code = 35010
pwd = '12345678'
phone = 567891234

driver.find_element_by_id('email_create').send_keys(email)
driver.find_element_by_xpath('//i[@class="icon-user left"]').click()

# Personal Information
driver.find_element_by_id('id_gender1').click()
driver.find_element_by_id('customer_firstname').send_keys(fname)
driver.find_element_by_id('customer_lastname').send_keys(lname)

# Assert that email id given in create account page is retrived in email id box
email_value = driver.find_element_by_id('email').get_attribute('value')
assert email_value == email, f"{email} | {email_value}"

driver.find_element_by_id('passwd').send_keys(pwd)
select_day = Select(driver.find_element_by_id('days'))
select_day.select_by_value('1')

select_month = Select(driver.find_element_by_id('months'))
select_month.select_by_value('1')

select_year = Select(driver.find_element_by_id('years'))
select_year.select_by_value('1990')

# Assert that entered name are displayed in Your Address section
fname_value = driver.find_element_by_id('firstname').get_attribute('value')
assert fname_value == fname, f"{fname_value}|{fname}"

lname_value = driver.find_element_by_id('lastname').get_attribute('value')
assert lname_value == lname, f"{lname_value}|{lname}"

driver.find_element_by_id("address1").send_keys(address)

driver.find_element_by_id("city").send_keys(city)

# Select State
select_state = Select(driver.find_element_by_id("id_state"))
select_state.select_by_value('1')

driver.find_element_by_id('postcode').send_keys(zip_code)

driver.find_element_by_id('phone_mobile').send_keys(phone)

ele_alais = driver.find_element_by_id('alias')
ele_alais.clear()
ele_alais.send_keys(alias)

# Click on Register button
driver.find_element_by_xpath('//span[text()="Register"]').click()

# Assert title page
assert driver.title == 'My account - My Store', f'Something went wrong with the title, {driver.title}'

# Validate the presence of Sign out option
try:
    driver.find_element_by_class_name('logout')
except NoSuchElementException:
    assert False, "Sign out option is not displayed"


section = "Women"
product = "Faded Short Sleeve T-shirts"

driver.find_element_by_link_text(section).click()

ele_product = driver.find_element_by_xpath('//div[h5[a[contains(text(),"Faded Short Sleeve T-shirts")]]]')

ActionChains(driver).move_to_element(ele_product).perform()

# Click on Add to Cart button
ele_product.find_element_by_link_text('Add to cart').click()

try:
    driver.find_element_by_xpath('//h2[contains(.,"Product successfully added to your shopping cart")]')

except NoSuchElementException:
    assert False, "Product confirmation message not displayed"

# Click on Proceed to Checkout option
ele_checkout = driver.find_element_by_xpath('//span[contains(text(),"Proceed to checkout")]')

# Click on checkout button in Confirmation page
ele_checkout.click()

# Click on checkout button in Summary page
WebDriverWait(driver, 5).\
    until(EC.presence_of_element_located((By.XPATH, '(//span[contains(text(),"Proceed to checkout")])[2]'))).click()

# Click on checkout button in Address page
WebDriverWait(driver, 5).\
    until(EC.presence_of_element_located((By.XPATH, '(//span[contains(text(),"Proceed to checkout")])[2]'))).click()

# Check Terms & Conditions
driver.find_element_by_id('cgv').click()
WebDriverWait(driver, 5).\
    until(EC.presence_of_element_located((By.XPATH, '(//span[contains(text(),"Proceed to checkout")])[2]'))).click()

driver.find_element_by_xpath('//a[contains(text(),"Pay by bank wire")]').click()

driver.find_element_by_xpath('//span[text()="I confirm my order"]').click()

assert driver.title == 'Order confirmation - My Store', "Confirmation page is not loaded"




