from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    db = settings.BUS_STATION_CSV
    with open(db, 'r') as f:
        file = csv.DictReader(f)


        # print(num)
        # for i in file:
        #     print(i['ID'])

        paginator = Paginator(num, 10)
        page = paginator.get_page(5)


    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

        context = {
            'bus_stations': file,
            'page': page,
        }
        return render(request, 'stations/index.html', context)
