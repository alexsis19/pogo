import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.pogo_home_page import PogoHomePage
from pages.pogo_login_page import PogoLoginPage
from pages.pogo_logout_page import PogoLogoutPage

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()
@pytest.fixture(scope="function")
def wait(browser):
    return WebDriverWait(browser, 10)

def login(driver):
    # 1. Visit www.pogo.com
    home_page = PogoHomePage(driver)
    home_page.load()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(home_page.login_button))
 # 2. Login user
    home_page.click_login()
    # Wait for the Login  page to load
    login_page = PogoLoginPage(driver)
    wait.until(EC.presence_of_element_located(login_page.signin_button))
    login_page.click_email()
    login_page.type_email("sismaharjan@gmail.com")
    login_page.click_next_button()
    wait.until(EC.presence_of_element_located(login_page.password))
    login_page.click_password()
    login_page.type_password("P@ssword123")
    login_page.click_signin_button()
    wait.until(EC.presence_of_element_located(login_page.searchArea))
    return login_page  # Return the logged-in login_page object

def logout(driver):
    wait = WebDriverWait(driver, 10)
    logout_page = PogoLogoutPage(driver)
    logout_page.click_profile_button()
    logout_page.click_signout_button()
    wait.until(EC.presence_of_element_located(logout_page.signoffcheck))
    return logout_page  # Return the logged-out logout_page object