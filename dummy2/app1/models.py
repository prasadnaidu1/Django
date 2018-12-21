from django.db import models

class student(models.Model):
    id=models.IntegerField(default=3,primary_key=True)
    username = models.IntegerField(default=500)
    password = models.IntegerField(default=50)
    cno=models.IntegerField(default=10)
    email=models.EmailField(max_length=49)
    course=models.CharField(max_length=500)
class faculity(models.Model):
    id=models.IntegerField(default=10,primary_key=True)
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    cno=models.IntegerField(default=10)
    exp=models.DecimalField(max_digits=3,decimal_places=1)
    course=models.CharField(max_length=50)
    password=models.IntegerField(default=10)





