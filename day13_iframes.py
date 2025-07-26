#import all the tools
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#open chrome and maxize it
driver= webdriver.Chrome()
driver.maximize_window()

#go to the site
driver.get("https://demo.automationtesting.in/Frames.html")

#find button Single Iframe and click on it
driver.find_element(By.LINK_TEXT,"Single Iframe").click()
print("switched to Iframe")  #for confirming

#Switch to the Iframe(focus oon the iframe window)
iframe= driver.find_element(By.ID,"singleframe")
driver.switch_to.frame(iframe)
print("switched to iframe")

#Locate input box by html tag then Type inside the input box

input_box=driver.find_element(By.TAG_NAME,"input")
input_box.send_keys("Tushar was here")
print("types into input box")

#Switch back to main page
driver.switch_to.default_content()
print("switched back to main frame")


#Add delay
time.sleep(5)

#to exit window
driver.quit()