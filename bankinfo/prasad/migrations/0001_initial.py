# Generated by Django 2.1.1 on 2018-10-18 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('cno', models.IntegerField(default=10, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
