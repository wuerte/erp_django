from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=50)
    nip = models.CharField(max_length=50)
