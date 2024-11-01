from django.urls import path
from . import views

urlpatterns = [
    path('', views.flights_list, name='flights_list'),
    path('<int:flight_id>/', views.flight_detail, name='flight_detail'),
]
