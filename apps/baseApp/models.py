from django.db import models
from django.urls import reverse_lazy, reverse
from django.utils import timezone


####################
# Variables
YES_NO_CHOICES = [(True, 'Yes'), (False, 'No')]

GENDER_LIST = [
    ('MA',"Male"),
    ('FE',"Female"),
    ('UN', "Unisex")
]

####################
# Affiliate and IDs
class Affiliate(models.Model):
    name = models.CharField(max_length=60)
    associate_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return '{}: {}'.format(self.name, self.associate_id)

    class Meta():
        verbose_name_plural = "Affiliate and IDs"

# Main Category
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = "Categories"

# Sub Category
class SubCategory(models.Model):
    main_category = models.ForeignKey(Category, related_name='main_categories', null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{} > {}'.format(self.main_category, self.name)

    class Meta():
        verbose_name_plural = "Sub Categories"
        unique_together = ('main_category', 'name',)


# Ocassion
class Ocassion(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = "Ocassions"

# Interest
class Interest(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = "Interests"

# Tag
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = "Tags"

# Recipient
class Recipient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = "Recipients"

# Product
class Product(models.Model):
    affiliate = models.ForeignKey(Affiliate, related_name='affiliates', null=True, on_delete=models.CASCADE)
    main_url = models.CharField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=300)
    gender = models.CharField(max_length=15, choices=GENDER_LIST, default='UN')
    category = models.ManyToManyField(Category, related_name='categories', null=True)
    sub_category = models.ManyToManyField(SubCategory, related_name='sub_categories', null=True)
    ocassion = models.ManyToManyField(Ocassion, related_name='ocassions', null=True)
    interest = models.ManyToManyField(Interest, related_name='interests', null=True)
    tag = models.ManyToManyField(Tag, related_name='tags', null=True)
    recipient = models.ManyToManyField(Recipient, related_name='recipients', null=True)
    description = models.TextField(max_length=5000, null=True, blank=True)
    scraped_description = models.TextField(max_length=5000, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=10.00, null=True, blank=True)
    active = models.BooleanField(choices=YES_NO_CHOICES, default=True)
    featured = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    slug = models.SlugField(max_length=300, blank=True, null=True, allow_unicode=True)
    created_on = models.DateField(editable=False)
    updated_on = models.DateField(editable=False, null=True)

    def __str__(self):
        return self.name

    class Meta():
        ordering  = ['-created_on']
        verbose_name_plural = "Products"

    def save(self, *args, **kwargs):
        # update or create time
        if not self.id:
            self.created_on = timezone.now()
        self.updated_on = timezone.now()

        return super(Product, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('resumeApp:personal-resume-private', kwargs={'user_id':self.user.pk,
    #                                                             'full_name':self.user.slug})

# Product Images
class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.CharField(max_length=1000, null=True, blank=True)
    display_order = models.PositiveIntegerField(null=True, blank=True)

    class Meta():
        verbose_name_plural = "Product Images"
        ordering = ['display_order']
