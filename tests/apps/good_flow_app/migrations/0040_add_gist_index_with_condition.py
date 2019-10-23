# Generated by Django 3.0a1 on 2019-10-14 19:47

import django.contrib.postgres.indexes
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good_flow_app', '0039_drop_gist_index'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='testtable',
            index=django.contrib.postgres.indexes.GistIndex(
                condition=models.Q(test_field_tsv__isnull=False),
                fields=['test_field_tsv'],
                name='test_index',
            ),
        ),
    ]
