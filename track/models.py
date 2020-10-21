from django.db import models
from django.contrib.gis.db  import models as geomodels
from django.utils.translation import gettext as _

class Sighting(models.Model):
    latitude = models.FloatField(
            help_text=_('Latitude of sighting'),
    )

    longitude = models.FloatField(
            help_text=_('Longitude of sighting'),
    )

    unique_squirrel_id = models.CharField(
        max_length=14,
        help_text=_('Unique Squirrel ID'),
    )

    geometry = geomodels.PointField()

    class Meta:
        verbose_name_plural = 'sightings'
    
