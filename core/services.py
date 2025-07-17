from django.shortcuts import get_object_or_404
from .models import (
    Produto, CategoriaProduto, Restaurante, Cliente, Pedido, EnderecoCliente, ItemPedido, Avaliacao, Funcionario, Pagamento 
)



class ProdutoService:
    def get_all_produtos(self):
        return Produto.objects.all()

    def get_produto_by_id(self, produto_id):
        try:
            return Produto.objects.get(pk=produto_id)
        except Produto.DoesNotExist:
            return None

    def create_produto(self, form):
        return form.save()

    def update_produto(self, form):
        return form.save()

    def delete_produto(self, produto_id):
        produto = self.get_produto_by_id(produto_id)
        if produto:
            produto.delete()

class ClienteService:
    def get_all_clientes(self):
        return Cliente.objects.all()

    def get_cliente_by_id(self, cliente_id):
        try:
            return Cliente.objects.get(pk=cliente_id)
        except Cliente.DoesNotExist:
            return None

    def create_cliente(self, form):
        return form.save()

    def update_cliente(self, form):
        return form.save()

    def delete_cliente(self, cliente_id):
        cliente = self.get_cliente_by_id(cliente_id)
        if cliente:
            cliente.delete()

class RestauranteService:
    def get_all_restaurantes(self):
        return Restaurante.objects.all()

    def get_restaurante_by_id(self, restaurante_id):
        try:
            return Restaurante.objects.get(pk=restaurante_id)
        except Restaurante.DoesNotExist:
            return None

    def create_restaurante(self, form):
        return form.save()

    def update_restaurante(self, form):
        return form.save()

    def delete_restaurante(self, restaurante_id):
        restaurante = self.get_restaurante_by_id(restaurante_id)
        if restaurante:
            restaurante.delete()

class CategoriaProdutoService:
    def get_all_categorias(self):
        return CategoriaProduto.objects.all()

    def get_categoria_by_id(self, categoria_id):
        try:
            return CategoriaProduto.objects.get(pk=categoria_id)
        except CategoriaProduto.DoesNotExist:
            return None

    def create_categoria(self, form):
        return form.save()

    def update_categoria(self, form):
        return form.save()

    def delete_categoria(self, categoria_id):
        categoria = self.get_categoria_by_id(categoria_id)
        if categoria:
            categoria.delete()

class PedidoService:
    def get_all_pedidos(self):
        return Pedido.objects.all()

    def get_pedido_by_id(self, pedido_id):
        try:
            return Pedido.objects.get(pk=pedido_id)
        except Pedido.DoesNotExist:
            return None

    def create_pedido(self, form):
        return form.save()

    def update_pedido(self, form):
        return form.save()

    def delete_pedido(self, pedido_id):
        pedido = self.get_pedido_by_id(pedido_id)
        if pedido:
            pedido.delete()
            
    def get_all_enderecos(self):
        return EnderecoCliente.objects.all()

    def get_endereco_by_id(self, endereco_id):
        try:
            return EnderecoCliente.objects.get(pk=endereco_id)
        except EnderecoCliente.DoesNotExist:
            return None

    def create_endereco(self, form):
        return form.save()

    def update_endereco(self, form):
        return form.save()

    def delete_endereco(self, endereco_id):
        endereco = self.get_endereco_by_id(endereco_id)
        if endereco:
            endereco.delete()

class EnderecoClienteService:
    def get_all_enderecos(self):
        return EnderecoCliente.objects.all()

    def get_endereco_by_id(self, endereco_id):
        try:
            return EnderecoCliente.objects.get(pk=endereco_id)
        except EnderecoCliente.DoesNotExist:
            return None

    def create_endereco(self, form):
        return form.save()

    def update_endereco(self, form):
        return form.save()

    def delete_endereco(self, endereco_id):
        endereco = self.get_endereco_by_id(endereco_id)
        if endereco:
            endereco.delete()

class ItemPedidoService:
    def get_all_itens_pedido(self):
        return ItemPedido.objects.all()

    def get_item_pedido_by_id(self, item_pedido_id):
        try:
            return ItemPedido.objects.get(pk=item_pedido_id)
        except ItemPedido.DoesNotExist:
            return None

    def create_item_pedido(self, form):
        return form.save()

    def update_item_pedido(self, form):
        return form.save()

    def delete_item_pedido(self, item_pedido_id):
        item_pedido = self.get_item_pedido_by_id(item_pedido_id)
        if item_pedido:
            item_pedido.delete()

class AvaliacaoService: 
    def get_all_avaliacoes(self):
        return Avaliacao.objects.all()

    def get_avaliacao_by_id(self, avaliacao_id):
        try:
            return Avaliacao.objects.get(pk=avaliacao_id)
        except Avaliacao.DoesNotExist:
            return None

    def create_avaliacao(self, form):
        return form.save()

    def update_avaliacao(self, form):
        return form.save()

    def delete_avaliacao(self, avaliacao_id):
        avaliacao = self.get_avaliacao_by_id(avaliacao_id)
        if avaliacao:
            avaliacao.delete()


class FuncionarioService:
    def get_all_funcionarios(self):
        return Funcionario.objects.all()

    def get_funcionario_by_id(self, funcionario_id):
        try:
            return Funcionario.objects.get(pk=funcionario_id)
        except Funcionario.DoesNotExist:
            return None

    def create_funcionario(self, form):
        return form.save()

    def update_funcionario(self, form):
        return form.save()

    def delete_funcionario(self, funcionario_id):
        funcionario = self.get_funcionario_by_id(funcionario_id)
        if funcionario:
            funcionario.delete()

class PagamentoService: # NOVO SERVIÇO PARA PAGAMENTO
    def get_all_pagamentos(self):
        return Pagamento.objects.all()

    def get_pagamento_by_id(self, pagamento_id):
        try:
            return Pagamento.objects.get(pk=pagamento_id)
        except Pagamento.DoesNotExist:
            return None

    def create_pagamento(self, form):
        return form.save()

    def update_pagamento(self, form):
        return form.save()

    def delete_pagamento(self, pagamento_id):
        pagamento = self.get_pagamento_by_id(pagamento_id)
        if pagamento:
            pagamento.delete()


