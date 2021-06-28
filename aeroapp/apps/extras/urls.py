from django.urls import path
from . import views

app_name = 'extras'

urlpatterns = [
    path('', views.list_extras, name='list_extras'),
    path('adicionar/', views.add_extra, name='add_extra'),
    path('editar/<int:id_extra>/', views.edit_extra, name='edit_extra'),
    path('excluir/<int:id_extra>/', views.delete_extra, name='delete_extra'),
]