from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open('data-398-2018-08-30.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        bus_stations = tuple(reader)
        paginator = Paginator(bus_stations, 10)
        page_number = request.GET.get("page")
        page = paginator.get_page(page_number)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

        context = {
                 'bus_stations': page,
                 'page': page,
            }
    return render(request, 'stations/index.html', context)
