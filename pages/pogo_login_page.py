import random
import time
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PogoLoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.email = (By.CSS_SELECTOR, "input[id='email']")
        self.next_button = (By.CSS_SELECTOR, "a[id='logInBtn']")
        self.password = (By.CSS_SELECTOR, "input[id='password']")
        self.signin_button = (By.CSS_SELECTOR, "a[id='logInBtn']")
        self.setscreenname = (By.CSS_SELECTOR, "input[id='screenname']")
        self.screename_nextbtn = (By.CLASS_NAME, "default__1rbFd.primary__3GVte.button__3Z-Ug.cta__i9VIC")
        self.continuebtn = (By.CLASS_NAME, ".large__2-kkI primary__3GVte button__3Z-Ug button__10icW")
        self.searchArea = (By.CSS_SELECTOR, "input[placeholder='Search for games']")
    def click_email(self):
        self.driver.find_element(*self.email).click()

    def type_email(self, email):
        self.driver.find_element(*self.email).send_keys(email)
    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def click_password(self):
        self.driver.find_element(*self.password).click()

    def type_password(self, password):
        self.driver.find_element(*self.password).send_keys("P@ssword123")

    def click_signin_button(self):
        self.driver.find_element(*self.signin_button).click()

    def type_screen_name(self, screen_name):
        self.driver.find_element(*self.setscreenname).send_keys(screen_name)

    def click_screen_name_next_button(self):
        self.driver.find_element(*self.screename_nextbtn).click()

    def click_continue_button(self):
        self.driver.find_element(*self.continuebtn).click()

    # def login(self, email, password):
    #     self.click_email()
    #     self.type_email(email)
    #     self.click_next_button()
    #     self.click_password()
    #     self.type_password(password)
    #     self.click_signin_button()

    def set_screen_name(self, screen_name):
        self.type_screen_name(screen_name)
        self.click_screen_name_next_button()

    def continue_after_login(self):
        # Add a try-except block to handle potential absence of the button
        try:
            wait = WebDriverWait(self.driver, 10)
            continue_button = wait.until(EC.element_to_be_clickable(self.continuebtn))
            continue_button.click()
        except Exception as e:
            print(f"Continue button not found or clickable: {e}")



    def click_search_area(self):
        self.driver.find_element(*self.searchArea).click()
    def type_search_area(self, search_text):
        self.driver.find_element(*self.searchArea).send_keys(search_text)
    def hit_enter_on_search(self):
        self.driver.find_element(*self.searchArea).send_keys(Keys.ENTER)
    
      