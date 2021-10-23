from django.shortcuts import render
from rest_framework import viewsets

from weather_app.serializers import MeasurementsSerializer
from .models import Measurements

# Create your views here.

class MeasurementsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Measurements.objects.all()
    serializer_class = MeasurementsSerializer