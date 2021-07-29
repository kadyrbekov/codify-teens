from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *

# Create your views here.

class AboutUsListView(APIView,):

    def get(self, request, *args, **kwargs):
        about = AboutUs.objects.all()
        serializer = AboutUsSerializer(about, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = AboutUsSerializer(data=request.POST)
        if serializer.is_valid():
            about_object = serializer.save()
            json_serializer = AboutUsSerializer(instance=about_object)
            return Response(data=json_serializer.data, status=201)
        return Response(data=serializer.errors)

class AboutUsDetailView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            about_us = AboutUs.objects.get(pk=kwargs.get('pk'))
        except AboutUs.DoesNotExist as e:
            return Response(data={"message": f'AboutUs was not found: {e}'}, status=404)

        serializer = AboutUsSerializer(instance=about_us)
        return Response(data=serializer.data)

    def put(self, request, *args, **kwargs):
        about_us = AboutUs.objects.get(pk=kwargs.get('pk'))
        serializer = AboutUsSerializer(instance=about_us, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


    def delete(self, request, *args, **kwargs):
        about_us = AboutUs.objects.get(pk=kwargs.get('pk'))
        about_us.delete()
        return Response(data={'message': 'Обьект был удален'})

class AdvantagesListView(APIView):

    def get(self, request, *args, **kwargs):
        advantages = Advantages.objects.all()
        serializer = AdvantagesSerializer(advantages, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = AdvantagesSerializer(data=request.POST)
        if serializer.is_valid():
            advantages_object = serializer.save()
            json_serializer = AdvantagesSerializer(instance=advantages_object)
            return Response(data=json_serializer.data, status=201)
        return Response(data=serializer.errors)

class AdvantagesDetailView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            advantages = Advantages.objects.get(pk=kwargs.get('pk'))
        except Advantages.DoesNotExist as e:
            return Response(data={"message": f'Advantages was not found: {e}'}, status=404)

        serializer = AdvantagesSerializer(instance=advantages)
        return Response(data=serializer.data)

    def put(self, request, *args, **kwargs):
        advantages = Advantages.objects.get(pk=kwargs.get('pk'))
        serializer = AdvantagesSerializer(instance=advantages, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


    def delete(self, request, *args, **kwargs):
        advantages = Advantages.objects.get(pk=kwargs.get('pk'))
        advantages.delete()
        return Response(data={'message': 'Обьект был удален'})


class CourseCategoryList(APIView):

    def get(self, request, *args, **kwargs):
        course_category = CourseCategory.objects.all()
        serializer = CourseCategorySerializer(course_category, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CourseCategorySerializer(data=request.POST)
        if serializer.is_valid():
            course_category = serializer.save()
            json_serializer = CourseCategorySerializer(instance=course_category)
            return Response(data=json_serializer.data, status=201)
        return Response(data=serializer.errors)

class CourseCategoryDetail(APIView):

    def get(self, request, *args, **kwargs):
        try:
            course_category = CourseCategory.objects.get(pk=kwargs.get('pk'))
        except CourseCategory.DoesNotExist as e:
            return Response(data={"message": f'AboutUs was not found: {e}'}, status=404)

        serializer = CourseCategorySerializer(instance=course_category)
        return Response(data=serializer.data)

    def put(self, request, *args, **kwargs):
        course_category = CourseCategory.objects.get(pk=kwargs.get('pk'))
        serializer = CourseCategorySerializer(instance=course_category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


    def delete(self, request, *args, **kwargs):
        course_category = CourseCategory.objects.get(pk=kwargs.get('pk'))
        course_category.delete()
        return Response(data={'message': 'Обьект был удален'})

class CourseList(APIView):

    def get(self, request, *args, **kwargs):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CourseSerializer(data=request.POST)
        if serializer.is_valid():
            course = serializer.save()
            json_serializer = CourseSerializer(instance=course)
            return Response(data=json_serializer.data, status=201)
        return Response(data=serializer.errors)

class CourseDetail(APIView):

    def get(self, request, *args, **kwargs):
        try:
            course = Course.objects.get(pk=kwargs.get('pk'))
        except Course.DoesNotExist as e:
            return Response(data={"message": f'Course was not found: {e}'}, status=404)

        serializer = CourseSerializer(instance=course)
        return Response(data=serializer.data)

    def put(self, request, *args, **kwargs):
        course = Course.objects.get(pk=kwargs.get('pk'))
        serializer = CourseSerializer(instance=course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


    def delete(self, request, *args, **kwargs):
        course = Course.objects.get(pk=kwargs.get('pk'))
        course.delete()
        return Response(data={'message': 'Обьект был удален'})


class ContactList(APIView):

    def get(self, request, *args, **kwargs):
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.POST)
        if serializer.is_valid():
            contact = serializer.save()
            json_serializer = ContactSerializer(instance=contact)
            return Response(data=json_serializer.data, status=201)
        return Response(data=serializer.errors)

class ContactDetail(APIView):

    def get(self, request, *args, **kwargs):
        try:
            contact = Contact.objects.get(pk=kwargs.get('pk'))
        except Contact.DoesNotExist as e:
            return Response(data={"message": f'Contact was not found: {e}'}, status=404)

        serializer = ContactSerializer(instance=contact)
        return Response(data=serializer.data)

    def put(self, request, *args, **kwargs):
        contact = Contact.objects.get(pk=kwargs.get('pk'))
        serializer = ContactSerializer(instance=contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


    def delete(self, request, *args, **kwargs):
        contact = Contact.objects.get(pk=kwargs.get('pk'))
        contact.delete()
        return Response(data={'message': 'Обьект был удален'})

class MentorList(APIView):

    def get(self, request, *args, **kwargs):
        mentor = Mentor.objects.all()
        serializer = MentorSerializer(mentor, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = MentorSerializer(data=request.POST)
        if serializer.is_valid():
            mentor = serializer.save()
            json_serializer = MentorSerializer(instance=mentor)
            return Response(data=json_serializer.data, status=201)
        return Response(data=serializer.errors)

class MentorDetail(APIView):

    def get(self, request, *args, **kwargs):
        try:
            mentor = Mentor.objects.get(pk=kwargs.get('pk'))
        except Mentor.DoesNotExist as e:
            return Response(data={"message": f'Mentor was not found: {e}'}, status=404)

        serializer = MentorSerializer(instance=mentor)
        return Response(data=serializer.data)

    def put(self, request, *args, **kwargs):
        mentor = Mentor.objects.get(pk=kwargs.get('pk'))
        serializer = MentorSerializer(instance=mentor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


    def delete(self, request, *args, **kwargs):
        mentor = Mentor.objects.get(pk=kwargs.get('pk'))
        mentor.delete()
        return Response(data={'message': 'Обьект был удален'})


class ApplicationList(APIView):

    def get(self, request, *args, **kwargs):
        application = Application.objects.all()
        serializer = ApplicationSerializer(application, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ApplicationSerializer(data=request.POST)
        if serializer.is_valid():
            application = serializer.save()
            json_serializer = ApplicationSerializer(instance=application)
            return Response(data=json_serializer.data, status=201)
        return Response(data=serializer.errors)

class ApplicationDetail(APIView):

    def get(self, request, *args, **kwargs):
        try:
            application = Application.objects.get(pk=kwargs.get('pk'))
        except Application.DoesNotExist as e:
            return Response(data={"message": f'Application was not found: {e}'}, status=404)

        serializer = ApplicationSerializer(instance=application)
        return Response(data=serializer.data)

    def put(self, request, *args, **kwargs):
        application = Application.objects.get(pk=kwargs.get('pk'))
        serializer = ApplicationSerializer(instance=application, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


    def delete(self, request, *args, **kwargs):
        application = Application.objects.get(pk=kwargs.get('pk'))
        application.delete()
        return Response(data={'message': 'Обьект был удален'})

class FeedbackList(APIView):

    def get(self, request, *args, **kwargs):
        feedback = Feedback.objects.all()
        serializer = FeedbackSerializer(feedback, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = FeedbackSerializer(data=request.POST)
        if serializer.is_valid():
            feedback = serializer.save()
            json_serializer = FeedbackSerializer(instance=feedback)
            return Response(data=json_serializer.data, status=201)
        return Response(data=serializer.errors)

class FeedbackDetail(APIView):

    def get(self, request, *args, **kwargs):
        try:
            feedback = Feedback.objects.get(pk=kwargs.get('pk'))
        except Feedback.DoesNotExist as e:
            return Response(data={"message": f'Feedback was not found: {e}'}, status=404)

        serializer = FeedbackSerializer(instance=feedback)
        return Response(data=serializer.data)

    def put(self, request, *args, **kwargs):
        feedback = Feedback.objects.get(pk=kwargs.get('pk'))
        serializer = FeedbackSerializer(instance=feedback, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


    def delete(self, request, *args, **kwargs):
        feedback = Feedback.objects.get(pk=kwargs.get('pk'))
        feedback.delete()
        return Response(data={'message': 'Обьект был удален'})


class EventList(APIView):

    def get(self, request, *args, **kwargs):
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.POST)
        if serializer.is_valid():
            event = serializer.save()
            json_serializer = EventSerializer(instance=event)
            return Response(data=json_serializer.data, status=201)
        return Response(data=serializer.errors)

class EventDetail(APIView):

    def get(self, request, *args, **kwargs):
        try:
            event = Event.objects.get(pk=kwargs.get('pk'))
        except Event.DoesNotExist as e:
            return Response(data={"message": f'Event was not found: {e}'}, status=404)

        serializer = EventSerializer(instance=event)
        return Response(data=serializer.data)

    def put(self, request, *args, **kwargs):
        event = Event.objects.get(pk=kwargs.get('pk'))
        serializer = EventSerializer(instance=event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


    def delete(self, request, *args, **kwargs):
        event = Event.objects.get(pk=kwargs.get('pk'))
        event.delete()
        return Response(data={'message': 'Обьект был удален'})

class FAQList(APIView):

    def get(self, request, *args, **kwargs):
        faq = FAQ.objects.all()
        serializer = FAQSerializer(faq, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = FAQSerializer(data=request.POST)
        if serializer.is_valid():
            faq = serializer.save()
            json_serializer = FAQSerializer(instance=faq)
            return Response(data=json_serializer.data, status=201)
        return Response(data=serializer.errors)

class FAQDetail(APIView):

    def get(self, request, *args, **kwargs):
        try:
            faq = FAQ.objects.get(pk=kwargs.get('pk'))
        except FAQ.DoesNotExist as e:
            return Response(data={"message": f'FAQ was not found: {e}'}, status=404)

        serializer = FAQCourseSerializer(instance=faq)
        return Response(data=serializer.data)

    def put(self, request, *args, **kwargs):
        faq = FAQ.objects.get(pk=kwargs.get('pk'))
        serializer = FAQCourseSerializer(instance=faq, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


    def delete(self, request, *args, **kwargs):
        faq = FAQ.objects.get(pk=kwargs.get('pk'))
        faq.delete()
        return Response(data={'message': 'Обьект был удален'})

class FAQCourseList(APIView):

    def get(self, request, *args, **kwargs):
        faq = FAQCourse.objects.all()
        serializer = FAQCourseSerializer(faq, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = FAQCourseSerializer(data=request.POST)
        if serializer.is_valid():
            faq = serializer.save()
            json_serializer = FAQCourseSerializer(instance=faq)
            return Response(data=json_serializer.data, status=201)
        return Response(data=serializer.errors)

class FAQCourseDetail(APIView):

    def get(self, request, *args, **kwargs):
        try:
            faq = FAQCourse.objects.get(pk=kwargs.get('pk'))
        except FAQCourse.DoesNotExist as e:
            return Response(data={"message": f'FAQ was not found: {e}'}, status=404)

        serializer = FAQSerializer(instance=faq)
        return Response(data=serializer.data)

    def put(self, request, *args, **kwargs):
        faq = FAQCourse.objects.get(pk=kwargs.get('pk'))
        serializer = FAQCourseSerializer(instance=faq, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


    def delete(self, request, *args, **kwargs):
        faq = FAQCourse.objects.get(pk=kwargs.get('pk'))
        faq.delete()
        return Response(data={'message': 'Обьект был удален'})




