from django.urls import path
from . import views

app_name = 'tickets'

urlpatterns = [
    path('', views.list_tickets, name='list_tickets'),
    path('adicionar/', views.add_ticket, name='add_ticket'),
    path('excluir/<int:id_ticket>/', views.delete_ticket, name='delete_ticket'),
    path('excluir-passageiro/<int:id_ticket_passenger>/', views.delete_ticket_passenger, name='delete_ticket_passenger'),
    path('editar-status/<int:id_ticket>/', views.edit_ticket_status, name='edit_ticket_status'),
]