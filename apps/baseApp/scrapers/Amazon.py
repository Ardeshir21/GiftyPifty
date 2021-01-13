import requests
from bs4 import BeautifulSoup


class ProductPage():
    def __init__(self, product_link):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
                'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language' : 'en-US,en;q=0.5',
                'Accept-Encoding' : 'gzip',
                'DNT' : '1', # Do Not Track Request Header
                'Connection' : 'close'
                }
            page = requests.get(product_link, headers=headers)
        # When the request is not a valid URL
        except: return None
        self.page_soup = BeautifulSoup(page.content, 'html.parser')


    def information(self):
        # Country
        country = self.page_soup.select_one('#glow-ingress-line2')
        if country is not None:
            country = country.text.strip()

        # Price
        price = self.page_soup.find("span", attrs={'id':'priceblock_ourprice'})
        if price is not None:
            price = price.string.strip()
            price = float(price.replace('$', ''))
        print(price)
        # Descripton: About this item - List of bullets
        description_ul = str(self.page_soup.select_one('#feature-bullets > ul'))

        # First Image
        image = self.page_soup.select_one('#landingImage')['data-old-hires']

        # result
        result = {
            'Location': country,
            'Price': price,
            'Description List': description_ul,
            'Image URL': image
        }
        return result
