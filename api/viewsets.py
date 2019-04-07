from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from api.models import Mood, Action, MoodLog
from api.serializers import MoodSerializer, ActionSerializer, MoodLogSerializer


class MoodViewSet(viewsets.ModelViewSet):

    queryset = Mood.objects.all()
    serializer_class = MoodSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

class MoodLogViewSet(viewsets.ModelViewSet):
    queryset = MoodLog.objects.all()
    serializer_class = MoodLogSerializer
    permissions = [AllowAny,]
