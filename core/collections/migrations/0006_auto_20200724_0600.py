# Generated by Django 3.0.8 on 2020-07-24 06:00

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections', '0005_collection__background_process_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='_background_process_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, null=True, size=None),
        ),
    ]