from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url
from . import views

router = routers.DefaultRouter()

# router.register('user', views.UserSerializer)
router.register(r'activities', views.UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('get_data/', views.get_data),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]