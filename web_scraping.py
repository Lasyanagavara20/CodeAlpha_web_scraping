import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "http://books.toscrape.com/catalogue/page-{}.html"
books = []

for page in range(1, 51):  # There are 50 pages
    url = base_url.format(page)
    print(f"Scraping: {url}")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for book in soup.select(".product_pod"):
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text
        availability = book.select_one(".availability").text.strip()
        rating_class = book.select_one(".star-rating")["class"]
        rating = rating_class[1] if len(rating_class) > 1 else "No rating"

        books.append({
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Rating": rating
        })

# Save to CSV
df = pd.DataFrame(books)
df.to_csv("all_books.csv", index=False, encoding="utf-8-sig")
print("\nScraping complete. Saved to all_books.csv")

