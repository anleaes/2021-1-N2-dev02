from django.urls import path
from . import views

app_name = 'cities'

urlpatterns = [
    path('', views.list_cities, name='list_cities'),
    path('adicionar/', views.add_city, name='add_city'),
    path('editar/<int:id_city>/', views.edit_city, name='edit_city'),
    path('excluir/<int:id_city>/', views.delete_city, name='delete_city'),
]