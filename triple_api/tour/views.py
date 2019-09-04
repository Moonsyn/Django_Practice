# triple_api/tour/views.py

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TourSerializer
from .models import Tour

class TourViewSet(viewsets.ModelViewSet): 
    queryset = Tour.objects.all() 
    serializer_class = TourSerializer
