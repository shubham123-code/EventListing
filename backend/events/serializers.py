from rest_framework import serializers
from .models import *

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('host', 'name', 'uid', 'description', 'venue', 'start_date', 'end_date', 'status')

