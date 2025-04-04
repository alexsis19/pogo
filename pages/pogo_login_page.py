from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time


class PogoLoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.email = (By.CSS_SELECTOR, "input[id='email']")
        self.next_button = (By.CSS_SELECTOR, "a[id='logInBtn']")
        self.password = (By.CSS_SELECTOR, "input[id='password']")
        self.signin_button = (By.CSS_SELECTOR, "a[id='logInBtn']")
        self.setscreenname = (By.CSS_SELECTOR, "input[id='screenname']")
        self.screenname_nextbtn = (By.CSS_SELECTOR, ".default__1rbFd.primary__3GVte.button__3Z-Ug.cta__i9VIC")
        self.continuebtn = (By.CSS_SELECTOR, ".large__2-kkI.primary__3GVte.button__3Z-Ug.button__10icW")
        self.searchArea = (By.CSS_SELECTOR, "input[placeholder='Search for games']")
        self.searchContent = (By.CSS_SELECTOR, "span[class='categoryLabel__exxVq']")
        self.solitairgame = (By.CSS_SELECTOR, "div.gameTile__3amEb ")
        self.gameplaybtn = (By.CSS_SELECTOR, "button.playButton__1NRst")
        
    def click_email(self):
        assert self.driver.find_element(*self.email).is_displayed(), "Email field is not displayed"
        self.driver.find_element(*self.email).click()

    def type_email(self, email):
        self.driver.find_element(*self.email).send_keys(email)
    def click_next_button(self):
        assert self.driver.find_element(*self.next_button).is_displayed(), "Next button is not displayed"
        self.driver.find_element(*self.next_button).click()

    def click_password(self):
        assert self.driver.find_element(*self.password).is_displayed(), "Password field is not displayed"
        self.driver.find_element(*self.password).click()

    def type_password(self, password):
        
        self.driver.find_element(*self.password).send_keys(password)

    def click_signin_button(self):
        assert self.driver.find_element(*self.signin_button).is_displayed(), "Signin button is not displayed"
        self.driver.find_element(*self.signin_button).click()

    def type_screen_name(self, screen_name):
        self.driver.find_element(*self.setscreenname).send_keys(screen_name)

    def click_screen_name_next_button(self):
        self.driver.find_element(*self.screenname_nextbtn).click()

    def click_continue_button(self):
        self.driver.find_element(*self.continuebtn).click()

    def set_screen_name(self, screen_name):
        self.type_screen_name(screen_name)
        self.click_screen_name_next_button()

    
    def click_search_area(self):
        self.driver.find_element(*self.searchArea).click()
        
    def type_search_area(self, search_text):
        self.driver.find_element(*self.searchArea).send_keys(search_text)
        
    def hit_enter_on_search(self):
        self.driver.find_element(*self.searchArea).send_keys(Keys.ENTER)
        
        
    def click_solitairgame(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.searchContent))
        assert self.driver.find_element(*self.solitairgame).is_displayed(), "Solitaire game is not displayed"
        solitaire_element = self.driver.find_element(*self.searchContent)
        assert "SOLITAIRE" in solitaire_element.text, \
            f"Expected 'SOLITAIRE' in element text, but found '{solitaire_element.text}'"
        self.driver.find_element(*self.solitairgame).click()
        
    def game_play_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.gameplaybtn))
        assert self.driver.find_element(*self.gameplaybtn).is_displayed(), "Game search results are not displayed"

    
      