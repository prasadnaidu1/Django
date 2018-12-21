from django.db import models

class Employee(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Contact = models.IntegerField(primary_key=True)
    Salary = models.DecimalField(max_digits=10,decimal_places=2)

