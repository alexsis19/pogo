import random
import time
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PogoRegisterPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.country_dropdown = (By.CSS_SELECTOR, "select[name='country']")
        self.month_dropdown = (By.CSS_SELECTOR, "select[name='dobMonth']")
        self.day_dropdown = (By.CSS_SELECTOR, "select[name='dobDay']")
        self.year_dropdown = (By.CSS_SELECTOR, "select[name='dobYear']")
        self.next_button = (By.CSS_SELECTOR, "a[id='countryDobNextBtn']")
        self.email_address = (By.CSS_SELECTOR,"input[name='email']")
        self.ea_id = (By.CSS_SELECTOR, "input[name='originId']")
        self.password = (By.CSS_SELECTOR, "input[name='password']")
        self.eaNextButton = (By.CSS_SELECTOR, "a[id='basicInfoNextBtn']")
        self.profileVisibility = (By.CSS_SELECTOR, "select[name='friendVisibility']")
        self.eaAccCheckbox = (By.CSS_SELECTOR, "input[type='checkbox']")
        self.createAccBtn = (By.CSS_SELECTOR, "#submitBtn")

    def select_random_option(self, locator):
        wait = WebDriverWait(self.driver, 10)
        dropdown_element = wait.until(EC.presence_of_element_located(locator))
        select = Select(dropdown_element)
        options = select.options
        # Ensure there are options to select from
        if len(options) > 1:
            random_index = random.randint(1, len(options) - 1)  # Exclude the first default option if present
            select.select_by_index(random_index)
        else:
            print(f"Warning: Less than two options available in dropdown: {locator}")

    def click_country_dropdown(self):
        self.driver.find_element(*self.country_dropdown).click()

    def select_random_country(self):
        self.select_random_option(self.country_dropdown)

    def click_month_dropdown(self):
        self.driver.find_element(*self.month_dropdown).click()

    def select_random_month(self):
        self.select_random_option(self.month_dropdown)

    def click_day_dropdown(self):
        self.driver.find_element(*self.day_dropdown).click()

    def select_random_day(self):
        self.select_random_option(self.day_dropdown)

    def click_year_dropdown(self):
        self.driver.find_element(*self.year_dropdown).click()

    def select_random_year(self):
        self.select_random_option(self.year_dropdown)

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def register_email_address(self):
        self.driver.find_element(*self.email_address).click()
        # Generate a unique email address
        timestamp = int(time.time())  # Use current timestamp to ensure uniqueness
        unique_email = f"testuser_{timestamp}@example.com"

        # Enter the email address into the email field
        self.driver.find_element(*self.email_address).send_keys(unique_email)
        # self.driver.find_element(*self.email_address).send_keys(self.email)
        

    def ea_unique_id(self):
        # Generate a random length between 4 and 16 characters
        id_length = random.randint(4, 16)

        # Generate a random string with letters and digits
        unique_id = ''.join(random.choices(string.ascii_letters + string.digits, k=id_length))

        # Enter the unique ID into the ea_id field
        self.driver.find_element(*self.ea_id).send_keys(unique_id)

    def register_password(self):
    # Generate a random password with letters, digits, and special characters
        characters = "P@ssword123"
    # Enter the random password in the password field
        self.driver.find_element(*self.password).send_keys(characters)
        # self.driver.find_element(*self.password).send_keys(self.password)
        

    def ea_next_button(self):
        # Click on the ea_next_button element
        self.driver.find_element(*self.eaNextButton).click()
        time.sleep(10)

    def click_profile_visibility_dropdown(self):
        self.driver.find_element(*self.profileVisibility).click()

    def select_random_profile_visibility(self):
        self.select_random_option(self.profileVisibility)

    def check_all_ea_checkboxes(self):
        checkboxes = self.driver.find_elements(*self.eaAccCheckbox)
        for checkbox in checkboxes:
            if not checkbox.is_selected():
                # Use JavaScript to click the checkbox to avoid interception issues
                self.driver.execute_script("arguments[0].click();", checkbox)
                
    def click_create_account_button(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.createAccBtn))
        self.driver.find_element(*self.createAccBtn).click()


