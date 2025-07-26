from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Chrome setup
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Step 1: Open the site
driver.get("https://trytestingthis.netlify.app/")
driver.maximize_window()
print("🔍 Opened the form page")
time.sleep(2)

# Step 2: Fill Username
username_input = driver.find_element(By.ID, "uname")
username_input.send_keys("Tushar")
print("✅ Typed username: Tushar")
time.sleep(2)

# Step 3: Fill Password
password_input = driver.find_element(By.ID, "pwd")
password_input.send_keys("MySecret123")
print("✅ Typed password: MySecret123")
time.sleep(2)

# Step 4: Click Submit Button
submit_button = driver.find_element(By.CLASS_NAME, "btn")
submit_button.click()
print("✅ Clicked submit")
time.sleep(3)

# Step 5: Recheck if fields are cleared (form submitted)
username_field = driver.find_element(By.ID, "uname")
password_field = driver.find_element(By.ID, "pwd")
if username_field.get_attribute("value") == "" and password_field.get_attribute("value") == "":
    print("✅ Test Passed: Fields are cleared after submission")
else:
    print("❌ Test Failed: Fields not cleared")

# Final wait so you can SEE everything
time.sleep(5)
driver.quit()