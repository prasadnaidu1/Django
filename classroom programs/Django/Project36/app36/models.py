from django.db import models

class Student(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Contact  = models.IntegerField()
    Email = models.EmailField(max_length=100,primary_key=True)
    Password = models.CharField(max_length=50)