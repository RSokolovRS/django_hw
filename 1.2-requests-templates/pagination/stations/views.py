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
        t = tuple(file)
        # print(t)

        paginator = Paginator(t[1], 5)
        page = request.GET.get('page', 1)
        # print(page)
        page = paginator.get_page(page)
        # print(paginator.get_page(page).object_list)

    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

        context = {
                'bus_stations': t,
                'page': page,
        }
        return render(request, 'stations/index.html', context)
