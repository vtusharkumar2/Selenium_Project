#importing all tools
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

#Step 1 open chrome and maximize it

driver=webdriver.Chrome()
driver.maximize_window()

#Step 2 open file upload page

driver.get("https://the-internet.herokuapp.com/upload")
print("opened upload page")

# store file name as variable and abstract its full path for selenium to later upload

file_name="sample_upload.txt"
file_path=os.path.abspath(file_name)

#finding choose files as html file-upload and then uploading our file
upload_input=driver.find_element(By.ID,"file-upload")
upload_input.send_keys(file_path)
print(f"selected file:{file_path}")

#Locate submit button as html file-submit and click on it
driver.find_element(By.ID,"file-submit").click()
print("uploaded the file")

#Confirm the upload by checking if File Uploaded! text appears or not

message=driver.find_element(By.TAG_NAME,"h3").text

if "File Uploaded!" in message:
    print("file uploaded successfully")
else:
    print("Upload failed")


#Wait then close Chrome
time.sleep(5)
driver.quit()