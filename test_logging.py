import logging 

def test_google(driver):
    logging.info("Starting test")
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    logging.info("Google loaded successfully")
