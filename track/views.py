from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Max, Min, Count, Avg
from .models import Sighting
from .forms import SightingForm



def map(request):
    return render(request, 'track/map.html', {})


#unique id
def update_sighting(request,):
    return render(request, 'track/update.html', {})


#add
def create_sighting(request):
    
    return render(request, 'track/add.html', {})


#stats
def obtain_stats(request):
    squirrels = Sighting.objects.all()
    total = len(squirrels)
    avg_hectare_squirrel_num = squirrels.aggregate(Avg('Hectare Squirrel Number')).values()[0] 
    num_juve = len(squirrels.filter(age='Juvenile'))
    num_adult = len(squirrels.filter(age='Adult'))
    fur_color = squirrels.values_list('values_list('Primary Fur Color').annotate(fur_count=Count('Primary Fur Color')).order_by('-fur_count')')[0]
    content = {'total number of squrrels':total,
               'average number of squirrels per hectare':avg_hectare_squirrel_num,
               'total number of juvenile':num_juve,
               'total number of adult':num_adult,
               'most common fur color':fur_color,
               }
    return render(request, 'track/stats.html', content)

#sightings
def list_sightings(request):
    sighting = Sighting.objects.all()
    context = {
            'sighting': sighting,
    }
    return render(request, 'track/index.html', context)

def index(request):
    return HttpResponse("Index Page")
