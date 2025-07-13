from django.urls import path
from . import views

app_name = 'core' 

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'), 
    path('catalogo/<int:categoria>/', views.catalogo_view, name='catalogo'),
    path('produtos/', views.produto_list, name='produto_list'),
    path('produtos/novo/', views.produto_create, name='produto_create'),
    path('produtos/<int:pk>/', views.produto_detail, name='produto_detail'),
    path('produtos/<int:pk>/editar/', views.produto_update, name='produto_update'),
    path('produtos/<int:pk>/deletar/', views.produto_delete, name='produto_delete'),
]
    
