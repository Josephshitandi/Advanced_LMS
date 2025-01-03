from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('instructor', 'Instructor'), ('student', 'Student')])


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(User, related_name='courses', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)

class Enrollment(models.Model):
    student = models.ForeignKey(User, related_name='enrollments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    progress = models.FloatField(default=0)  # Track the percentage of completion

class Submission(models.Model):
    student = models.ForeignKey(User, related_name='submissions', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name='submissions', on_delete=models.CASCADE)
    content = models.TextField()
    grade = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)











