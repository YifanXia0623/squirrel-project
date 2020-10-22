from django.urls import include, path
from django.contribute import admin

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('track.urls')),
]
