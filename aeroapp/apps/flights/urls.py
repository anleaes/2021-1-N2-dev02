from django.urls import path
from . import views

app_name = 'flights'

urlpatterns = [
    path('', views.list_flights, name='list_flights'),
    path('adicionar/', views.add_flight, name='add_flight'),
    path('editar/<int:id_flight>/', views.edit_flight, name='edit_flight'),
    path('excluir/<int:id_flight>/', views.delete_flight, name='delete_flight'),
]
