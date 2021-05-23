from django.urls import path
from .views import *

urlpatterns = [
    path('about-us/', AboutUsListView.as_view(), name='about-us-list-create'),
    path('about-us/<int:pk>/', AboutUsDetailView.as_view(), name='about-us'),

    path('advantages/', AdvantagesListView.as_view(), name='advantages-list-create'),
    path('advantages/<int:pk>/', AdvantagesDetailView.as_view(), name='advantages'),

    path('course-category/', CourseCategoryList.as_view(), name='course_category-list-create'),
    path('course-category/<int:pk>/', CourseCategoryDetail.as_view(), name='course_category'),
    #
    path('course/', CourseList.as_view(), name='course-list-create'),
    path('course/<int:pk>/', CourseDetail.as_view(), name='course'),

    path('contact/', ContactList.as_view(), name='contact-list-create'),
    path('contact/<int:pk>/', ContactDetail.as_view(), name='contact'),

    path('mentor/', MentorList.as_view(), name='mentor-list-create'),
    path('mentor/<int:pk>/', MentorDetail.as_view(), name='mentor'),

    path('application/', ApplicationList.as_view(), name='application-list-create'),
    path('application/<int:pk>/', ApplicationDetail.as_view(), name='application'),

    path('feedback/', FeedbackList.as_view(), name='feedback-list-create'),
    path('feedback/<int:pk>/', FeedbackDetail.as_view(), name='feedback'),

    path('category-event/', CategoryEventList.as_view(), name='category_event-list-create'),
    path('category-event/<int:pk>/', CategoryEventDetail.as_view(), name='category_event'),

    path('event/', EventList.as_view(), name='event-list-create'),
    path('event/<int:pk>/', EventDetail.as_view(), name='event'),

    path('FAQ/', FAQList.as_view(), name='FAQ-list-create'),
    path('FAQ/<int:pk>/', FAQDetail.as_view(), name='FAQ'),


]