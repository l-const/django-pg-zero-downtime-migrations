# Generated by Django 3.0a1 on 2019-10-14 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('good_flow_app', '0040_add_gist_index_with_condition'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='testtable',
            name='test_index',
        ),
    ]