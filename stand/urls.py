from django.urls import path

from . import views

app_name = "stand"

urlpatterns = [
    path('stands/list/', views.Listar.as_view(), name='listarstand'),
    path('stands/detail/<int:pk>/', views.Detalharstand.as_view(), name='detalharstand'),
    path('stands/update/<int:pk>/', views.Editar.as_view(), name='editarstand'),
    path('stands/delete/<int:pk>/', views.Apagar.as_view(), name='apagarstand'),
    path('stands/create/', views.Cadastrar.as_view(), name='cadastrarstand'),
]