from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    # obj_phon = Phone.objects.all()
    # phones = [f'{i.name}' for i in obj_phon]
    # print(phones)
    context = {}
    return render(request, template, context)
