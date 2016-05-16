from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Create your models here.
class Controls(models.Model):
    x_direction = models.FloatField()
    y_direction = models.FloatField()