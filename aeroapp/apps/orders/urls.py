from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.list_orders, name='list_orders'),
    path('adicionar/', views.add_order, name='add_order'),
    path('editar/<int:id_order>/', views.edit_order, name='edit_order'),
    path('excluir/<int:id_order>/', views.delete_order, name='delete_order'),
]