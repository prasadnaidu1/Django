# Generated by Django 2.1.1 on 2018-10-15 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20181015_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='faculity',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('cno', models.IntegerField(default=10, primary_key=True, serialize=False)),
                ('exp', models.DecimalField(decimal_places=1, max_digits=3)),
                ('course', models.CharField(max_length=50)),
            ],
        ),
    ]
