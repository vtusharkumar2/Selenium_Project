def test_screenshot_fail(driver):
    driver.get("https://example.com")
    assert False

    