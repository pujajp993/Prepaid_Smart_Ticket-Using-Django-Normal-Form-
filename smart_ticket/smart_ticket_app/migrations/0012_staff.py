# Generated by Django 5.0.3 on 2024-03-29 14:29

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_ticket_app', '0011_tbl_fare'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Status', models.IntegerField(verbose_name='Status')),
                ('Staff_id', models.IntegerField(verbose_name='Staff Id')),
            ],
            options={
                'db_table': 'tbl_staff',
            },
            bases=('smart_ticket_app.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]