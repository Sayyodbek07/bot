import requests
from bs4 import BeautifulSoup

url = "https://asaxiy.uz/product/telefony-i-gadzhety/telefony/smartfony"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

phones = []
izlash = requests.get(url, headers=headers)
data = izlash.text

suop = BeautifulSoup(data, "html.parser")
main_block = suop.find("div", class_="row")
block = main_block.find_all("div", class_="col-6")
for product in block:
    image = product.find("img", class_="img-fluid")["data-src"]
    product_name = product.find("span", class_="product__item__info-title").get_text()
    phones.append({
        "Kampyuter nomi": product_name,
        "Kompyuter rasmi": image
    })

print(phones)