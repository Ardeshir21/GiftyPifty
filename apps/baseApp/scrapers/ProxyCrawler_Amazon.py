from urllib.request import urlopen
from urllib.parse import quote_plus
import ast

"""
Using proxycrawl.com to extract data from Amazon. Their API has a scraper=amazon-product-details
which helps to extract all the pictures and information in a dictionary.

The keys in crawled_dict:

original_status
pc_status
url
body
        # the subkeys in body:
        name
        price
        canonicalUrl
        isPrime
        inStock
        mainImage
        images
        videos
        byLineInfo
        brand
        merchantInfo
        customerReview
        customerReviewCount
        editorialReviews
        warrantyMessage
        shippingMessage
        climatePledgeFriendly
        features
        description
        breadCrumbs
        productInformation
        manufacturerProductDescription
        sponsoredAds
        productReviewBottom
        reviews

"""

class ProductPage():
    def __init__(self, product_link):
        try:
            url = quote_plus(product_link)
            handler = urlopen('https://api.proxycrawl.com/?token=TR9ra9jPRdm7fgmY_uv5Lw&scraper=amazon-product-details&url=' + url)
            proxycrawl_output=handler.read()
            proxycrawl_output_decoded = proxycrawl_output.decode("UTF-8")
            # These changes need to be implementated in order to make a dictionary
            proxycrawl_output_decoded = proxycrawl_output_decoded.replace('null', 'None')
            proxycrawl_output_decoded = proxycrawl_output_decoded.replace('true', 'True')
            proxycrawl_output_decoded = proxycrawl_output_decoded.replace('false', 'False')
            crawled_dict = ast.literal_eval(proxycrawl_output_decoded)
        # When the request is not a valid URL
        except: self.page_soup = None
        # Server Error and other errors
        if crawled_dict['original_status'] >= 400:
            self.page_soup = None
        else:
            self.page_soup = crawled_dict

    def information(self):
        body_dict = self.page_soup['body']

        # Price
        price = body_dict['price']
        if price is not None:
            price = float(price.replace('$', ''))

        # Descripton: About this item - List of bullets
        description_list = body_dict['features']

        # First Image
        main_image = body_dict['mainImage']
        images_list = body_dict['images']

        # result
        result = {
            'Price': price,
            'Description List': description_list,
            'Main Image': main_image,
            'Other Images': images_list
        }
        return result
