import smtplib
import requests
# import lxml
from bs4 import BeautifulSoup

url = ("https://www.amazon.in/ASUS-Vivobook-i5-13500H-Laptop-S5504VA-MA541WS/dp/B0BSDZY5FV/ref=sr_1_7?crid"
       "=2OHKC44UYIZYG&keywords=asus+vivobook+s15+oled+2023&qid=1692670162&sprefix=asus+vivobook+s%2Caps%2C270&sr=8-7")
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
# print(title)

BUY_PRICE = 70000

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("YOUR_SMTP_ADDRESS", port=587) as connection:
        connection.starttls()
        result = connection.login("YOUR_EMAIL", "YOUR_PASSWORD")
        connection.sendmail(
            from_addr="YOUR_EMAIL",
            to_addrs="YOUR_EMAIL",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
