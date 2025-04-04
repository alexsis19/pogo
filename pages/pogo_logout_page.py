from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

class PogoLogoutPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.profilebtn = (By.CSS_SELECTOR, "img.avatarPortrait__1crGB")
        self.signoutbtn = (By.CSS_SELECTOR, "button.secondary__13sCi ")
        self.signoffcheck = (By.CSS_SELECTOR, "div[class='signout__2YBlu'] section h1")
    
    def click_profile_button(self):
        assert self.driver.find_element(*self.profilebtn).is_displayed(), "Profile button is not displayed"
        self.driver.find_element(*self.profilebtn).click()
        
    def click_signout_button(self):
        assert self.driver.find_element(*self.signoutbtn).is_displayed(), "Signout button is not displayed"
        self.driver.find_element(*self.signoutbtn).click()
        
    def signoff_check(self):
        assert self.driver.find_element(*self.signoffcheck).is_displayed(), "Signout check is not displayed"
    

    
      