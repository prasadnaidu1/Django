# Generated by Django 2.1.2 on 2018-10-10 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.IntegerField(default=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('cno', models.IntegerField(default=10)),
            ],
        ),
    ]
