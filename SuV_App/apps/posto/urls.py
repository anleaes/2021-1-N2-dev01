from django.urls import path
from . import views

app_name = 'posto'

urlpatterns = [
    path('', views.list_postos, name='list_posto'),
    path('adicionar/', views.add_posto, name='add_posto'),
    path('editar/<int:id_posto>/', views.edit_posto, name='edit_posto'),
    path('excluir/<int:id_posto>/', views.delete_posto, name='delete_posto'),
]