from django.urls import path

from . import views

# Allow for namespaces in reverse URLs
app_name = 'track'

urlpatterns = [
        path('', views.index,name='index'),
        path('map/', views.map, name='map'),
        path('sightings/', views.list_sightings, name='list'),
        path('sightings/<unique_squirrel_id>/', views.update_sighting, name='update'),
        path('sightings/add/', views.create_sighting, name='create'),
        path('sightings/stats/', views.obtain_stats, name='stats'),
]
