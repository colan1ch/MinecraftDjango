from django.db import models
from django.contrib.auth import get_user_model


class Servers():
    name = models.CharField(max_length=100)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    docker_id = models.CharField(max_length=64)
class User_settings():
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)