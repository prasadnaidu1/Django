from django.db import models


class friends(models.Model):
    entry=models.IntegerField(default=10,primary_key=True)
    date=models.DateField()
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    members=models.CharField(max_length=50)
    res=models.IntegerField(default=10)


