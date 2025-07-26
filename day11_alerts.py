from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup driver
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
print("🌐 Opened JS Alerts page")

time.sleep(1)  # Let the page load

# ✅ Click the correct alert button
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
print("✅ Clicked JS Alert Button")

# ✅ Handle the alert popup
alert = driver.switch_to.alert
print("⚠️ Alert Text:", alert.text)
alert.accept()
print("✅ Alert Accepted")

time.sleep(2)
driver.quit()