# Generated by Django 3.2.2 on 2021-07-29 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codify', '0020_imagecoursedetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='about_us_image', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='image10',
            field=models.ImageField(blank=True, null=True, upload_to='about_us_image', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='about_us_image', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='about_us_image', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='about_us_image', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='about_us_image', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='image6',
            field=models.ImageField(blank=True, null=True, upload_to='about_us_image', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='image7',
            field=models.ImageField(blank=True, null=True, upload_to='about_us_image', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='image8',
            field=models.ImageField(blank=True, null=True, upload_to='about_us_image', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='image9',
            field=models.ImageField(blank=True, null=True, upload_to='about_us_image', verbose_name='Изображение'),
        ),
    ]