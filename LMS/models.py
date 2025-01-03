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


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name='quizzes', on_delete=models.CASCADE)
    deadline = models.DateTimeField()

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    question_type = models.CharField(max_length=50, choices=[('mcq', 'Multiple Choice'), ('tf', 'True/False')])

class Answer(models.Model):
    student = models.ForeignKey(User, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)









