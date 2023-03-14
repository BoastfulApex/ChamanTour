from rest_framework import serializers
from .models import *


class AboutSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = About
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Service
        fields = "__all__"


class TourSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tour
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = "__all__"


