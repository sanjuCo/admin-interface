# Generated by Django 4.2.14 on 2024-07-29 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_int', '0006_businessaccount_commissionaccount_mainaccount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesstransactions',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='commissiontransactions',
            name='commission',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=8),
        ),
    ]
