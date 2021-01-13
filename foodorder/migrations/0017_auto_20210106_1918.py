# Generated by Django 3.0.7 on 2021-01-06 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodorder', '0016_auto_20210106_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='best_seller',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='offer_zone',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodorder.Product'),
        ),
    ]
