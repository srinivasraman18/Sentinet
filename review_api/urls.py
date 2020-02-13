from django.urls import path, include
from .views import ReviewView, RegionView

urlpatterns = [
    path('insights/', ReviewView.as_view()),
    path('region-insights/', RegionView.as_view()),
    
]