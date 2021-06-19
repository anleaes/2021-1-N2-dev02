from django.urls import path
from . import views

app_name = 'countries'

urlpatterns = [
    path('', views.list_countries, name='list_countries'),
    path('adicionar/', views.add_country, name='add_country'),
    path('editar/<int:id_country>/', views.edit_country, name='edit_country'),
    path('excluir/<int:id_country>/', views.delete_country, name='delete_country'),
]
