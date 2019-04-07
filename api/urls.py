from django.urls import path, include

from rest_framework.routers import DefaultRouter
from api.viewsets import *

router = DefaultRouter()
router.register(r'moods', MoodViewSet)
router.register(r'actions', ActionViewSet)
router.register(r'logs', MoodLogViewSet)

urlpatterns = [
    path('', include(router.urls))
]
