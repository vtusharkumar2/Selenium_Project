from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://practice.expandtesting.com/checkboxes")
time.sleep(2)

#Locate all checkboxes
checkboxes=driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
print(f"found {len(checkboxes)} checkboxes")

#click each checkbox and verify
for box in checkboxes:
    driver.execute_script("arguments[0].click();", box)
    print(f"✅ Clicked Checkbox | Selected: {box.is_selected()}")

driver.quit()