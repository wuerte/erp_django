from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=50)
    nip = models.CharField(max_length=50)
    
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name