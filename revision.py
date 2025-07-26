from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup
driver = webdriver.Chrome()
driver.maximize_window()

# Step 1: Open the page
driver.get("https://the-internet.herokuapp.com/iframe")
print("🌐 Opened page with iframe")

# Step 2: Switch to iframe
iframe_element = driver.find_element(By.ID, "mce_0_ifr")
driver.switch_to.frame(iframe_element)
print("🔄 Switched to iframe")

# Step 3: Interact with elements inside iframe
text_box = driver.find_element(By.ID, "tinymce")

# CLEAR using JS (body tag can't be cleared directly)
driver.execute_script("arguments[0].innerHTML = '';", text_box)

# Send keys normally
text_box.send_keys("Hello from Tushar!")
print("✅ Typed inside iframe")

# Step 4: Switch back
driver.switch_to.default_content()
print("🔙 Switched back to main page")

# Optional: Pause and close
time.sleep(5)
driver.quit()