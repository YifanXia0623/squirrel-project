from django.forms import ModelForm
from .models import Sighting 


class SightingForm(ModelForm):
    class Meta:
        model = Sighting
        fields = [
            'latitude',
            'Longitude',
            'Unique_Squirrel_ID',
            'Shift',
            'Age',
            'Date',
        ]
