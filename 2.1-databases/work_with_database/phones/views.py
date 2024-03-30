from django.shortcuts import render, redirect, HttpResponse
from phones.models import Phone
from django.db.models import Avg, Max, Min
from django.db.models.functions import Lower

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    # post_ = request.GET['sort']
    # phones = Phone.objects.all()
    print(request.GET)
    if request.GET == {}:
        phones = Phone.objects.all()
    elif request.GET['sort'] == 'name':
        phones = Phone.objects.all().order_by(Lower('name'))
    elif request.GET['sort'] == 'min_price':
        phones = Phone.objects.all().aggregate(Min('price'))

    context = {'phones': phones,}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)




