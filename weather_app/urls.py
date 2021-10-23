from django.urls import path, include
from weather_app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('measurements', views.MeasurementsViewSet)

urlpatterns = [
    path('', include(router.urls))
    
]