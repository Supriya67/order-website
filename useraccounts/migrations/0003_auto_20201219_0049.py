# Generated by Django 3.0.7 on 2020-12-18 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0002_auto_20201218_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone2',
            field=models.CharField(max_length=100),
        ),
    ]