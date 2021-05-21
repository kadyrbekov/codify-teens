from rest_framework import serializers
from .models import *

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ('id', 'name', 'description', )

class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = ('id', 'name', 'description', 'name')
#
class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ('id', 'name',)
#
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'duration', 'price')
#
#
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ('',)

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        exclude = ('',)
#
#
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        exclude = ('',)


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        exclude = ('',)


class CategoryEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryEvent
        fields = ('id', 'name',)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ('',)


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        exclude = ('',)