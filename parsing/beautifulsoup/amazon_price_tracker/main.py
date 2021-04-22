import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

BUY_PRICE = 100
URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
YOUR_EMAIL = "YOUR_EMAIL"
YOUR_PASSWORD = "YOUR_PASSWORD"

headers = {"Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"}

response = requests.get(URL, headers=headers)
item_amazon_page = response.text

soup = BeautifulSoup(item_amazon_page, "lxml")
price = soup.find(name="span", id="priceblock_ourprice").get_text()
price_as_float = float(price.split("$")[1])
title = soup.find(id="productTitle").get_text().strip()
print(price_as_float)

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )
