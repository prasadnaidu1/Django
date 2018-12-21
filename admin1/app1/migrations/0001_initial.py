# Generated by Django 2.1.1 on 2018-10-12 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(default=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=30)),
                ('fee', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Faculity',
            fields=[
                ('id', models.IntegerField(default=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('exp', models.DecimalField(decimal_places=1, max_digits=4)),
                ('contact', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='NewCourse',
            fields=[
                ('cid', models.IntegerField(default=4, primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=50)),
                ('duration', models.IntegerField(default=3)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
            ],
        ),
    ]
