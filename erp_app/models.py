from django.db import models

#TODO models to add: UoM, product_categ, currency

class Company(models.Model):
    name = models.CharField(max_length=50)
    nip = models.CharField(max_length=50)
    mail = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=14, null=True, blank=True) #TODO validacja
    #TODO currency field
    
class Product(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.FloatField(default=0.0, null=True, blank=True)
    #TODO on_stock_qty field, uom field and uom model, category model and category field, currency field


    def __str__(self):
        return self.name