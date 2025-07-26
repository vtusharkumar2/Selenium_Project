from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Optional: Automatically opens and controls Chrome
service = Service()
driver = webdriver.Chrome(service=service)

# 1️⃣ Open the test site
driver.get("https://the-internet.herokuapp.com/windows")
print("🌐 Opened the test page")

# 2️⃣ Click the link that opens a new tab
driver.find_element(By.LINK_TEXT, "Click Here").click()
print("🖱️ Clicked 'Click Here' to open a new tab")

# 3️⃣ Get list of all open windows (returns list of window handles)
windows = driver.window_handles
print("🪟 Windows found:", windows)

# 4️⃣ Switch to the new window (second one in list)
driver.switch_to.window(windows[1])
print("🔁 Switched to new tab/window")

# 5️⃣ Wait for the h3 tag to appear on the new tab
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "h3"))
)

# 6️⃣ Extract and print the heading text
heading = driver.find_element(By.TAG_NAME, "h3").text
print("✅ Heading text found:", heading)

# 7️⃣ Close the new tab
driver.close()
print("❌ Closed the new tab")

# 8️⃣ Switch back to original window
driver.switch_to.window(windows[0])
print("🔙 Switched back to original tab")

# Optional: Give time to observe
time.sleep(2)
driver.quit()