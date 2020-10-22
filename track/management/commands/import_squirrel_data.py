import csv

from django.core.management.base import BaseCommand

from track.models import Sighting

class Command(BaseCommand):
    help = 'Import squirrel data from 2018 census file'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_census_data', help='file containing squirrel details')

    def handle(self, *args, **options):
        file_ = options['squirrel_census_data']

        with open(file_) as fp:
            reader = csv.DictReader(fp)

            for item in reader:
                obj = Sighting() 
                obj.latitude = item['Latitude']
                obj.longitude = item['Longitude']
                obj.unique_squirrel_id = item['Unique Squirrel ID']
                obj.shift = item['Shift']
                obj.date = item['Date']
                obj.age = item['Age']

                try:
                    obj.save()
                except:
                    continue



        msg = f'You are importing from {file_}'
        self.stdout.write(self.style.SUCCESS(msg))
