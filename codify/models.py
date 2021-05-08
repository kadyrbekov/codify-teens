from django.db import models

# Create your models here.
class AboutUs(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to="about_us_image", null=True, blank=True, verbose_name="about us picture")

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'O нас'
       
    def __str__(self):
        return self.name

class Advantages(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to="advantages", null=True, blank=True, verbose_name="advantages")

    class Meta:
        verbose_name = 'Наши преимущества'
        verbose_name_plural = 'Наши преимущества'
       
    def __str__(self):
        return self.name

