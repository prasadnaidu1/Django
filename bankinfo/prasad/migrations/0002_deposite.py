# Generated by Django 2.1.1 on 2018-10-18 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prasad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='deposite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A_no', models.IntegerField(default=10)),
                ('A_name', models.CharField(max_length=50)),
                ('A_money', models.IntegerField(default=10)),
                ('A_date', models.DateField()),
                ('A_type', models.CharField(max_length=20)),
            ],
        ),
    ]
