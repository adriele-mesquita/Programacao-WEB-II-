from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 
from django.contrib.auth.models import User 
from .models import (
    Cliente, Restaurante, CategoriaProduto, Produto, Pedido,
    EnderecoCliente, ItemPedido, Avaliacao, Funcionario, Pagamento
)

# Register your models here.

admin.site.register(Restaurante)
admin.site.register(CategoriaProduto)
admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(EnderecoCliente)
admin.site.register(ItemPedido)
admin.site.register(Avaliacao)
admin.site.register(Pagamento)


class ClienteInline(admin.StackedInline): 
    model = Cliente 
    can_delete = False
    verbose_name_plural = 'Perfil de Cliente'



class FuncionarioInline(admin.StackedInline): 
    model = Funcionario
    can_delete = False
    verbose_name_plural = 'Perfil de Funcionario'


class CustomUserAdmin(BaseUserAdmin):
    inlines = (ClienteInline, FuncionarioInline) 



admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)