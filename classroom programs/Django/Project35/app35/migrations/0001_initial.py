# Generated by Django 2.0.7 on 2018-11-02 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactsInfo',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('cno', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
