# Generated by Django 3.0.7 on 2021-01-06 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodorder', '0014_auto_20210106_1708'),
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
