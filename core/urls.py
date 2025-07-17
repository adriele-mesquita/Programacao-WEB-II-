# foodtravel_django/core/urls.py
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('catalogo/<int:categoria>/', views.catalogo_view, name='catalogo'),

    # --- URLs para CRUD de Produto ---
    path('produtos/', views.produto_list, name='produto_list'),
    path('produtos/novo/', views.produto_create, name='produto_create'),
    path('produtos/<int:pk>/', views.produto_detail, name='produto_detail'),
    path('produtos/<int:pk>/editar/', views.produto_update, name='produto_update'),
    path('produtos/<int:pk>/deletar/', views.produto_delete, name='produto_delete'),

    # --- URLs para CRUD de Cliente ---
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/novo/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('clientes/<int:pk>/editar/', views.cliente_update, name='cliente_update'),
    path('clientes/<int:pk>/deletar/', views.cliente_delete, name='cliente_delete'),

    # --- URLs para CRUD de Restaurante ---
    path('restaurantes/', views.restaurante_list, name='restaurante_list'),
    path('restaurantes/novo/', views.restaurante_create, name='restaurante_create'),
    path('restaurantes/<int:pk>/', views.restaurante_detail, name='restaurantes_detail'), # Erro de digitação corrigido aqui: restaurantes_detail
    path('restaurantes/<int:pk>/editar/', views.restaurante_update, name='restaurante_update'),
    path('restaurantes/<int:pk>/deletar/', views.restaurante_delete, name='restaurante_delete'),

    # --- URLs para CRUD de CategoriaProduto ---
    path('categorias/', views.categoria_produto_list, name='categoria_produto_list'),
    path('categorias/novo/', views.categoria_produto_create, name='categoria_produto_create'),
    path('categorias/<int:pk>/', views.categoria_produto_detail, name='categoria_produto_detail'),
    path('categorias/<int:pk>/editar/', views.categoria_produto_update, name='categoria_produto_update'),
    path('categorias/<int:pk>/deletar/', views.categoria_produto_delete, name='categoria_produto_delete'),

    # --- NOVAS URLs para CRUD de Pedido ---
    path('pedidos/', views.pedido_list, name='pedido_list'),
    path('pedidos/novo/', views.pedido_create, name='pedido_create'),
    path('pedidos/<int:pk>/', views.pedido_detail, name='pedido_detail'),
    path('pedidos/<int:pk>/editar/', views.pedido_update, name='pedido_update'),
    path('pedidos/<int:pk>/deletar/', views.pedido_delete, name='pedido_delete'),
]