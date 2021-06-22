from django.urls import path
from . import views

app_name = 'passengers'

urlpatterns = [
    path('', views.list_passengers, name='list_passengers'),
    path('adicionar/', views.add_passenger, name='add_passenger'),
    path('editar/<int:id_passenger>/', views.edit_passenger, name='edit_passenger'),
    path('excluir/<int:id_passenger>/', views.delete_passenger, name='delete_passenger'),
]