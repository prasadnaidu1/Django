# Generated by Django 2.1.1 on 2018-10-15 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_faculity'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculity',
            name='id',
            field=models.IntegerField(default=10, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='faculity',
            name='password',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='faculity',
            name='cno',
            field=models.IntegerField(default=10),
        ),
    ]
