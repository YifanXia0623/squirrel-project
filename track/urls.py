from django.urls import path

from . import views

# Allow for namespaces in reverse URLs
app_name = 'track'

urlpatterns = [
        path('', views.index,name='index'),
        path('map/', views.map, name='map'),
        path('sightings/', views.list_sightings, name='list_sightings'),
        path('sightings/<unique_squirrel_id>/', views.update_sighting, name='update_sighting'),
        path('sightings/add/', views.create_sighting, name='create_sighting'),
        path('sightings/stats/', views.obtain_stats, name='obtain_stats'),
]
