# Generated by Django 3.2.2 on 2021-07-29 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codify', '0009_auto_20210729_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='course',
        ),
    ]