from django.db import models
from django.contrib.auth import get_user_model


class Servers(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    docker_id = models.CharField(max_length=64)


class UserSettings(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)