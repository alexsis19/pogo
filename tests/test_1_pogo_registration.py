import pytest
import time
from pages.pogo_home_page import PogoHomePage
from pages.pogo_register_page import PogoRegisterPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_pogo_registration_flow(driver):
    home_page = PogoHomePage(driver)
    home_page.load()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(home_page.register_free_button))
    home_page.click_register_free()

    registration_page = PogoRegisterPage(driver)
    wait.until(EC.presence_of_element_located(registration_page.country_dropdown))
    register_page = PogoRegisterPage(driver)

    register_page.click_country_dropdown()
    register_page.select_random_country()

    register_page.click_month_dropdown()
    register_page.select_random_month()

    register_page.click_day_dropdown()
    register_page.select_random_day()

    register_page.click_year_dropdown()
    register_page.select_random_year()

    register_page.click_next_button()

    wait.until(EC.presence_of_element_located(registration_page.password))
    register_page.register_email_address()
    register_page.ea_unique_id()
    register_page.register_password()
    register_page.ea_next_button()
    time.sleep(60)
    wait.until(EC.presence_of_element_located(registration_page.eaAccCheckbox))
    register_page.click_profile_visibility_dropdown()
    register_page.select_random_profile_visibility()
    register_page.check_all_ea_checkboxes()
    register_page.click_create_account_button() 
    time.sleep(30)