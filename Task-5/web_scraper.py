import requests
from bs4 import BeautifulSoup
import json

URL = "https://quotes.toscrape.com/"

def scrape_quotes():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = []

        for item in soup.select(".quote"):
            text = item.select_one(".text").get_text(strip=True)
            author = item.select_one(".author").get_text(strip=True)

            quotes.append({
                "quote": text,
                "author": author
            })

        with open("quotes.json", "w", encoding="utf-8") as file:
            json.dump(quotes, file, indent=4, ensure_ascii=False)

        print(f"Successfully saved {len(quotes)} quotes to quotes.json")

    except requests.RequestException as error:
        print("Error fetching website:", error)

if __name__ == "__main__":
    scrape_quotes()
