# Generated by Django 4.2.14 on 2024-07-29 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a_int', '0005_alter_item_color_alter_item_f1_alter_item_f2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('account', models.IntegerField(unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='CommissionAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('account', models.IntegerField(unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='MainAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('account', models.IntegerField(unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='item_id',
            field=models.CharField(editable=False, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(editable=False, max_length=200, unique=True),
        ),
        migrations.CreateModel(
            name='MainTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transc_id', models.CharField(editable=False, max_length=100, unique=True)),
                ('business_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('number', models.IntegerField(unique=True)),
                ('ref_code', models.CharField(max_length=50)),
                ('item_id', models.CharField(max_length=1000000)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('commission', models.DecimalField(decimal_places=2, default=2, max_digits=8)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=8)),
                ('debit', models.DecimalField(decimal_places=2, max_digits=8)),
                ('is_credited', models.BooleanField(default=False)),
                ('is_success', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a_int.mainaccount')),
            ],
        ),
        migrations.CreateModel(
            name='CommissionTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transc_id', models.CharField(editable=False, max_length=100, unique=True)),
                ('business_id', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('commission', models.DecimalField(decimal_places=2, max_digits=8)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=8)),
                ('debit', models.DecimalField(decimal_places=2, max_digits=8)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a_int.commissionaccount')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transc_id', models.CharField(editable=False, max_length=100, unique=True)),
                ('business_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('number', models.IntegerField(unique=True)),
                ('ref_code', models.CharField(max_length=50)),
                ('item_id', models.CharField(max_length=1000000)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('commission', models.DecimalField(decimal_places=2, max_digits=8)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=8)),
                ('debit', models.DecimalField(decimal_places=2, max_digits=8)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a_int.businessaccount')),
            ],
        ),
    ]
