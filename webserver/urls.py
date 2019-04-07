from django.urls import path
from webserver.views import homepage

urlpatterns = [
    path('', homepage)
]
