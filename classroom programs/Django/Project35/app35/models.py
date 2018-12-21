from django.db import models


class ContactsInfo(models.Model):
    name = models.CharField(max_length=50)
    cno = models.IntegerField(primary_key=True)