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

    def __str__(self):
        return self.name

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


class Contact(models.Model):
    name = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20)
    instagram = models.CharField(max_length=55)
    twitter = models.CharField(max_length=55)
    facebook = models.CharField(max_length=55)


    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.phone_number



class Mentor(models.Model):
    specialty = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="mentor", null=True, blank=True, verbose_name="mentor")
    course = models.ForeignKey(
        to=Course,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ментора'
        verbose_name_plural = 'Менторы'



class Application(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField(null=False)
    mail = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.phone_number

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="feedback", null=True, blank=True, verbose_name="feedback")
    message = models.TextField(null=False)
    mail = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name

class CategoryEvent(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Категория мероприятия'
        verbose_name_plural = 'Категория Мероприятий'

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=False)
    category = models.ForeignKey(
        to=CategoryEvent,
        null=True,
        blank=True,
        on_delete=models.CASCADE,

    )
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to="event", null=True, blank=True, verbose_name="event")

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = "Мероприятия"

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.TextField(null=True)
    answer = models.TextField(null=True)


    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'

    def __str__(self):
        return self.question