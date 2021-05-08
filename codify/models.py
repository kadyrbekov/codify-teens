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

class CourseCategory(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name = 'Категории курсов'
        verbose_name_plural = 'Категории курсов'

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=False)
    duration = models.IntegerField(default=0, choices=(
    
            (1, '1 месяц'),
            (2, '2 месяц'),
            (3, '3 месяц'),
            (4, '4 месяц'),
            (5, '5 месяц'),
            (6, '6 месяц'),
        ))
    price = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name
    
    
    
    
    
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'