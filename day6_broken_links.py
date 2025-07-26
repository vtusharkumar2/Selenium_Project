import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")
print("🌐 Opened Wikipedia")

time.sleep(2)

links = driver.find_elements(By.TAG_NAME, "a")
print(f"🔗 Total links found: {len(links)}")

# Check only first 20 links
for index, link in enumerate(links[:20], start=1):
    url = link.get_attribute("href")
    if url and url.startswith("http"):
        try:
            response = requests.head(url, timeout=5)
            if response.status_code >= 400:
                print(f"{index}. ❌ Broken: {url} [Status: {response.status_code}]")
            else:
                print(f"{index}. ✅ Working: {url} [Status: {response.status_code}]")
        except Exception as e:
            print(f"{index}. ⚠️ Error checking {url}: {e}")

driver.quit()
print("✅ Test Completed")