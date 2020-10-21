from django.forms import ModelForm
from .models import SquirrelDetail 


class SightingForm(ModelForm):
    class Meta:
        model = SquirrelDetail
        fields = [
            'Latitude',
            'Longitude',
            'Unique_Squirrel_ID',
            'Age'
            'Shift',
            'Date',
            'Squirrel_Image'
        ]
