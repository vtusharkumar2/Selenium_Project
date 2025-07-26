from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Step 1: Setup browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 2: Open the menu hover test site
driver.get("https://demoqa.com/menu")
print("🌐 Opened website")

# Step 3: Locate the 'Main Item 2' which opens submenu on hover
main_item2 = driver.find_element(By.XPATH, "//a[text()='Main Item 2']")
print("✅ Found Main Item 2")

# Step 4: Hover on 'Main Item 2'
actions = ActionChains(driver)
actions.move_to_element(main_item2).perform()
print("🎯 Hovered over 'Main Item 2'")

# Step 5: Wait for sub-menu to appear
time.sleep(1)

# Step 6: Hover on 'SUB SUB LIST »'
sub_sub_list = driver.find_element(By.XPATH, "//a[text()='SUB SUB LIST »']")
actions.move_to_element(sub_sub_list).perform()
print("🎯 Hovered over 'SUB SUB LIST »'")

# Step 7: Wait and then click on 'Sub Sub Item 1'
time.sleep(1)
sub_sub_item1 = driver.find_element(By.XPATH, "//a[text()='Sub Sub Item 1']")
sub_sub_item1.click()
print("🖱️ Clicked on 'Sub Sub Item 1'")

# Final Step: Close browser
time.sleep(3)
driver.quit()
print("✅ Done and closed browser")