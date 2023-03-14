from django.urls import path
from .views import *
urlpatterns = [
    path('about/', AboutView.as_view()),
    path('services/', ServiceView.as_view()),
    path('tours/', TourView.as_view()),
    path('comments/', CommentView.as_view()),
]
