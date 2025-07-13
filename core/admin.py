from django.contrib import admin
from .models import Cliente, Restaurante, CategoriaProduto, Produto, Pedido, \
                    EnderecoCliente, ItemPedido, Avaliacao, Funcionario, Pagamento

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Restaurante)
admin.site.register(CategoriaProduto)
admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(EnderecoCliente)
admin.site.register(ItemPedido)
admin.site.register(Avaliacao)
admin.site.register(Funcionario)
admin.site.register(Pagamento)