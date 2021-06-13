from django.urls import path
from . import views

app_name = 'vaccines'

urlpatterns = [
    path('', views.list_vaccines, name='list_vaccines'),
    path('adicionar/', views.add_vaccine, name='add_vaccine'),
    path('editar/<int:id_vaccine>/', views.edit_vaccine, name='edit_vaccine'),
    path('excluir/<int:id_vaccine>/', views.delete_vaccine, name='delete_vaccine'),
]