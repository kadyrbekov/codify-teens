from django.contrib import admin
from .models import *

# Register your models here.
class AboutusAdmin(admin.ModelAdmin):
    class Meta:
        model = AboutUs

class CourseAdmin(admin.ModelAdmin):
    class Meta:
        model = Course
    

models = [AboutUs, Advantages, Course, Contact, Application, Feedback, Mentor, Event, CategoryEvent, FAQ]
admin.site.register(models)


