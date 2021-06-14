from django.urls import path
from . import views

app_name = 'Aircrafts'

urlpatterns = [
    path('', views.list_aircrafts, name='list_aircrafts'),
    path('adicionar/', views.add_aircraft, name='add_aircraft'),
    path('editar/<int:id_aircraft>/', views.edit_aircraft, name='edit_aircraft'),
    path('excluir/<int:id_aircraft>/', views.delete_aircraft, name='delete_aircraft'),
]