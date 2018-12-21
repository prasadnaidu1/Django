from django.db import models

class product(models.Model):

    no =models.IntegerField(default=5,primary_key=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    qty = models.IntegerField(default=3)
