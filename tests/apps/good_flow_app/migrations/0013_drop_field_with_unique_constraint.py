# Generated by Django 3.1 on 2019-09-22 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('good_flow_app', '0012_add_field_with_unique_constraint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testtable',
            name='field',
        ),
    ]