from django.core.management.base import BaseCommand, CommandError
from apps.baseApp import models
from apps.baseApp.scrapers import Amazon


class Command(BaseCommand):
    help = 'Does some magical work'

    def handle(self, *args, **options):
        # Amazon
        all_products = models.Product.objects.all()
        for product in all_products:
            product_scraped_object = Amazon.ProductPage(product.main_url)
            print(product_scraped_object.page_soup)

            # if the URL exists
            if product_scraped_object is not None:
                product_info = product_scraped_object.information()
                # insert new information into product
                country_location = product_info['Location']
                product.price = product_info['Price']
                # Deactivate the product if does not have the Price
                if product.price is None:
                    product.active = False
                product.scraped_description = product_info['Description List']

                # Available Current Product images on the database
                available_images = models.ProductImages.objects.filter(product=product)
                if len(available_images) < 1:
                    # It is from a different model which has ForeignKey of the product
                    image = models.ProductImages(
                                                product=product,
                                                image=product_info['Image URL'],
                                                display_order = 1)
                    image.save()

                product.save()

            self.stdout.write('{} has been updated --- {}'.format(product.name, country_location))
