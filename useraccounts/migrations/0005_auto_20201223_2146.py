# Generated by Django 3.0.7 on 2020-12-23 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0004_auto_20201222_2243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='password1',
            new_name='password',
        ),
    ]
