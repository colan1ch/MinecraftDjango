from django.db import models
from django.contrib.auth import get_user_model


class Server(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    plan = models.CharField(max_length=10)
    settings = models.JSONField(default=None)
    docker_id = models.CharField(max_length=64)


class UserSettings(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
