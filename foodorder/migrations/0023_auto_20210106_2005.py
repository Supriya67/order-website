# Generated by Django 3.0.7 on 2021-01-06 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodorder', '0022_auto_20210106_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='non_veg',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodorder.Product'),
        ),
    ]
