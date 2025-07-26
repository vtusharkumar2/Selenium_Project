from logger import set_log
from selenium import webdriver
from logger import setup_logger
import pytest

logger = set_log()
logger.info("Testing log output")

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    # Simulate failure:
    assert driver.title == "Incorrect Title"