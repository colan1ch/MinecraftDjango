from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=511)
    online = models.IntegerField()
    address = models.CharField(max_length=15)
