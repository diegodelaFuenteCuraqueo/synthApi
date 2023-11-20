# presets/urls.py
from django.urls import path
from .views import PresetListCreateView

urlpatterns = [
    path('presets/', PresetListCreateView.as_view(), name='preset-list-create'),
    # Add more URLs as needed for specific endpoints
]
