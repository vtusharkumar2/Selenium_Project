#import every tool
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#launch chrome and maximize window
driver=webdriver.Chrome()
driver.maximize_window()

#Open the website in google
driver.get("https://testautomationpractice.blogspot.com/")
print("opened the website")

#Locate the table
table=driver.find_element(By.XPATH,"//table[@name='BookTable']")
print("Found the book table")

#find the no of rows
rows=table.find_elements(By.TAG_NAME,"tr")
print(f"the no. of rows are: {len(rows)}")

#loop horizontally one by one each row 
for i in range(1,len(rows)):
    #suppose first row has tushar 21 pink cols=..helps in finding these
    cols=rows[i].find_elements(By.TAG_NAME,"td")
    #row_data converts the data found into text 
    row_data=[col.text for col in cols]

    #for printing the converte text
    print(f"rows{i}:{row_data}")

#pause and close chrome

time.sleep(5)
driver.quit()
  
               
