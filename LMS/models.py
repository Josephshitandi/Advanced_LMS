# models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('instructor', 'Instructor'), ('student', 'Student')])










from django.db import models

# Create your models here.
