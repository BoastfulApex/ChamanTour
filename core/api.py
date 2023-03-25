from apps.tours.views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'about', AboutView, basename='about') 
router.register(r'services', ServiceView, basename='serivces') 
router.register(r'tours', TourView, basename='tours')
router.register(r'comments', CommentView, basename='comments') 