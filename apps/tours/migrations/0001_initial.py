# Generated by Django 4.1.4 on 2023-03-13 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=100000)),
                ('name_en', models.CharField(max_length=100000)),
                ('name_ru', models.CharField(max_length=100000)),
                ('about_uz', models.TextField(max_length=100000)),
                ('about_en', models.TextField(max_length=100000)),
                ('about_ru', models.TextField(max_length=100000)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=100000)),
                ('name_en', models.CharField(max_length=100000)),
                ('name_ru', models.CharField(max_length=100000)),
                ('comment_uz', models.TextField(max_length=100000)),
                ('comment_en', models.TextField(max_length=100000)),
                ('comment_ru', models.TextField(max_length=100000)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=100000)),
                ('name_en', models.CharField(max_length=100000)),
                ('name_ru', models.CharField(max_length=100000)),
                ('description_uz', models.TextField(max_length=100000)),
                ('description_en', models.TextField(max_length=100000)),
                ('description_ru', models.TextField(max_length=100000)),
                ('about_uz', models.TextField(max_length=100000)),
                ('about_en', models.TextField(max_length=100000)),
                ('about_ru', models.TextField(max_length=100000)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('icon', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=100000)),
                ('name_en', models.CharField(max_length=100000)),
                ('name_ru', models.CharField(max_length=100000)),
                ('description_uz', models.TextField(max_length=100000)),
                ('description_en', models.TextField(max_length=100000)),
                ('description_ru', models.TextField(max_length=100000)),
                ('country_uz', models.CharField(max_length=1000)),
                ('country_en', models.CharField(max_length=1000)),
                ('country_ru', models.CharField(max_length=1000)),
                ('about_uz', models.TextField(max_length=100000)),
                ('about_en', models.TextField(max_length=100000)),
                ('about_ru', models.TextField(max_length=100000)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('image2', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
