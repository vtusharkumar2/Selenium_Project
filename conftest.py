import pytest
import logging
import datetime
import os
from selenium import webdriver

@pytest.fixture
def driver():
    driver=webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)    #customise pytest to make extra code eg. to take ss after each test
def pytest_runtest_makereport(item,call):
    outcome=yield  #pause the test 
    report=outcome.get_result()   #store the result pass? fail?..

    if report.when=="call" and report.failed:  #make sure test is failed make sure its in main test body
        driver=item.funcargs.get("driver")     #get chrome browser used

        if driver:
            screenshot_dir=os.path.join(os.getcwd(),"screenshots") #make screenshot folder and know it's path
            os.makedirs(screenshot_dir,exist_ok=True)   #
            
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name=report.nodeid.replace("::","_").replace("/","_")
            file_name=f"{test_name}_{timestamp}.png"

            file_path=os.path.join(screenshot_dir,file_name)
            driver.save_screenshot(file_path)
            print(f"screenshot saved: {file_path}")


#configure logger

logging.basicConfig(
    filename="logfile.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)



#logging fixture

@pytest.fixture

def driver():
    logging.info("launching chrome")
    driver=webdriver.Chrome()
    driver.maximize_window()
    logging.info("opened google and maximized window") 
    yield driver                                         #for running the test   
    
    driver.quit()

    logging.info("closed the browser")








