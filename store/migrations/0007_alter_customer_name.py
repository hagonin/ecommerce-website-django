# Generated by Django 4.0.6 on 2022-07-15 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_state_shippingaddress_county'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
