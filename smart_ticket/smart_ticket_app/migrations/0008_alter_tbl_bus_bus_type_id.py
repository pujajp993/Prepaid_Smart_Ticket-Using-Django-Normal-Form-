# Generated by Django 5.0.3 on 2024-03-28 08:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_ticket_app', '0007_alter_tbl_bus_bus_type_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_bus',
            name='bus_type_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smart_ticket_app.tbl_bustype'),
        ),
    ]