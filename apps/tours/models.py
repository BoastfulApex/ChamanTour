from django.db import models

class About(models.Model):
    name_uz = models.CharField(max_length=100000)
    name_en = models.CharField(max_length=100000)
    name_ru = models.CharField(max_length=100000)
    about_uz = models.TextField(max_length=100000)
    about_en = models.TextField(max_length=100000)
    about_ru = models.TextField(max_length=100000)


class Tour(models.Model):
    name_uz = models.CharField(max_length=100000)
    name_en = models.CharField(max_length=100000)
    name_ru = models.CharField(max_length=100000)
    description_uz = models.TextField(max_length=100000)
    description_en = models.TextField(max_length=100000)
    description_ru = models.TextField(max_length=100000)
    country_uz = models.CharField(max_length=1000)
    country_en = models.CharField(max_length=1000)
    country_ru = models.CharField(max_length=1000)
    about_uz = models.TextField(max_length=100000)
    about_en = models.TextField(max_length=100000)
    about_ru = models.TextField(max_length=100000)
    image = models.ImageField(null=True)
    image2 = models.ImageField(null=True)
    

class Comment(models.Model):
    name_uz = models.CharField(max_length=100000)
    name_en = models.CharField(max_length=100000)
    name_ru = models.CharField(max_length=100000)
    comment_uz = models.TextField(max_length=100000)
    comment_en = models.TextField(max_length=100000)
    comment_ru = models.TextField(max_length=100000)
    image = models.ImageField(null=True)


class Service(models.Model):
    name_uz = models.CharField(max_length=100000)
    name_en = models.CharField(max_length=100000)
    name_ru = models.CharField(max_length=100000)
    description_uz = models.TextField(max_length=100000)
    description_en = models.TextField(max_length=100000)
    description_ru = models.TextField(max_length=100000)
    about_uz = models.TextField(max_length=100000)
    about_en = models.TextField(max_length=100000)
    about_ru = models.TextField(max_length=100000)
    image = models.ImageField(null=True)
    icon = models.ImageField(null=True)
