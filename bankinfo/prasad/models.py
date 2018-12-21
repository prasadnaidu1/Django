from django.db import models

# Create your models here.
class account(models.Model):
    name=models.CharField(max_length=50)
    cno=models.IntegerField(default=10,primary_key=True)
    email=models.EmailField()
    address=models.CharField(max_length=100)
class deposite(models.Model):
    D_no=models.IntegerField(default=10,primary_key=True)
    D_name=models.CharField(max_length=45)
    D_money=models.IntegerField(default=10)
    A_date=models.DateField()
    A_type=models.CharField(max_length=20)
class withdraw(models.Model):
    w_no=models.IntegerField(default=10)
    w_name=models.CharField(max_length=50)
    w_money=models.IntegerField(default=10)
    A_date=models.DateField()
    A_type=models.CharField(max_length=20)
