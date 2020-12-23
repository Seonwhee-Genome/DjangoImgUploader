from django.urls import path, include
#from rest_framework import routers
from .views import ImgList


urlpatterns = [
    path('',ImgList.as_view()),    
]