from django.contrib import admin
from django import forms
from django.db import models
from .models import (Affiliate,
                    Category, SubCategory, Ocassion, Interest, Tag,
                    Product, ProductImages,
                    )

######################
# Inline Forms
class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    list_display = ['product', 'image', 'display_order']
    list_editable = ['display_order']
    # Read more https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#modeladmin-methods
    # You may upload multiple images with one upload process and save the seperatly in the backend.
    # formfield_overrides = {
    #     models.ImageField: {'widget': forms.ClearableFileInput(attrs={'multiple': True})},
    # }


######################
class ProductAdmin(admin.ModelAdmin):

    # search_fields = ['complex']
    list_filter = ['name']
    list_display = ['id', 'created_on', 'name', 'active', 'featured', 'price']
    list_editable = ['active', 'featured']
    prepopulated_fields = {'slug': ('name',)}

    # other Inlines
    # inlines = [
    #     ProductImagesInline,
    # ]

    # Using Widgets
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple(attrs={'multiple': True})},
    }

class AffiliateAdmin(admin.ModelAdmin):
    list_display = ['name', 'associate_id']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'main_category', 'name']

class OcassionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class InterestAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Affiliate, AffiliateAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Ocassion, OcassionAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(Tag, TagAdmin)
