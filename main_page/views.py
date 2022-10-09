from django.shortcuts import render
from main_page.models import *
from django.shortcuts import render
#from django.core.exceptions import ImproperlyConfigured
from django.views.generic import ListView


class ProductView(ListView):
    template_name = 'product.html'
    queryset = Product.objects.all()
