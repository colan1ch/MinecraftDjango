from django.db import models


# Create your models here.

class Page_proj(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=511)
    online = models.IntegerField()
    url = models.CharField(max_length=15)
    img = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=100)