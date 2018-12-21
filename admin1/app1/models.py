from django.db import models

class Course(models.Model):
    id=models.IntegerField(default=2,primary_key=True)
    name=models.CharField(max_length=50)
    course=models.CharField(max_length=30)
    fee=models.IntegerField(default=5)
class Faculity(models.Model):
    id=models.IntegerField(default=4,primary_key=True)
    name=models.CharField(max_length=50)
    exp=models.DecimalField(max_digits=4,decimal_places=1)
    contact=models.IntegerField(default=10)
class NewCourse(models.Model):
    cid=models.IntegerField(default=4,primary_key=True)
    cname=models.CharField(max_length=50)
    duration=models.IntegerField(default=3)
    time=models.TimeField()
    date=models.DateField()


