from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout # <-- NOVOS IMPORTS: authenticate, login, logout
from .models import (
    Produto, CategoriaProduto, Restaurante, Cliente, Pedido, EnderecoCliente, ItemPedido, Avaliacao, Funcionario, Pagamento
)
from .forms import (
    ProdutoForm, ClienteForm, RestauranteForm, CategoriaProdutoForm, PedidoForm, EnderecoClienteForm, ItemPedidoForm, AvaliacaoForm, FuncionarioForm, PagamentoForm
)
from .services import (
    ProdutoService, ClienteService, RestauranteService, CategoriaProdutoService, PedidoService, EnderecoClienteService, ItemPedidoService, AvaliacaoService, FuncionarioService, PagamentoService
)

produto_service = ProdutoService()
cliente_service = ClienteService()
restaurante_service = RestauranteService()
categoria_produto_service = CategoriaProdutoService()
pedido_service = PedidoService()
endereco_cliente_service = EnderecoClienteService()
item_pedido_service = ItemPedidoService()
avaliacao_service = AvaliacaoService()
funcionario_service = FuncionarioService()
pagamento_service = PagamentoService()

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f"Bem-vindo(a), {username}!")
            return redirect('core:index') 
        else:
            messages.error(request, "Nome de usuário ou senha inválidos.")
    
    return render(request, 'login.html') 

def logout_view(request): 
    logout(request)
    messages.info(request, "Você saiu da sua conta.")
    return redirect('core:login_view') 

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
    return render(request, 'produto_form.html', {'form': form, 'form_title': 'Criar'}) 

def produto_update(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            produto_service.update_produto(form)
            return redirect('core:produto_list')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produto_form.html', {'form': form, 'form_title': 'Editar '})

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
            messages.success(request, 'Cliente cadastrado com sucesso! Agora você pode fazer login.') 
            return redirect('core:login_view') 
        else:
            messages.error(request, 'Erro ao cadastrar cliente. Verifique os dados informados.') 
            
    else: 
        form = ClienteForm()
    return render(request, 'cliente_form.html', {'form': form, 'form_title': 'Cadastrar '})

def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente_service.update_cliente(form)
            return redirect('core:cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente_form.html', {'form': form, 'form_title': 'Editar '})

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
    return render(request, 'restaurante_form.html', {'form': form, 'form_title': 'Cadastrar '}) 

def restaurante_update(request, pk):
    restaurante = get_object_or_404(Restaurante, pk=pk)
    if request.method == 'POST':
        form = RestauranteForm(request.POST, instance=restaurante)
        if form.is_valid():
            restaurante_service.update_restaurante(form)
            return redirect('core:restaurante_list')
    else:
        form = RestauranteForm(instance=restaurante)
    return render(request, 'restaurante_form.html', {'form': form, 'form_title': 'Editar '})

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
    return render(request, 'categoria_produto_form.html', {'form': form, 'form_title': 'Criar '})

def categoria_produto_update(request, pk):
    categoria = get_object_or_404(CategoriaProduto, pk=pk)
    if request.method == 'POST':
        form = CategoriaProdutoForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria_produto_service.update_categoria(form)
            return redirect('core:categoria_produto_list')
    else:
        form = CategoriaProdutoForm(instance=categoria)
    return render(request, 'categoria_produto_form.html', {'form': form, 'form_title': 'Editar '})

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
    return render(request, 'pedido_form.html', {'form': form, 'form_title': 'Criar '})

def pedido_update(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            pedido_service.update_pedido(form)
            return redirect('core:pedido_list')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'pedido_form.html', {'form': form, 'form_title': 'Editar '})

def pedido_delete(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido_service.delete_pedido(pk)
        return redirect('core:pedido_list')
    return render(request, 'pedido_confirm_delete.html', {'pedido': pedido})

def endereco_cliente_list(request):
    enderecos = endereco_cliente_service.get_all_enderecos()
    return render(request, 'endereco_cliente_list.html', {'enderecos': enderecos})

def endereco_cliente_detail(request, pk):
    endereco = get_object_or_404(EnderecoCliente, pk=pk)
    return render(request, 'endereco_cliente_detail.html', {'endereco': endereco})

def endereco_cliente_create(request):
    if request.method == 'POST':
        form = EnderecoClienteForm(request.POST)
        if form.is_valid():
            endereco_cliente_service.create_endereco(form)
            return redirect('core:endereco_cliente_list')
    else:
        form = EnderecoClienteForm()
    return render(request, 'endereco_cliente_form.html', {'form': form, 'form_title': 'Criar '})

def endereco_cliente_update(request, pk):
    endereco = get_object_or_404(EnderecoCliente, pk=pk)
    if request.method == 'POST':
        form = EnderecoClienteForm(request.POST, instance=endereco)
        if form.is_valid():
            endereco_cliente_service.update_endereco(form)
            return redirect('core:endereco_cliente_list')
    else:
        form = EnderecoClienteForm(instance=endereco)
    return render(request, 'endereco_cliente_form.html', {'form': form, 'form_title': 'Editar '})

def endereco_cliente_delete(request, pk):
    endereco = get_object_or_404(EnderecoCliente, pk=pk)
    if request.method == 'POST':
        endereco_cliente_service.delete_endereco(pk)
        return redirect('core:endereco_cliente_list')
    return render(request, 'endereco_cliente_confirm_delete.html', {'endereco': endereco})

def item_pedido_list(request):
    itens_pedido = item_pedido_service.get_all_itens_pedido()
    return render(request, 'item_pedido_list.html', {'itens_pedido': itens_pedido})

def item_pedido_detail(request, pk):
    item_pedido = get_object_or_404(ItemPedido, pk=pk)
    return render(request, 'item_pedido_detail.html', {'item_pedido': item_pedido})

def item_pedido_create(request):
    if request.method == 'POST':
        form = ItemPedidoForm(request.POST)
        if form.is_valid():
            item_pedido_service.create_item_pedido(form)
            return redirect('core:item_pedido_list')
    else: 
        form = ItemPedidoForm()
    return render(request, 'item_pedido_form.html', {'form': form, 'form_title': 'Criar '}) 

def item_pedido_update(request, pk):
    item_pedido = get_object_or_404(ItemPedido, pk=pk)
    if request.method == 'POST':
        form = ItemPedidoForm(request.POST, instance=item_pedido)
        if form.is_valid():
            item_pedido_service.update_item_pedido(form)
            return redirect('core:item_pedido_list')
    else:
        form = ItemPedidoForm(instance=item_pedido)
    return render(request, 'item_pedido_form.html', {'form': form, 'form_title': 'Editar'})

def item_pedido_delete(request, pk):
    item_pedido = get_object_or_404(ItemPedido, pk=pk)
    if request.method == 'POST':
        item_pedido_service.delete_item_pedido(pk)
        return redirect('core:item_pedido_list')
    return render(request, 'item_pedido_confirm_delete.html', {'item_pedido': item_pedido})

def avaliacao_list(request):
    avaliacoes = avaliacao_service.get_all_avaliacoes()
    return render(request, 'avaliacao_list.html', {'avaliacoes': avaliacoes})

def avaliacao_detail(request, pk):
    avaliacao = get_object_or_404(Avaliacao, pk=pk)
    return render(request, 'avaliacao_detail.html', {'avaliacao': avaliacao})

def avaliacao_create(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao_service.create_avaliacao(form)
            return redirect('core:avaliacao_list')
    else: 
        form = AvaliacaoForm()
    return render(request, 'avaliacao_form.html', {'form': form, 'form_title': 'Criar '}) 

def avaliacao_update(request, pk):
    avaliacao = get_object_or_404(Avaliacao, pk=pk)
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, instance=avaliacao)
        if form.is_valid():
            avaliacao_service.update_avaliacao(form)
            return redirect('core:avaliacao_list')
    else:
        form = AvaliacaoForm(instance=avaliacao)
    return render(request, 'avaliacao_form.html', {'form': form, 'form_title': 'Editar '})

def avaliacao_delete(request, pk):
    avaliacao = get_object_or_404(Avaliacao, pk=pk)
    if request.method == 'POST':
        avaliacao_service.delete_avaliacao(pk)
        return redirect('core:avaliacao_list')
    return render(request, 'avaliacao_confirm_delete.html', {'avaliacao': avaliacao})

def funcionario_list(request):
    funcionarios = funcionario_service.get_all_funcionarios()
    return render(request, 'funcionario_list.html', {'funcionarios': funcionarios})

def funcionario_detail(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    return render(request, 'funcionario_detail.html', {'funcionario': funcionario})

def funcionario_create(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            funcionario_service.create_funcionario(form)
            return redirect('core:funcionario_list')
    else: 
        form = FuncionarioForm()
    return render(request, 'funcionario_form.html', {'form': form, 'form_title': 'Criar '}) 

def funcionario_update(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            funcionario_service.update_funcionario(form)
            return redirect('core:funcionario_list')
    else:
        form = FuncionarioForm(instance=funcionario)
    return render(request, 'funcionario_form.html', {'form': form, 'form_title': 'Editar'})

def funcionario_delete(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        funcionario_service.delete_funcionario(pk)
        return redirect('core:funcionario_list')
    return render(request, 'funcionario_confirm_delete.html', {'funcionario': funcionario})

def pagamento_list(request):
    pagamentos = pagamento_service.get_all_pagamentos()
    return render(request, 'pagamento_list.html', {'pagamentos': pagamentos})

def pagamento_detail(request, pk):
    pagamento = get_object_or_404(Pagamento, pk=pk)
    return render(request, 'pagamento_detail.html', {'pagamento': pagamento})

def pagamento_create(request):
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            pagamento_service.create_pagamento(form)
            return redirect('core:pagamento_list')
    else: 
        form = PagamentoForm()
    return render(request, 'pagamento_form.html', {'form': form, 'form_title': 'Criar '}) 

def pagamento_update(request, pk):
    pagamento = get_object_or_404(Pagamento, pk=pk)
    if request.method == 'POST':
        form = PagamentoForm(request.POST, instance=pagamento)
        if form.is_valid():
            pagamento_service.update_pagamento(form)
            return redirect('core:pagamento_list')
    else:
        form = PagamentoForm(instance=pagamento)
    return render(request, 'pagamento_form.html', {'form': form, 'form_title': 'Editar '})

def pagamento_delete(request, pk):
    pagamento = get_object_or_404(Pagamento, pk=pk)
    if request.method == 'POST':
        pagamento_service.delete_pagamento(pk)
        return redirect('core:pagamento_list')
    return render(request, 'pagamento_confirm_delete.html', {'pagamento': pagamento})