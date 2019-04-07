from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Mood, Action, MoodLog
from api.serializers import MoodLogSerializer
import json

class GetAllMoods(APIView):

    def get(self, request):
        moods = Mood.objects.all().values('id', 'title', 'emoji')
        moods = list(moods)
        return Response(moods)

class GetAllActions(APIView):

    def get(self, request):
        actions = Action.objects.all().values('id', 'title', 'emoji')
        actions = list(actions)
        return Response(actions)

class GetAllMoodLogs(APIView):

    def get(self, request):
        queryset = MoodLog.objects.all()
        logs = MoodLogSerializer(queryset, many=True)
        return Response(logs.data)
