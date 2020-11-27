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
