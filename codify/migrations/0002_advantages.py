# Generated by Django 3.2.2 on 2021-05-08 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codify', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='advantages', verbose_name='advantages')),
            ],
            options={
                'verbose_name': 'Наши преимущества',
                'verbose_name_plural': 'Наши преимущества',
            },
        ),
    ]
