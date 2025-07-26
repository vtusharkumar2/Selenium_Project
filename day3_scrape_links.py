#import everything
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

#setup 
service=Service("chromedriver.exe")
driver=webdriver.Chrome(service=service)

#open wikipedia and locate links tab
driver.get("https://en.wikipedia.org/wiki/Main_Page")
time.sleep(3)

#from did you know find all the apearing links
facts=driver.find_elements(By.CSS_SELECTOR,"#mp-dyk a")

#print the no. of facts

print("The number of facts are:",len(facts))

#print all link text

for idx,fact in enumerate(facts,1):
    print(f"{idx}.{fact.text}")
    

#to check that there is no missing facts

if all(fact.text.strip()!="" for fact in facts):
    print("Test passed all facts are there")
else:
    print("test failed there are some missing facts")


#to print empty fact

for idx,fact in enumerate(facts,1):
    if fact.text.strip() == "":
        print(f"empty fact found at {idx}.{fact}")
    


#Close the browser

time.sleep(3)
driver.quit()


