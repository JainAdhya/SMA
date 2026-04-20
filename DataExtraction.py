import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Find all books
books = soup.find_all('article', class_='product_pod')

print("SCRAPED DATA:\n")

for book in books:
    
    # Title
    title = book.h3.a['title']
    
    # Price
    price = book.find('p', class_='price_color').text
    
    # Availability
    availability = book.find('p', class_='instock availability').text.strip()
    
    # Rating (convert text → number)
    rating_class = book.find('p', class_='star-rating')['class'][1]
    
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    
    rating = rating_map.get(rating_class, 0)
    
    # Image link
    image = book.find('img')['src']
    image_link = "https://books.toscrape.com/" + image
    
    # Print extracted data
    print("Title:", title)
    print("Price:", price)
    print("Availability:", availability)
    print("Rating:", rating)
    print("Image:", image_link)
    print("-" * 50)