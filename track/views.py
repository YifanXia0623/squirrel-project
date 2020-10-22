from django.shortcuts import render
from django.http import HttpResponse
from .models import Sighting

def map(request):
    return render(request, 'track/map.html', {})

def list_sightings(request):
    sighting = Sighting.objects.all()
    context = {
            'sighting': sighting,
    }
    return render(request, 'track/index.html', context)

def update_sighting(request):
    return render(request, 'track/map.html', {})

def create_sighting(request):
    return render(request, 'track/map.html', {})

def obtain_stats(request):
    return render(request, 'track/map.html', {})
