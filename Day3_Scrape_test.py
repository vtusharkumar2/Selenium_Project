from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Step 1: Setup ChromeDriver
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Step 2: Open Wikipedia
driver.get("https://www.wikipedia.org")

# Step 3: Click the English link
english_link = driver.find_element(By.ID, "js-link-box-en")
english_link.click()

# Step 4: Wait a bit
time.sleep(2)

# Step 5: Get the main heading text (screenshot it with your eyes)
heading = driver.find_element(By.ID, "mp-welcome")
print("Heading found:", heading.text)

if heading.text == "Welcome to Wikipedia,":
    print("✅ Test Passed: Heading is correct")
else:
    print("❌ Test Failed: Heading text is incorrect")

# Step 6: Close browser
driver.quit()