from django.urls import path
from . import views

app_name = 'routes'

urlpatterns = [
    path('', views.list_routes, name='list_routes'),
    path('adicionar/', views.add_route, name='add_route'),
    path('editar/<int:id_route>/', views.edit_route, name='edit_route'),
    path('excluir/<int:id_route>/', views.delete_route, name='delete_route'),
]
