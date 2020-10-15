import csv

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Export data on squirrel sighting in CSV format'

    def add_arguments(self, parser):
        parser.add_argument('outfile',
                            nargs=1,
                            type=str,
                            help='Save path, like </path/to/outfile.csv> or "/data/squirrel_data.csv"')

    def handle(self, *args, **options):

        squirrels = SquirrelDetail.objects.all()

        writer = csv.writer(open(options['outfile'][0], 'w'), quoting=csv.QUOTE_ALL, delimiter=',')
        writer.writerow(['latitude', 'longitude', 'unique_squirrel_id', 'shift', 'date', 'age', 'primary_fur_color', 'location', 'specific_location', 'running', 'chasing', 'climbing', 
        'eating', 'foraging', 'other_activities', 'kuks', 'quaas', 'moans', 'tail_flags', 'tail_twitches', 'approaches', 'indifferent', 'runs_from'])

        for squirrel in squirrels:
            writer.writerow([squirrel.latitude, squirrel.longitude, squirrel.unique_squirrel_id, squirrel.shift, squirrel.date, squirrel.age, squirrel.primary_fur_color, squirrel.location,
            squirrel.specific_location, squirrel.running, squirrel.chasing, squirrel.climbing, squirrel.eating, squirrel.foraging, squirrel.other_activities, squirrel.kuks, squirrel.quaas,
            squirrel.moans, squirrel.tail_flags, squirrel.tail_twitches, squirrel.approaches, squirrel.indifferent, squirrel.runs_from])

        return response



         msg = f'You are exporting squirrel database to {outfile}'

         self.stdout.write(self.style.SUCCESS(msg))
