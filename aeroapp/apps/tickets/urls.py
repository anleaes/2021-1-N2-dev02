from django.urls import path
from . import views

app_name = 'tickets'

urlpatterns = [
    path('', views.list_tickets, name='list_tickets'),
    path('adicionar/', views.add_ticket, name='add_ticket'),
    path('editar/<int:id_ticket>/', views.edit_ticket, name='edit_ticket'),
    path('excluir/<int:id_ticket>/', views.delete_ticket, name='delete_ticket'),
]