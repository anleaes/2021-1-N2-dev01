from django.urls import path
from . import views

app_name = 'vaccinations'

urlpatterns = [
    path('', views.list_vaccinations, name='list_vaccinations'),
    path('adicionar/', views.add_vaccination, name='add_vaccination'),
    path('editar/<int:id_vaccination>/', views.edit_vaccination, name='edit_vaccination'),
    path('excluir/<int:id_vaccination>/', views.delete_vaccination, name='delete_vaccination'),
    path('editar_vacinação/<int:id_vaccination>/', views.edit_vaccination_status, name='edit_vaccination_status'),
    path('status_vacinação/<int:id_vaccination>/', views.list_vaccinations_status, name='list_vaccinations_status'),
]