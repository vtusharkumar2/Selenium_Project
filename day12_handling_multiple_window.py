from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Setup driver

driver= webdriver.Chrome()
driver.maximize_window()

#step 1 open the test page

driver.get("https://the-internet.herokuapp.com/windows")
print("opened test page!")

#Step 2 click the link to oepn new window
driver.find_element(By.LINK_TEXT,"Click Here").click()
print("clicked, click here to open new tab")

#Step 3 get all window handles

windows=driver.window_handles

print(f"windows found:{windows}")

# step4 switch to the new window
driver.switch_to.new_window(windows[1])

print("switched to new window/tag")

#Step 5 get content of the new tab
heading=driver.find_element(By.TAG_NAME,"h3").text
print("heading on new tab", heading)

#Step6 close the new tab and switch back
driver.close()
driver.switch_to.window(windows[0])
print("switched back to original window")

#Final wait and quit

time.sleep(2)
driver.quit()