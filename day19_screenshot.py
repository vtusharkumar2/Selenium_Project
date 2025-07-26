#import everything

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os


#open chrome, maximize, go to site and print confirmation
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Register.html")
print("opened the testing website")

#store the absolute path of the folder inside a variable, make a folder on this path even if there is no folder 


screenshot_dir=os.path.abspath("screenshots")
os.makedirs(screenshot_dir,exist_ok=True)


#take full page screenshot

full_page=os.path.join(screenshot_dir,"fullpage.png")    #stors full path on png file of screenshot
driver.save_screenshot(full_page)                        #takes a full page screenshot and saves as the name mentioned in path
print(f"screenshot saved at:{full_page}")               #confirmation


#taking screenshot of a specific element

#find element
first_name_input=driver.find_element(By.XPATH,"//input[@placeholder='First Name']")
#make it's path
first_name_ss_path=os.path.join(screenshot_dir,"element.png")
#take the screenshot at path
first_name_input.screenshot(first_name_ss_path)
#print confirmation
print(f"screenshot saved at:{first_name_ss_path}")


#ending
time.sleep(5)
driver.quit()