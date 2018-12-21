from django.db import models
class course(models.Model):
    id=models.IntegerField(default=3,primary_key=True)
    name=models.CharField(max_length=50)
    duration=models.IntegerField(default=3)
    fee=models.IntegerField(default=5)
class student(models.Model):
    Id=models.IntegerField(default=3, primary_key=True)
    Name=models.CharField(max_length=40)
    Contact=models.IntegerField(default=10)
    Email=models.EmailField(max_length=50)
    Password=models.IntegerField(default=20)