from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Max, Min, Count, Avg
from .models import Sighting
from .forms import SightingForm
from django.views.generic.edit import CreateView, DeleteView



def map(request):
    sighting = Sighting.objects.all()[:100]
    context = {'sighting': sighting}
    return render(request, 'track/map.html',context)


#unique id
def update_sighting(request,unique_squirrel_id):
    squirrel = get_object_or_404(Sighting, unique_squirrel_id=unique_squirrel_id)
    form = SightingForm(request.POST or None, instance=squirrel)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('track:list_sightings'))
    return render(request, 'track/update.html', {'form':form})


#add
def create_sighting(request):
    squirrel = Sighting()
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            squirrel = form.save()
            return HttpResponseRedirect(reverse('track:list_sightings'))
    else:
        form = SightingForm()        
    return render(request, 'track/add.html', {'form': form,'squirrel':squirrel})


#stats
def obtain_stats(request):
    squirrels = Sighting.objects.all()
    total = len(squirrels)
    avg_hectare_squirrel_num = squirrels.aggregate(Avg('Hectare Squirrel Number')).values()[0] 
    num_juve = len(squirrels.filter(age='Juvenile'))
    num_adult = len(squirrels.filter(age='Adult'))
    fur_color = squirrels.values_list('Primary Fur Color').annotate(fur_count=Count('Primary Fur Color')).order_by('-fur_count')
    context = {'total number of squrrels':total,
               'average number of squirrels per hectare':avg_hectare_squirrel_num,
               'total number of juvenile':num_juve,
               'total number of adult':num_adult,
               'most common fur color':fur_color,
               }
    return render(request, 'track/stats.html', context)

#sightings
def list_sightings(request):
    sighting = Sighting.objects.all()
    context = {
            'sighting': sighting,
    }
    return render(request, 'track/sighting.html', context)

def index(request):
    return HttpResponse("Index Page")
