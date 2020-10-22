from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Max, Min, Count, Avg
from .mdoels import Sighting
from .forms import SightingForm

def index(request):
    return render(request, 'track/index.html', {})

def map(request):
    return render(request, 'track/map.html', {})

def list_sightings(request):
    return render(request, 'track/sightings.html', {})

def update_sighting(request,):
    return render(request, 'track/update.html', {})

def create_sighting(request):
    return render(request, 'track/add.html', {})

def obtain_stats(request):
    squirrels = Sighting.objects.all()
    total = len(squirrels)
    avg_hectare_squirrel_num = squirrels.aggregate(Avg('Hectare Squirrel Number')).values()[0] 

    content = {'total number of squrrels':total,
               'average number of squirrels per hectare':avg_hectare_squirrel_num,
            }
    return render(request, 'track/stats.html', content)
