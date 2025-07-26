from selenium.webdriver.common.by import By

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

    

    def is_login_successful(self):
        expected_url="https://practicetestautomation.com/logged-in-successfully/"
        actual_url=self.driver.current_url
        return expected_url == actual_url