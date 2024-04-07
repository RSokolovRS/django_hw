from django.shortcuts import render, redirect
from phones.models import Phone
from django.db.models import Avg, Max, Min
from django.db.models.functions import Lower

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    if request.GET == {}:
        phones = Phone.objects.all()
    elif request.GET['sort'] == 'name':
        phones = Phone.objects.all().order_by(Lower('name'))
    elif request.GET['sort'] == 'min_price':
        phones = Phone.objects.order_by('price')
    elif request.GET['sort'] == 'max_price':
        phones = Phone.objects.order_by('-price')
    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)

