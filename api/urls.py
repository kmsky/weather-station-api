from django.urls import path
from . import views

urlpatterns = [
    path('api/measurement/', views.measurement_collection, name='measure_collection'),
    path("api/measurement/<int:pk>/", views.measurement_element, name='measure_element'),
    path("api/measurement/last/", views.measurement_last, name='measure_last'),
    path("api/measurement/post/", views.measurement_post, name='measure_post'),
    path("api/measurement/update/<int:pk>/", views.measurement_update, name='measure_update'),
]
