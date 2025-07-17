from django import forms
from .models import Produto, CategoriaProduto, Restaurante, Cliente, Pedido 


class ProdutoForm(forms.ModelForm):
    id_categoria = forms.ModelChoiceField(
        queryset=CategoriaProduto.objects.all(),
        empty_label="Selecione uma categoria",
        label="Categoria"
    )
    id_restaurante = forms.ModelChoiceField(
        queryset=Restaurante.objects.all(),
        empty_label="Selecione um restaurante",
        label="Restaurante"
    )

    class Meta:
        model = Produto
        fields = ['nome_produto', 'descricao', 'preco', 'id_restaurante', 'id_categoria']
        widgets = {
            'nome_produto': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Nome do Produto'}),
            'descricao': forms.Textarea(attrs={'class': 'input-field', 'placeholder': 'Descrição do Produto', 'rows': 3}),
            'preco': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Preço'}),
        }
        labels = {
            'nome_produto': 'Nome do Produto',
            'descricao': 'Descrição',
            'preco': 'Preço',
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'telefone', 'email', 'senha']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Nome Completo'}),
            'cpf': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'CPF (apenas números)'}),
            'telefone': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Telefone'}),
            'email': forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'E-mail'}),
            'senha': forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Senha'}),
        }
        labels = {
            'nome': 'Nome',
            'cpf': 'CPF',
            'telefone': 'Telefone',
            'email': 'E-mail',
            'senha': 'Senha',
        }

class RestauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = ['cnpj', 'nome_do_restaurante', 'descricao', 'categoria', 'endereco_restaurante', 'horario_funcionamento']
        widgets = {
            'cnpj': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'CNPJ (apenas números)'}),
            'nome_do_restaurante': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Nome do Restaurante'}),
            'descricao': forms.Textarea(attrs={'class': 'input-field', 'placeholder': 'Descrição', 'rows': 3}),
            'categoria': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Categoria (Ex: Chinesa, Brasileira)'}),
            'endereco_restaurante': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Endereço'}),
            'horario_funcionamento': forms.TimeInput(attrs={'class': 'input-field', 'placeholder': 'HH:MM:SS', 'type': 'time'}),
        }
        labels = {
            'cnpj': 'CNPJ',
            'nome_do_restaurante': 'Nome do Restaurante',
            'descricao': 'Descrição',
            'categoria': 'Categoria',
            'endereco_restaurante': 'Endereço',
            'horario_funcionamento': 'Horário de Funcionamento',
        }

class CategoriaProdutoForm(forms.ModelForm): 
    class Meta:
        model = CategoriaProduto
        fields = ['nome_categoria']
        widgets = {
            'nome_categoria': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Nome da Categoria'}),
        }
        labels = {
            'nome_categoria': 'Nome da Categoria',
        }
class PedidoForm(forms.ModelForm): # NOVO FORMULÁRIO PARA PEDIDO
    id_cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        empty_label="Selecione o Cliente",
        label="Cliente"
    )
    id_restaurante = forms.ModelChoiceField(
        queryset=Restaurante.objects.all(),
        empty_label="Selecione o Restaurante",
        label="Restaurante"
    )

    class Meta:
        model = Pedido
        fields = ['id_cliente', 'id_restaurante', 'data_hora_pedido', 'status_pedido', 'total_pedido', 'forma_pagamento', 'troco', 'delivery']
        widgets = {
            'data_hora_pedido': forms.DateTimeInput(attrs={'class': 'input-field', 'type': 'datetime-local'}),
            'status_pedido': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Status do Pedido'}),
            'total_pedido': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Total do Pedido'}),
            'forma_pagamento': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Forma de Pagamento'}),
            'troco': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Troco (opcional)'}),
            'delivery': forms.Select(choices=[('Sim', 'Sim'), ('Não', 'Não')], attrs={'class': 'input-field'}), # Exemplo de Select
        }
        labels = {
            'id_cliente': 'Cliente',
            'id_restaurante': 'Restaurante',
            'data_hora_pedido': 'Data e Hora do Pedido',
            'status_pedido': 'Status do Pedido',
            'total_pedido': 'Total do Pedido',
            'forma_pagamento': 'Forma de Pagamento',
            'troco': 'Troco',
            'delivery': 'Entrega',
        }