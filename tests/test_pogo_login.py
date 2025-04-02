import pytest
import time
from pages.pogo_home_page import PogoHomePage
from pages.pogo_login_page import PogoLoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_pogo_login_flow(driver):
    # 1. Visit www.pogo.com
    home_page = PogoHomePage(driver)
    home_page.load()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(home_page.login_button))
 # 2. Register user
    # 2.1 Click on register free button
    home_page.click_login()

    # Wait for the registration page to load (you might need to adjust the wait condition)
    login_page = PogoLoginPage(driver)
    wait.until(EC.presence_of_element_located(login_page.signin_button))
    signin_page = PogoLoginPage(driver)

    # 2.2 Click and select random country
    signin_page.click_email()
    signin_page.type_email("sismaharjan@gmail.com")
    signin_page.click_next_button()
    wait.until(EC.presence_of_element_located(login_page.password))
    signin_page.click_password()
    signin_page.type_password("P@ssword123")
    signin_page.click_signin_button()
    wait.until(EC.presence_of_element_located(login_page.searchArea))
    signin_page.click_search_area()
    signin_page.type_search_area("Solitaire")
    signin_page.hit_enter_on_search()
    time.sleep(20)