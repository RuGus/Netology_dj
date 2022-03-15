import csv

from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
from requests_toolbelt import StreamingIterator


def index(request):
    return redirect(reverse("bus_stations"))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get("page", 1))
    station_list = []
    with open(BUS_STATION_CSV) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            station = {
                "Name": row["Name"],
                "Street": row["Street"],
                "District": row["District"],
            }
            station_list.append(station)
    paginator = Paginator(station_list, 10)
    page = paginator.get_page(page_number)

    context = {
        "bus_stations": page.object_list,
        "page": page,
    }
    return render(request, "stations/index.html", context)
