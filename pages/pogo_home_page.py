from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class PogoHomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.register_free_button = (By.CSS_SELECTOR, "button.primary__3GVte")
        self.login_button = (By.CSS_SELECTOR, "button.secondary__13sCi ")


    def load(self):
        self.driver.get("https://www.pogo.com")

    def click_register_free(self):
        self.driver.find_element(*self.register_free_button).click()

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    