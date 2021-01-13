# Generated by Django 3.0.7 on 2020-12-28 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodorder', '0009_auto_20201228_0245'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='veg',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodorder.Product'),
        ),
    ]
