from selenium import webdriver #tool to control web browser
from selenium.webdriver.chrome.service import Service #service class to get chromedriver path
import time


service=Service("chromedriver.exe") #get file path and give it to selenium to use
driver=webdriver.Chrome(service=service) # use chromedriver from it's assigned path in service clss and give it to driver variable to use different operations

#open google and print it's title

driver.get("https://www.google.com") 
print("page title:",driver.title)


time.sleep(3)
driver.quit()