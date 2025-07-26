from selenium import webdriver
from selenium.webdriver.common.by import By
from login_page import LoginPage
from logger import setup_logger
import time


#open chrome, maximize,goto site

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://practicetestautomation.com/practice-test-login/")
print("opened the website")


login_page=LoginPage(driver)

login_page.enter_username("student")
login_page.enter_password("Password123")
login_page.click_login()
print("login attempted")



assert login_page.is_login_successful()
print("login successful assertion passed")



from logger import setup_logger

logger = setup_logger()

def test_login_successful():
    logger.info("Test started: test_login_successful")
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    logger.info("Filling login form")
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    logger.info("Checking URL after login")
    assert driver.current_url == "https://practicetestautomation.com/logged-in-successfully/"
    
    logger.info("Test passed")
    driver.quit()


time.sleep(5)
driver.quit()