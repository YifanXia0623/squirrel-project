from django.db import models
from django.utils.translation import gettext as _

class SquirrelDetail(models.Model):
    Latitude = models.DecimalField(
        max_digits = 100,
        decimal_places = 20,
        help_text=_('Name of Squirrel'),
    )    


    Longtitude = models.DecimalField(
        max_digits = 100,
        decimal_places = 20
        help_text=_('Name of Squirrel'),
    )


    Unique_Squirrel_ID = models.CharField(
        max_length=15,
        help_text=_('Unique ID of Squirrel'),
    )


    Age = models.CharField(
        max_length=15,
        help_text=_('Age of Squirrel'),
    )


    AM = 'AM'
    PM = 'PM'


    SHIFT_CHOICES = [
        (AM,_('AM'),
         PM,_('PM')),        
    ]


    shift = models.CharField(
        max_length=5,
        help_text=_('Shift of Sighting'),
        chioces = SHIFT_CHOIcES
        default = AM,
    )       


    date = models.DateField(
        help_text = _('Date of Sighting'),        
    )

    
    Squirrel_Image = mdoels.ImageField(
        help_text = _('Image of Squirrel'),
        blank = True,
        upload_to = 'Profiles_Images'
    )

