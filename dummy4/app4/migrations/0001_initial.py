# Generated by Django 2.1.1 on 2018-10-15 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='faculity',
            fields=[
                ('id', models.IntegerField(default=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('cno', models.IntegerField(default=10)),
                ('exp', models.DecimalField(decimal_places=1, max_digits=3)),
                ('course', models.CharField(max_length=50)),
                ('password', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.IntegerField(default=3, primary_key=True, serialize=False)),
                ('username', models.IntegerField(default=500)),
                ('password', models.IntegerField(default=50)),
                ('cno', models.IntegerField(default=10)),
                ('email', models.EmailField(max_length=49)),
                ('course', models.CharField(max_length=500)),
            ],
        ),
    ]
