from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    name = models.CharField(
            max_length=100,
            help_text=_('Name of Squirrel'),
    )

    
