from .models import Produto, CategoriaProduto, Restaurante, Cliente, Pedido

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