import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

BASE_URL = "https://www.shl.com/solutions/products/product-catalog/"

def scrape_shl_catalog():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Remove this line if you want to see the browser

    driver_path = os.path.join(os.getcwd(), "drivers", "chromedriver.exe")
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(BASE_URL)

    try:
        # Wait for the assessment cards to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product-card"))
        )
        cards = driver.find_elements(By.CLASS_NAME, "product-card")
    except:
        cards = []

    print(f"Total assessments scraped: {len(cards)}")

    assessments = []
    for card in cards:
        try:
            name = card.find_element(By.TAG_NAME, "h3").text
            url = card.find_element(By.TAG_NAME, "a").get_attribute("href")
            details = card.text

            assessments.append({
                "name": name,
                "url": url,
                "description": details,
                "remote_testing": "Yes" if "Remote" in details else "No",
                "adaptive_irt": "Yes" if "adaptive" in details.lower() else "No",
                "duration": "N/A",
                "test_type": "N/A"
            })
        except Exception as e:
            print("Error parsing card:", e)

    with open("assessments.json", "w") as f:
        json.dump(assessments, f, indent=2)
    print(driver.page_source[:10000])
    driver.quit()

if __name__ == "__main__":
    scrape_shl_catalog()
