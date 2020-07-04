from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import User,ActivityPeriod
from .serializers import UserSerializer, ActivityPeriodSerializer
from rest_framework import viewsets
from rest_framework.views import APIView


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    data =list(queryset.values())

def get_data(request):
    user_data = User.objects.all()
    activity_data = ActivityPeriod.objects.all()
    data = list(user_data.values())
    for d in data:
        ap_data = list(activity_data.values())
        d['activity_periods'] = []
        for ap in ap_data:
            if d['id'] == ap['user_id']:
                del ap['id']
                del ap['user_id']
                d['activity_periods'].append(ap)
        d['id'] = d['user_id']
        del d['user_id']    
    data1 = {"ok":True, "members": data}
    return JsonResponse(data1)