from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from django.db.models import Max, Min, Q
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# form applications
from . import models


# Here is the Extra Context ditionary which is used in get_context_data of Views classes
def get_extra_context():
    extraContext = {
        'something': 'ADD SOMETHING HERE',
        }
    return extraContext

# Index View
class IndexView(generic.TemplateView):
    template_name = 'baseApp/layouts/cafe/index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Append shared extraContext
        context.update(get_extra_context())
        context['featured_products'] = models.Product.objects.filter(featured=True, active=True)
        return context

class ProductDetailView(generic.DetailView):
    context_object_name = 'product'
    model = models.Product
    template_name = 'baseApp/layouts/cafe/product.html'
    query_pk_and_slug = True
    slug_url_kwarg = 'product_slug'
    pk_url_kwarg = 'pk'


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Append shared extraContext
        context.update(get_extra_context())
        # This returns __str__ of the object
        # context['page_title'] = self.get_object()
        # context['page_slug'] = self.kwargs['product']
        # context['page_url_detector'] = 'three level depth url'
        # context['products'] = models.Product.objects.filter(category__slug=self.kwargs['category'], status=True).exclude(slug=self.kwargs['product'])

        return context
