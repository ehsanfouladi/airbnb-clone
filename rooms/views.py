from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.urls import reverse
from django_countries import countries
from . import models


class HomeView(ListView):

    """home view"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#     except models.Room.DoesNotExist:
#         raise Http404()
#     return render(request, "rooms/detail.html", {"room": room})


class RoomDetail(DetailView):

    """RoomDetail Definition"""

    model = models.Room


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    room_type = int(request.GET.get("room_type", 0))
    country = request.GET.get("country", "IR")
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    baths = int(request.GET.get("baths", 0))
    instant = request.GET.get("instant", False)
    super_host = bool(request.GET.get("super_host", False))
    s_amenities = bool(request.GET.getlist("amenities"))
    s_facilities = request.GET.getlist("facilities")
    form = {
        "city": city,
        "s_country": country,
        "s_room_type": room_type,
        "s_price": price,
        "s_guests": guests,
        "s_bedrooms": bedrooms,
        "s_baths": baths,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
        "instant": instant,
        "super_host": super_host,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()
    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    filter_args = {}

    if city != "Anywhere":
        filter_args["city__startswith"] = city

    filter_args["country"] = country

    if room_type != 0:
        filter_args["room_type__pk"] = room_type

    if price != 0:
        filter_args["price__lte"] = price

    if guests != 0:
        filter_args["guests__gte"] = guests
    if bedrooms != 0:
        filter_args["bedrooms__gte"] = bedrooms
    if baths != 0:
        filter_args["baths__gte"] = baths

    if instant:
        filter_args["instant_book"] = True
    if super_host:
        filter_args["host__superhost"] = True

    if len(s_amenities) > 0:
        for s_a in s_amenities:
            filter_args["amenities__pk"] = int(s_a)
    if len(s_facilities) > 0:
        for s_f in s_facilities:
            filter_args["amenities__pk"] = int(s_f)
    rooms = models.Room.objects.filter(**filter_args)

    return render(
        request,
        "rooms/search.html",
        {**form, **choices, "rooms": rooms},
    )
