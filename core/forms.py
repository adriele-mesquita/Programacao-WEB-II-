from django import forms
from .models import Produto, CategoriaProduto, Restaurante

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