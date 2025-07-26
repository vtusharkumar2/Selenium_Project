# importing everything
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os


#Set up downlaod directory
download_dir=os.path.abspath("downloads")

#to make if folder and handle if it exists already
os.makedirs(download_dir,exist_ok=True)

#To control chrome download settings for easy download without pop ups and error

chrome_options=Options()
chrome_options.add_experimental_option("prefs",{ #prefs for adding more preferences on handling chrome
    "download.default_directory": download_dir,   #specifying the directory of downlaod
    "download.prompt_for_download":False,         #To canclet the pop-up
    "download.directory_upgrade":False,            #overrite the folder if it already exists so no error
    "safebrowsing.enabled":True                    #To allow downloads on chrome
})


#open chrome and make the abhove options as new options for chrome after that maximize it

driver=webdriver.Chrome(options=chrome_options)
driver.maximize_window()

#open file download test site and print opened

driver.get("https://demo.automationtesting.in/FileDownload.html")
print("Opened the download site")


#To find the text box using id=textbox and type "tushar was here!"
driver.find_element(By.ID,"textbox").send_keys("Tushar was here!")

#To click on save to safe the file as txt

driver.find_element(By.ID,"createTxt").click()
#print sts
print("Text file created")


#now clicking on download button
time.sleep(1)  #To see what's happening
driver.find_element(By.ID,"link-to-download").click()
print("download initiated")  #To notify download beginnning

#Confirming if file exists or not

downloaded_file=os.path.join(download_dir,"info.txt")

timeout = 10
while timeout:
    if os.path.exists(downloaded_file):
        print("✅ File downloaded successfully:", downloaded_file)
        break
    time.sleep(1)
    timeout -= 1
else:
    print("❌ File does not exist")

driver.quit()





