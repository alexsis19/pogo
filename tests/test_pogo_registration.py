import pytest
import time
from pages.pogo_home_page import PogoHomePage
from pages.pogo_register_page import PogoRegisterPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_pogo_registration_flow(driver):
    # 1. Visit www.pogo.com
    home_page = PogoHomePage(driver)
    home_page.load()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(home_page.register_free_button))
 # 2. Register user
    # 2.1 Click on register free button
    home_page.click_login()

    # Wait for the registration page to load (you might need to adjust the wait condition)
    registration_page = PogoRegisterPage(driver)
    wait.until(EC.presence_of_element_located(registration_page.country_dropdown))
    register_page = PogoRegisterPage(driver)

    # 2.2 Click and select random country
    register_page.click_country_dropdown()
    register_page.select_random_country()

    # 2.3 Click and select random month
    register_page.click_month_dropdown()
    register_page.select_random_month()

    # 2.4 Click and select random day
    register_page.click_day_dropdown()
    register_page.select_random_day()

    # 2.5 Click and select random year
    register_page.click_year_dropdown()
    register_page.select_random_year()

    # 2.6 Click on the next button
    register_page.click_next_button()

    # Add assertions here to verify the next step or any expected outcome
    # For example, you might want to check if a specific element is now visible
    # wait.until(EC.presence_of_element_located((By.ID, "some_next_page_element")))

    wait.until(EC.presence_of_element_located(registration_page.password))
    register_page.register_email_address()
    register_page.ea_unique_id()
    register_page.register_password()
    register_page.ea_next_button()
   #  assert driver.find_element(By.ID, "Verification Complete").is_displayed()
    wait.until(EC.presence_of_element_located(registration_page.eaAccCheckbox))
    register_page.click_profile_visibility_dropdown()
    time.sleep(180)
   #  register_page.select_random_profile_visibility()
   #  register_page.check_all_ea_checkboxes()
   
   #  register_page.eaAccCheckbox()
   

    # wait.until(EC.presence_of_element_located(registration_page.password))
    print("Successfully completed the initial registration steps.")