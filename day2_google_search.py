#import everything
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#set up webdriver
service= Service("chromedriver.exe") #to sav path of chromedriver used to manipulate chrome
driver= webdriver.Chrome(service=service)


#open google
driver.get("https://www.google.com")
driver.maximize_window()

#Accept cookies

try:
    accept_cookie=driver.find_element(By.ID,"L2AGLB")
    accept_cookie.click()
except:
    pass

#find search box, type selenium python, click or press enter

search_box=driver.find_element(By.NAME,"q")
search_box.send_keys("Selenium Python")
search_box.submit()


#wait for 3 secs, print the heading then close

time.sleep(3)
print("Title is:",driver.title)
driver.quit()

