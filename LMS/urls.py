from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'course', CourseViewSet)
router.register(r'lesson', LessonViewSet)
router.register(r'submission', SubmissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
