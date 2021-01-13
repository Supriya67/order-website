# Generated by Django 3.0.7 on 2021-01-06 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodorder', '0017_auto_20210106_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='bestseller',
        ),
        migrations.RemoveField(
            model_name='product',
            name='offerzone',
        ),
        migrations.AlterField(
            model_name='orders',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodorder.Product'),
        ),
    ]
