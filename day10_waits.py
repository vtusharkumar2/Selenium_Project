from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. Launch browser
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
print("🌐 Opened the test page")

# 2. Click the Start button
start_button = driver.find_element(By.XPATH, "//div[@id='start']/button")
start_button.click()
print("✅ Clicked 'Start'")

# 3. Wait for the Hello World message to appear
hello_text = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "finish"))
)
print("✅ Message appeared:", hello_text.text)

# 4. Pause for a few seconds to view result
time.sleep(3)

# 5. Close browser
driver.quit()
                                            

                                

