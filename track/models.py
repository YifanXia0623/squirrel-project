from django.db import models
from django.utils.translation import gettext as _

class Sighting(models.Model):
    latitude = models.FloatField(
        help_text=_('Latitude of Squirrel'),
    )    


    Longitude = models.FloatField(
        help_text=_('Longitude of Squirrel'),
    )


    unique_squirrel_id = models.CharField(
        max_length=15,
        help_text=_('Unique ID of Squirrel'),
        unique = True,
    )


    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = [
        (AM, _('AM')),
        (PM, _('PM')),
    ]


    Shift = models.CharField(
        max_length=5,
        help_text=_('Shift of Sighting(AM or PM)'),
        choices = SHIFT_CHOICES,
    )  

    Adult = 'Adult'
    Juvenile = 'Juvenile'
    Unknown = '?'

    AGE_CHOICES = [
        (Adult, 'Adult'),
        (Juvenile, 'Juvenile'),
        (Unknown, '?'),
    ]

    Age = models.CharField(
        max_length=15,
        help_text=_('Age of Squirrel'),
        choices = AGE_CHOICES,
        blank = True,
     )       


    Date = models.DateField(
        help_text = _('Date of Sighting'),        
    )


    def __str__(self):
        return self.Unique_Squirrel_ID
    
    

