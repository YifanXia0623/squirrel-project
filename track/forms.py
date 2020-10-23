from django.forms import ModelForm
from .models import Sighting 


class SightingForm(ModelForm):
    class Meta:
        model = Sighting
        fields = [
            'latitude',
            'Longitude',
            'unique_squirrel_id',
            'Shift',
            'Age',
            'Date',
        ]
