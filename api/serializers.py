from rest_framework import serializers
from api.models import MoodLog, Mood, Action

class MoodLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = MoodLog
        fields = '__all__'
        depth = 1

class MoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mood
        fields = '__all__'

class ActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Action
        fields = '__all__'