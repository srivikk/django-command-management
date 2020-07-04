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
    data = list(user_data.values())
    data1 = {"ok":True, "members": data}
    print('==============')
    print(data1)
    return JsonResponse(data1)