import csv

from django.http import HttpResponse

from .models import SquirrelDetail

def export(request):

    squirrels = SquirrelDetail.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Squirrel_Database.csv"'

    writer = csv.writer(response)
    writer.writerow(['latitude', 'longitude', 'unique_squirrel_id', 'shift', 'date', 'age', 'primary_fur_color', 'location', 'specific_location', 'running', 'chasing', 'climbing', 
        'eating', 'foraging', 'other_activities', 'kuks', 'quaas', 'moans', 'tail_flags', 'tail_twitches', 'approaches', 'indifferent', 'runs_from'])

    for squirrel in squirrels:
        writer.writerow([squirrel.latitude, squirrel.longitude, squirrel.unique_squirrel_id, squirrel.shift, squirrel.date, squirrel.age, squirrel.primary_fur_color, squirrel.location,
        squirrel.specific_location, squirrel.running, squirrel.chasing, squirrel.climbing, squirrel.eating, squirrel.foraging, squirrel.other_activities, squirrel.kuks, squirrel.quaas,
        squirrel.moans, squirrel.tail_flags, squirrel.tail_twitches, squirrel.approaches, squirrel.indifferent, squirrel.runs_from])

    return response
