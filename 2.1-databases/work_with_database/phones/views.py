from django.shortcuts import render, redirect
from phones.models import Phone
from django.db.models import Avg, Max, Min
from django.db.models.functions import Lower

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    phones_name = phones.order_by(Lower('name'))
    print(phones_name)
    context = {'phones': phones_name}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
