from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=50)
    cno=models.IntegerField(default=10,primary_key=True)
    desig=models.CharField(max_length=50)
    salary=models.DecimalField(max_digits=10,decimal_places=2)
