from django.contrib import admin
from api.models import Mood, Action, MoodLog

admin.site.register([Mood, Action, MoodLog])