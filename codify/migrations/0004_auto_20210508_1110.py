# Generated by Django 3.2.2 on 2021-05-08 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codify', '0003_course_coursecategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.IntegerField(choices=[(1, '1 месяц'), (2, '2 месяц'), (3, '3 месяц'), (4, '4 месяц'), (5, '5 месяц'), (6, '6 месяц')], default=0),
        ),
    ]