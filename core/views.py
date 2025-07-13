from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, CategoriaProduto, Restaurante
from .forms import ProdutoForm
from .services import ProdutoService

# Create your views here.

produto_service = ProdutoService()
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
    produto = produto_service.get_produto_by_id(pk)
    return render(request, 'produto_detail.html', {'produto': produto})

def produto_create(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto_service.create_produto(form) # 
            return redirect('core:produto_list')
    else:
        form = ProdutoForm()
    return render(request, 'produto_form.html', {'form': form, 'form_title': 'Criar Produto'})

def produto_update(request, pk):
    produto = produto_service.get_produto_by_id(pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            produto_service.update_produto(form) 
            return redirect('core:produto_list')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produto_form.html', {'form': form, 'form_title': 'Editar Produto'})

def produto_delete(request, pk):
    produto = produto_service.get_produto_by_id(pk)
    if request.method == 'POST':
        produto_service.delete_produto(pk) 
        return redirect('core:produto_list')
    return render(request, 'produto_confirm_delete.html', {'produto': produto})




