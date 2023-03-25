from django.shortcuts import render
from .serialiers import * 
from rest_framework import generics


class AboutView(generics.ListCreateAPIView):
    serializer_class = AboutSerializer
    
    def get_queryset(self):
        return About.objects.all()
    
    
class ServiceView(generics.ListCreateAPIView):
    serializer_class = ServiceSerializer
    
    def get_queryset(self):
        return Service.objects.all()
    
    
class TourView(generics.ListCreateAPIView):
    serializer_class = TourSerializer
    
    def get_queryset(self):
        return Tour.objects.all()
    
    
class CommentView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        return Comment.objects.all()