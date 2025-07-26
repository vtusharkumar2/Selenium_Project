#Step 1 import everything
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



#Step 2 open chrome,maximizeand load the website
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
print("Opened alert website")
time.sleep(2)         #for seeing

#click on Click for JS Alert. message
driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
time.sleep(2)
print("found the first button Click for JS Alert")

#switch the focus to alert and then click on ok(accept)

alert= driver.switch_to.alert
print("shifted to alert")
alert.accept()    #click on Ok
print("alert handled")


#Click on Click for JS Confirm

driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
time.sleep(3)
print("clicked on 2nd button Click for JS Confirm")

#alert appears shift focus to alert then dismiss it(click on cancel)
alert = driver.switch_to.alert
time.sleep(2)
alert = alert.dismiss()
print("Alert dismissed")



#Click on Click for JS Prompt
driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
time.sleep(3)
print("Clicked on 3rd option Click for JS Prompt ")

alert=driver.switch_to.alert #shift focus to alert
alert.send_keys("tushar was here")  #typing into alert
time.sleep(3)
print("Typed into fiedls")

alert.accept()   #click ok
print("Clicked ok")

time.sleep(4)
driver.quit()   #exit chrome



