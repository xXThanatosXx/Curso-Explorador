import requests
from bs4 import BeautifulSoup

def get_product_price(url, selector):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        price_element = soup.select_one(selector)
        if price_element:
            price = price_element.text.strip()
            return price
        else:
            return None
    else:
        return None

def scrape_product_prices(products):
    data = []
    for product in products:
        for entry in product['urls']:
            price = get_product_price(entry['url'], entry['selector'])
            if price:
                data.append({"Product": product['name'], "Store": entry['store'], "Price": price})
    return data
