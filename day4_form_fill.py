from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# ✅ Add these Chrome options
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--start-maximized')

# ✅ Setup WebDriver with options
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Open practice form
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
time.sleep(10)

# Accept cookies if present
try:
    gender = driver.find_element(By.ID, "sex-0")
    driver.execute_script("arguments[0].scrollIntoView();", gender)
    time.sleep(1)
    gender.click()
except:
    pass  # ignore if not found

# Fill first name and last name
driver.find_element(By.NAME, "firstname").send_keys("Tushar")
driver.find_element(By.NAME, "lastname").send_keys("kumar")

# Select gender (Male)
driver.find_element(By.ID, "sex-0").click()

# Select experience (5 years)
driver.find_element(By.ID, "exp-4").click()

# Date
driver.find_element(By.ID, "datepicker").send_keys("06/28/2025")

# Select profession checkboxes
driver.find_element(By.ID, "profession-1").click()  # Automation Tester

# Upload photo (optional - skip this part for now)

# Select Automation Tool
driver.find_element(By.ID, "tool-2").click()  # Selenium Webdriver

# Continent dropdown
Select(driver.find_element(By.ID, "continents")).select_by_visible_text("Europe")

# Selenium commands dropdown (multi-select)
Select(driver.find_element(By.ID, "selenium_commands")).select_by_visible_text("Wait Commands")

# Wait and close
time.sleep(3)
driver.quit()