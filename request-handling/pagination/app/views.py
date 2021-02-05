from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
from urllib.parse import quote_plus, urlencode
from django.core.handlers.wsgi import WSGIRequest

import csv


def index(request):
    return redirect(reverse(bus_stations))

def createList()->list:
    bus_stations_list = []
    with open(file=f"{settings.BUS_STATION_CSV}", mode="r", encoding="cp1251") as f:
        reader = csv.DictReader(f)
        for row in reader:
            bus_stations_dict={}
            bus_stations_dict["Name"] = row["Name"]
            bus_stations_dict["Street"] = row["Street"]
            bus_stations_dict["District"] = row["District"]
            bus_stations_list.append(bus_stations_dict)
    return bus_stations_list


def bus_stations(request: WSGIRequest):
    paginator = Paginator(createList(), 10)
    page_number = int(request.GET.get("page", 1))
    page = paginator.get_page(page_number)
    next_page_url = reverse(bus_stations) + "?" + urlencode({"page":str(page_number + 1)})
    prev_page_url = reverse(bus_stations) + "?" + urlencode({"page":str(page_number - 1)})
    return render(request, 'index.html', context={
        'bus_stations': page.object_list,
        'current_page': page_number,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

