# Generated by Django 3.0.7 on 2021-01-06 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodorder', '0013_auto_20210106_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodorder.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='bestseller',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='offerzone',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='BestSeller',
        ),
        migrations.DeleteModel(
            name='OfferZone',
        ),
    ]