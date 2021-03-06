# Generated by Django 3.0.8 on 2020-07-20 14:50

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('internal_reference_id', models.CharField(blank=True, max_length=255, null=True)),
                ('public_access', models.CharField(blank=True, choices=[('View', 'View'), ('Edit', 'Edit'), ('None', 'None')], default='View', max_length=16)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('uri', models.TextField(blank=True, null=True)),
                ('mnemonic', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(regex=re.compile('^[a-zA-Z0-9\\-\\.\\_\\@]+$'))])),
                ('version', models.CharField(max_length=255)),
                ('released', models.NullBooleanField(default=False)),
                ('retired', models.BooleanField(default=False)),
                ('is_latest_version', models.BooleanField(default=True)),
                ('name', models.TextField()),
                ('full_name', models.TextField(blank=True, null=True)),
                ('default_locale', models.TextField(blank=True, default='en')),
                ('supported_locales', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, null=True, size=None)),
                ('website', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('external_id', models.TextField(blank=True, null=True)),
                ('custom_validation_schema', models.TextField(blank=True, null=True)),
                ('active_concepts', models.IntegerField(default=0)),
                ('active_mappings', models.IntegerField(default=0)),
                ('last_concept_update', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('last_mapping_update', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('last_child_update', models.DateTimeField(default=django.utils.timezone.now)),
                ('source_type', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'sources',
            },
        ),
    ]
