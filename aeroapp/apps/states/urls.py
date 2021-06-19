from django.urls import path
from . import views

app_name = 'states'

urlpatterns = [
    path('', views.list_states, name='list_states'),
    path('adicionar/', views.add_state, name='add_state'),
    path('editar/<int:id_state>/', views.edit_state, name='edit_state'),
    path('excluir/<int:id_state>/', views.delete_state, name='delete_state'),
]
