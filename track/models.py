from django.db import models
from django.utils.translation import gettext as _

class Sighting(models.Model):
    Latitude = models.DecimalField(
        max_digits = 100,
        decimal_places = 20,
        help_text=_('Latitude of Squirrel'),
    )    


    Longtitude = models.DecimalField(
        max_digits = 100,
        decimal_places = 20,
        help_text=_('Longitude of Squirrel'),
    )


    Unique_Squirrel_ID = models.CharField(
        max_length=15,
        help_text=_('Unique ID of Squirrel'),
    )

    JUVENILE = 'Juvenile'
    ADULT = 'Adult'

    
    AGE_CHOICES = [
        (JUVENILE, _('Juvenile')),
        (ADULT, _('Adult')),
    ]

    Age = models.CharField(
        max_length=15,
        help_text=_('Age of Squirrel'),
        choices=AGE_CHOICES,
        default=ADULT,
    )


    AM = 'AM'
    PM = 'PM'


    SHIFT_CHOICES = [
        (AM, _('AM')),
        (PM, _('PM')),        
    ]


    Shift = models.CharField(
        max_length=5,
        help_text=_('Shift of Sighting'),
        choices = SHIFT_CHOICES,
        default = AM,
    )       


    Date = models.DateField(
        help_text = _('Date of Sighting'),        
    )


    Squirrel_Image = models.ImageField(
        help_text = _('Image of Squirrel'),
        blank = True,
        upload_to = 'Profiles_Images'
    )


    
    

