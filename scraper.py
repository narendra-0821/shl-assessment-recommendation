import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.shl.com/solutions/products/product-catalog/"

def scrape_shl_catalog():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    assessments = []

    cards = soup.find_all('div', class_='product-card')
    for card in cards:
        name = card.find('h3').get_text(strip=True)
        url = card.find('a', href=True)['href']
        details = card.get_text(separator='|')

        assessments.append({
            "name": name,
            "url": url,
            "description": details,
            "remote_testing": "Yes" if "Remote" in details else "No",
            "adaptive_irt": "Yes" if "adaptive" in details.lower() else "No",
            "duration": "N/A",
            "test_type": "N/A"
        })

    with open("assessments.json", "w") as f:
        json.dump(assessments, f, indent=2)

if __name__ == "__main__":
    scrape_shl_catalog()