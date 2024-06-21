from django.db import models


class Users(models.Model):
    user_id = models.BigIntegerField()
    username = models.CharField(max_length=32)
