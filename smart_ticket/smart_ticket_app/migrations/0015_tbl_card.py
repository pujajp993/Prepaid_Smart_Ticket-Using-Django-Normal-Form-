# Generated by Django 5.0.3 on 2024-03-30 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_ticket_app', '0014_tbl_bank_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(max_length=25, verbose_name='Card Type')),
                ('card_prize', models.IntegerField()),
            ],
        ),
    ]