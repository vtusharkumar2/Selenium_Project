# step 1 import everything
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#Create page class


class LoginPage:
    def __init__(self,driver):
        self.driver=driver

        self.username_input=(By.ID,"username")
        self.password_input=(By.ID,"password")
        self.login_button=(By.ID,"submit")

    def enter_username(self,username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()



#test script
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://practicetestautomation.com/practice-test-login/")
print("opened the website")

login_page=LoginPage(driver)

#use methods
login_page.enter_username("student")
login_page.enter_password("Password123")
login_page.click_login()
print("login attempted")

time.sleep(5)
driver.quit()




   