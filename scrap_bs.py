import requests
from bs4 import BeautifulSoup
import pandas as pd

books = []
for i in range(1, 21):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    ol = soup.find('ol')
    articles = ol.find_all('article', class_='product_pod')
    for article in articles:
        image = article.find('img')
        img_alt = image.attrs['alt']
        star = article.find('p')
        star1 = star['class'][1]
        price = article.find('p', class_='price_color').text
        price1 = float(price[2:])
        books.append([img_alt, price1, star1])

df = pd.DataFrame(books, columns=['Title', 'Price Of Book in Euro', 'Rating'])
df.to_csv('books.csv', index=False)

