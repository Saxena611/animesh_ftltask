from rest_framework import serializers
from ftl_api.models import ActivityPeriod

class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['user','start_time','end_time']
    