from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# 1) Launch browser
driver = webdriver.Chrome()

# 2) Open the working dropdown practice page
driver.get("https://practice.expandtesting.com/dropdown")
time.sleep(2)

# 3) Find the simple dropdown (first one)
simple_dropdown = Select(driver.find_element(By.ID, "dropdown"))

# 4) Print available options
print("Options in dropdown:")
for opt in simple_dropdown.options:
    print("-", opt.text)

# 5) Select 'Option 2'
simple_dropdown.select_by_visible_text("Option 2")
print("✅ Selected 'Option 2'")
time.sleep(2)

# 6) Close browser
driver.quit()