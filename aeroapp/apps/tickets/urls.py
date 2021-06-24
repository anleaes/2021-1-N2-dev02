from django.urls import path
from . import views

app_name = 'tickets'

urlpatterns = [
    path('', views.list_tickets, name='list_tickets'),
    path('adicionar/<int:id_flight>/', views.add_ticket, name='add_ticket'),
    path('excluir/<int:id_ticket>/', views.delete_ticket, name='delete_ticket'),
    path('adicionar-passageiro/<int:id_ticket_passenger>/', views.add_ticket_passenger, name='add_ticket_passenger'),
    path('excluir-passageiro/<int:id_ticket_passenger>/', views.delete_ticket_passenger, name='delete_ticket_passenger'),
    path('editar-status/<int:id_ticket>/', views.edit_ticket_status, name='edit_ticket_status'),
]