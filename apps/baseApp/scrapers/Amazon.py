import requests
from bs4 import BeautifulSoup


class ProductPage():
    def __init__(self, product_link):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
                'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language' : 'en-US,en;q=0.9',
                'pragma': 'no-cache',
                'cache-control': 'no-cache',
                'Accept-Encoding' : "gzip, deflate, br",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Sec-Fetch-Dest": "document",
                'referer': 'https://www.amazon.com/',
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                'DNT' : '1', # Do Not Track Request Header
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

        # Descripton: About this item - List of bullets
        description_ul = str(self.page_soup.select_one('#feature-bullets > ul'))

        # First Image
        image = self.page_soup.select_one('#landingImage')
        if image is not None:
            image = image['data-old-hires']

        # result
        result = {
            'Location': country,
            'Price': price,
            'Description List': description_ul,
            'Image URL': image
        }
        return result
