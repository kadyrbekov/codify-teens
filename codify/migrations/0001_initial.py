# Generated by Django 3.2.2 on 2021-05-08 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='about_us_image', verbose_name='about us picture')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'O нас',
            },
        ),
    ]
