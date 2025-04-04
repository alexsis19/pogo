from selenium.webdriver.chrome.webdriver import WebDriver
from pages.pogo_login_page import PogoLoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from conftest import login, logout
   
def test_login_check(driver: WebDriver):
   wait = WebDriverWait(driver, 10)
   login(driver)
   wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img.avatarPortrait__1crGB")))
   logout(driver)
   
def test_search(driver: WebDriver):
   login(driver)
   login_page = PogoLoginPage(driver)
   wait = WebDriverWait(driver, 10)
   wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.searchInput__1crGB")))
   login_page.click_search_area()
   login_page.type_search_area("Solitaire")
   login_page.hit_enter_on_search()
   login_page.click_solitairgame()
   login_page.game_play_btn()
   logout(driver)
   
def test_login_logout_login(driver: WebDriver):
   login(driver)
   logout(driver)
   login(driver) 
   



   