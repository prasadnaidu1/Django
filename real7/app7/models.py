from django.db import models
from django.db import models
class employee(models.Model):
    id=models.IntegerField(default=5,primary_key=True)
    name = models.CharField(max_length=40)
    cno = models.IntegerField(default=10)
    sal=models.DecimalField(max_digits=10,decimal_places=2)
