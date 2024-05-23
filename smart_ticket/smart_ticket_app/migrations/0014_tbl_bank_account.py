# Generated by Django 5.0.3 on 2024-03-30 07:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_ticket_app', '0013_tbl_bank_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_bank_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holder_name', models.CharField(max_length=30, verbose_name='Card Holder name in card')),
                ('bank_name', models.CharField(max_length=25, verbose_name='Bank Name')),
                ('account_number', models.CharField(max_length=25, verbose_name='Bank Account No')),
                ('cvv', models.IntegerField(verbose_name='CVV')),
                ('month', models.CharField(max_length=10, verbose_name='Card Expiry mont')),
                ('year', models.IntegerField(verbose_name='yaer of Expiry')),
                ('amount', models.IntegerField(verbose_name='Cash in bank')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]