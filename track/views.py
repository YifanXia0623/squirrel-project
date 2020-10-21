from django.shortcuts import render
from django.http import HttpResponse

def map(request):
    return render(request, 'track/map.html', {})

def list_sightings(request):
    return render(request, 'track/map.html', {})

def update_sighting(request):
    return render(request, 'track/map.html', {})

def create_sighting(request):
    return render(request, 'track/map.html', {})

def obtain_stats(request):
    return render(request, 'track/map.html', {})
