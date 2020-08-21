# Generated by Django 3.0.9 on 2020-08-21 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concepts', '0004_auto_20200722_0846'),
        ('mappings', '0005_auto_20200722_0846'),
        ('collections', '0007_auto_20200729_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='concepts',
            field=models.ManyToManyField(blank=True, related_name='collections', to='concepts.Concept'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='mappings',
            field=models.ManyToManyField(blank=True, related_name='collections', to='mappings.Mapping'),
        ),
    ]
