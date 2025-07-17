from django import forms
from .models import (
    Produto, CategoriaProduto, Restaurante, Cliente, Pedido, EnderecoCliente, ItemPedido, Avaliacao, Funcionario, Pagamento 
)

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
class PedidoForm(forms.ModelForm):
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
            'delivery': forms.Select(choices=[('Sim', 'Sim'), ('Não', 'Não')], attrs={'class': 'input-field'}), 
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
class EnderecoClienteForm(forms.ModelForm): 
    id_cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        empty_label="Selecione o Cliente",
        label="Cliente"
    )
    id_pedido = forms.ModelChoiceField(
        queryset=Pedido.objects.all(),
        required=False, 
        empty_label="Selecione o Pedido (Opcional)",
        label="Pedido"
    )

    class Meta:
        model = EnderecoCliente
        fields = ['id_cliente', 'id_pedido', 'rua', 'numero', 'bairro', 'cidade', 'estado']
        widgets = {
            'rua': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Rua'}),
            'numero': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Número'}),
            'bairro': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Bairro'}),
            'cidade': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Cidade'}),
            'estado': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Estado'}),
        }
        labels = {
            'id_cliente': 'Cliente',
            'id_pedido': 'Pedido',
            'rua': 'Rua',
            'numero': 'Número',
            'bairro': 'Bairro',
            'cidade': 'Cidade',
            'estado': 'Estado',
        }
class ItemPedidoForm(forms.ModelForm): 
    id_pedido = forms.ModelChoiceField(
        queryset=Pedido.objects.all(),
        empty_label="Selecione o Pedido",
        label="Pedido"
    )
    id_produto = forms.ModelChoiceField(
        queryset=Produto.objects.all(),
        empty_label="Selecione o Produto",
        label="Produto"
    )

    class Meta:
        model = ItemPedido
        fields = ['id_pedido', 'id_produto', 'quantidade', 'valor_unitario']
        widgets = {
            'quantidade': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Quantidade'}),
            'valor_unitario': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Valor Unitário'}),
        }
        labels = {
            'id_pedido': 'Pedido',
            'id_produto': 'Produto',
            'quantidade': 'Quantidade',
            'valor_unitario': 'Valor Unitário',
        }
class AvaliacaoForm(forms.ModelForm):
    id_cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        required=False,
        empty_label="Selecione o Cliente (Opcional)",
        label="Cliente"
    )
    id_restaurante = forms.ModelChoiceField(
        queryset=Restaurante.objects.all(),
        empty_label="Selecione o Restaurante",
        label="Restaurante"
    )
    estrelas = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.Select(attrs={'class': 'input-field'}), 
        label="Estrelas"
    )

    class Meta:
        model = Avaliacao
        fields = ['id_cliente', 'id_restaurante', 'comentarios', 'estrelas']
        widgets = {
            'comentarios': forms.Textarea(attrs={'class': 'input-field', 'placeholder': 'Seu comentário', 'rows': 3}),
                }
        labels = {
            'id_cliente': 'Cliente',
            'id_restaurante': 'Restaurante',
            'comentarios': 'Comentários',
            'estrelas': 'Estrelas',
        }
class FuncionarioForm(forms.ModelForm): 
    id_restaurante = forms.ModelChoiceField(
        queryset=Restaurante.objects.all(),
        empty_label="Selecione o Restaurante",
        label="Restaurante"
    )

    class Meta:
        model = Funcionario
        fields = ['nome_funcionario', 'cargo', 'data_contratacao', 'salario', 'id_restaurante']
        widgets = {
            'nome_funcionario': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Nome Completo'}),
            'cargo': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Cargo'}),
            'data_contratacao': forms.DateInput(attrs={'class': 'input-field', 'type': 'date'}), 
            'salario': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Salário'}),
        }
        labels = {
            'nome_funcionario': 'Nome do Funcionário',
            'cargo': 'Cargo',
            'data_contratacao': 'Data de Contratação',
            'salario': 'Salário',
            'id_restaurante': 'Restaurante',
        }

class PagamentoForm(forms.ModelForm):
    id_pedido = forms.ModelChoiceField(
        queryset=Pedido.objects.all(),
        empty_label="Selecione o Pedido",
        label="Pedido Associado"
    )

    class Meta:
        model = Pagamento
        fields = ['id_pedido', 'valor_pago', 'data_pagamento', 'metodo_pagamento', 'status_pagamento']
        widgets = {
            'valor_pago': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Valor Pago'}),
            'data_pagamento': forms.DateTimeInput(attrs={'class': 'input-field', 'type': 'datetime-local'}),
            'metodo_pagamento': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Método de Pagamento'}),
            'status_pagamento': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Status do Pagamento'}),
        }
        labels = {
            'id_pedido': 'Pedido',
            'valor_pago': 'Valor Pago',
            'data_pagamento': 'Data do Pagamento',
            'metodo_pagamento': 'Método de Pagamento',
            'status_pagamento': 'Status do Pagamento',
        }