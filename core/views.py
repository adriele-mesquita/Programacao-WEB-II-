from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, CategoriaProduto, Restaurante, Cliente, Pedido
from .forms import ProdutoForm, ClienteForm, RestauranteForm, CategoriaProdutoForm, PedidoForm
from .services import ProdutoService, ClienteService, RestauranteService, CategoriaProdutoService, PedidoService

produto_service = ProdutoService()
cliente_service = ClienteService()
restaurante_service = RestauranteService()
categoria_produto_service = CategoriaProdutoService()
pedido_service = PedidoService()

def index(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def catalogo_view(request, categoria):
    return render(request, f'catalogo{categoria}.html')

def produto_list(request):
    produtos = produto_service.get_all_produtos()
    return render(request, 'produto_list.html', {'produtos': produtos})

def produto_detail(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'produto_detail.html', {'produto': produto})

def produto_create(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto_service.create_produto(form)
            return redirect('core:produto_list')
    else:
        form = ProdutoForm()
    return render(request, 'produto_form.html', {'form': form, 'form_title': 'Criar Produto'})

def produto_update(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            produto_service.update_produto(form)
            return redirect('core:produto_list')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produto_form.html', {'form': form, 'form_title': 'Editar Produto'})

def produto_delete(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto_service.delete_produto(pk)
        return redirect('core:produto_list')
    return render(request, 'produto_confirm_delete.html', {'produto': produto})

def cliente_list(request):
    clientes = cliente_service.get_all_clientes()
    return render(request, 'cliente_list.html', {'clientes': clientes})

def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'cliente_detail.html', {'cliente': cliente})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente_service.create_cliente(form)
            return redirect('core:cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'cliente_form.html', {'form': form, 'form_title': 'Cadastrar Cliente'})

def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente_service.update_cliente(form)
            return redirect('core:cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente_form.html', {'form': form, 'form_title': 'Editar Cliente'})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente_service.delete_cliente(pk)
        return redirect('core:cliente_list')
    return render(request, 'cliente_confirm_delete.html', {'cliente': cliente})


def restaurante_list(request):
    restaurantes = restaurante_service.get_all_restaurantes()
    return render(request, 'restaurante_list.html', {'restaurantes': restaurantes})

def restaurante_detail(request, pk):
    restaurante = get_object_or_404(Restaurante, pk=pk)
    return render(request, 'restaurante_detail.html', {'restaurante': restaurante})

def restaurante_create(request):
    if request.method == 'POST':
        form = RestauranteForm(request.POST)
        if form.is_valid():
            restaurante_service.create_restaurante(form)
            return redirect('core:restaurante_list')
    else:
        form = RestauranteForm()
    return render(request, 'restaurante_form.html', {'form': form, 'form_title': 'Cadastrar Restaurante'})

def restaurante_update(request, pk):
    restaurante = get_object_or_404(Restaurante, pk=pk)
    if request.method == 'POST':
        form = RestauranteForm(request.POST, instance=restaurante)
        if form.is_valid():
            restaurante_service.update_restaurante(form)
            return redirect('core:restaurante_list')
    else:
        form = RestauranteForm(instance=restaurante)
    return render(request, 'restaurante_form.html', {'form': form, 'form_title': 'Editar Restaurante'})

def restaurante_delete(request, pk):
    restaurante = get_object_or_404(Restaurante, pk=pk)
    if request.method == 'POST':
        restaurante_service.delete_restaurante(pk)
        return redirect('core:restaurante_list')
    return render(request, 'restaurante_confirm_delete.html', {'restaurante': restaurante})

def categoria_produto_list(request):
    categorias = categoria_produto_service.get_all_categorias()
    return render(request, 'categoria_produto_list.html', {'categorias': categorias})

def categoria_produto_detail(request, pk):
    categoria = get_object_or_404(CategoriaProduto, pk=pk)
    return render(request, 'categoria_produto_detail.html', {'categoria': categoria})

def categoria_produto_create(request):
    if request.method == 'POST':
        form = CategoriaProdutoForm(request.POST)
        if form.is_valid():
            categoria_produto_service.create_categoria(form)
            return redirect('core:categoria_produto_list')
    else:
        form = CategoriaProdutoForm()
    return render(request, 'categoria_produto_form.html', {'form': form, 'form_title': 'Criar Categoria'})

def categoria_produto_update(request, pk):
    categoria = get_object_or_404(CategoriaProduto, pk=pk)
    if request.method == 'POST':
        form = CategoriaProdutoForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria_produto_service.update_categoria(form)
            return redirect('core:categoria_produto_list')
    else:
        form = CategoriaProdutoForm(instance=categoria)
    return render(request, 'categoria_produto_form.html', {'form': form, 'form_title': 'Editar Categoria'})

def categoria_produto_delete(request, pk):
    categoria = get_object_or_404(CategoriaProduto, pk=pk)
    if request.method == 'POST':
        categoria_produto_service.delete_categoria(pk)
        return redirect('core:categoria_produto_list')
    return render(request, 'categoria_produto_confirm_delete.html', {'categoria': categoria})
def pedido_list(request):
    pedidos = pedido_service.get_all_pedidos()
    return render(request, 'pedido_list.html', {'pedidos': pedidos})

def pedido_detail(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    return render(request, 'pedido_detail.html', {'pedido': pedido})

def pedido_create(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido_service.create_pedido(form)
            return redirect('core:pedido_list')
    else:
        form = PedidoForm()
    return render(request, 'pedido_form.html', {'form': form, 'form_title': 'Criar Pedido'})

def pedido_update(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            pedido_service.update_pedido(form)
            return redirect('core:pedido_list')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'pedido_form.html', {'form': form, 'form_title': 'Editar Pedido'})

def pedido_delete(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido_service.delete_pedido(pk)
        return redirect('core:pedido_list')
    return render(request, 'pedido_confirm_delete.html', {'pedido': pedido})