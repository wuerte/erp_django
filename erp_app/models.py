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
    cost = models.FloatField(default=0.0, null=True, blank=True)
    weight = models.FloatField(default=0.0, null=True, blank=True)
    on_hand_qty = models.FloatField(default=0.0, null=True, blank=True)
    #product_categ
    #TODO on_stock_qty field, uom field and uom model, category model and category field, currency field


    def __str__(self):
        return self.name
    
    @staticmethod
    def get_stock_valuation_list() -> list:
        stock_valuation = []     
        products = Product.objects.all()
        for product in products:
            cost = 0.0 if product.cost == None else product.cost
            qty = 0.0 if product.on_hand_qty == None else product.on_hand_qty
            valuation = cost * qty
            dict = {
                'name': product.name,
                'quantity': product.on_hand_qty,
                'cost': product.cost,
                'valuation': valuation,
            }
            stock_valuation.append(dict)
        return sorted(stock_valuation, key=lambda d: d['valuation'], reverse=True)  