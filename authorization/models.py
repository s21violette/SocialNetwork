from django.db import models


class Users(models.Model):
    login = models.CharField(unique=True)
    password = models.CharField()
