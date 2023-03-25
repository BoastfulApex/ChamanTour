from django.shortcuts import render
from .serialiers import * 
from rest_framework import generics


class AboutView(generics.ListAPIView):
    serializer_class = AboutSerializer
    
    def get_queryset(self):
        return About.objects.all()
    
    
class ServiceView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    
    def get_queryset(self):
        return Service.objects.all()
    
    
class TourView(generics.ListAPIView):
    serializer_class = TourSerializer
    
    def get_queryset(self):
        return Tour.objects.all()
    
    
class CommentView(generics.ListAPIView):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        return Comment.objects.all()