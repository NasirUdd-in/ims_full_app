# Generated by Django 3.0.8 on 2023-07-19 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='commission',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
