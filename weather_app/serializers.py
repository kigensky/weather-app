from django.db.models import fields
from rest_framework import serializers
from .models import Measurements


class MeasurementsSerializer(serializers.ModelSerializer):


    class Meta:
        model = Measurements
        fields = ['id','Days_of_the_week', 'Rainfall', 'Day_created']
