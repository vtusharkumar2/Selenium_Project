#import everything
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#open chrome,maximize,goto site
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Register.html")
print("opened the website")
time.sleep(3)


#enable javascript and sroll down a bit

driver.execute_script("window.scrollBy(0,500)")
print("scrolled down")
time.sleep(3)

#fill out "tushar" on first name using javascript

first_name=driver.find_element(By.XPATH,"//input[@placeholder='First Name']")
driver.execute_script("arguments[0].setAttribute('value','tushar')",first_name)
time.sleep(3)
print("entered int field using javascript")

#highlight the first anme field

driver.execute_script("arguments[0].style.border='3px solid red'",first_name)
print("highlighted the first name field usind red border")
time.sleep(3)


#find submit button,scroll to the submit button, then fill it with green border then click it

submit_button=driver.find_element(By.ID,"submitbtn")
driver.execute_script("arguments[0].scrollIntoView(true);",submit_button)
time.sleep(3)
print("scrolled down to submit button")
driver.execute_script("arguments[0].style.border='3px solid green'",submit_button)
time.sleep(3)
print("colored the submit button into green")
driver.execute_script("arguments[0].click();",submit_button)
time.sleep(3)
print("clicked using JS")



#quit the browser
driver.quit()