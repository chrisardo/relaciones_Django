from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant
# Create your views here.


def create(request):
    place = Place(name="lugar1", address="Calle demo")
    place.save()
    restaurant = Restaurant(place=place, number_of_employees=10)
    restaurant.save()

    # Crear elementos
    return HttpResponse(restaurant.place.name)
