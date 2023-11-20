# yourprojectname/urls.py
from django.urls import path, include

urlpatterns = [
    # Other URL patterns...
    path('api/', include('presets.urls')),  # Point to your presets app's URLs
]
