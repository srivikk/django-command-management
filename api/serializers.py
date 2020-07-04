from rest_framework import serializers
from .models import User,ActivityPeriod

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('real_name', 'tz')

# class ActivityPeriodSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#     class Meta:
#         model = ActivityPeriod
#         fields = ('real_name', 'tz','start_time','end_time')

class ActivityPeriodSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ActivityPeriod
        # fields = ('start_time','end_time')
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    activityperiods = ActivityPeriodSerializer(read_only=True,many=True)
    class Meta:
        model = User
        fields = '__all__'