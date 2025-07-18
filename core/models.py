from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente_profile', null=True, blank=True) 
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    nome = models.CharField(max_length=30, null=False, blank=False)
    telefone = models.CharField(max_length=13, null=False, blank=False)
    email = models.EmailField(max_length=30, null=True, blank=True)
   

    def __str__(self):
        return self.nome if self.nome else f"Cliente {self.id_cliente}"
       


class Restaurante(models.Model):
    id_restaurante = models.AutoField(primary_key=True)
    cnpj = models.CharField(max_length=16, unique=True, null=True, blank=True)
    nome_do_restaurante = models.CharField(max_length=30, null=False, blank=False)
    descricao = models.CharField(max_length=250, null=True, blank=True)
    categoria = models.CharField(max_length=50, null=True, blank=True)
    endereco_restaurante = models.CharField(max_length=60, null=False, blank=False)
    horario_funcionamento = models.TimeField(null=False, blank=False)

    def __str__(self):
        return self.nome_do_restaurante


class CategoriaProduto(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome_categoria = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.nome_categoria


class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=30, null=False, blank=False)
    descricao = models.CharField(max_length=250, null=False, blank=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    id_restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(CategoriaProduto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_produto


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) 
    id_restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    data_hora_pedido = models.DateTimeField(default=timezone.now, null=False, blank=False)
    status_pedido = models.CharField(max_length=60, null=False, blank=False)
    total_pedido = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    forma_pagamento = models.CharField(max_length=50, null=False, blank=False)
    troco = models.CharField(max_length=5, null=True, blank=True)
    delivery = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return f"Pedido {self.id_pedido} - Cliente: {self.id_cliente.nome}"


class EnderecoCliente(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True, blank=True)
    rua = models.CharField(max_length=50, null=False, blank=False)
    numero = models.IntegerField(null=True, blank=True)
    bairro = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=50, null=False, blank=False)
    estado = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f"Endereço de {self.id_cliente.nome}: {self.rua}, {self.numero}"


class ItemPedido(models.Model):
    id_item_pedido = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    id_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(null=False, blank=False)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return f"Item {self.id_item_pedido} - Pedido: {self.id_pedido.id_pedido}, Produto: {self.id_produto.nome_produto}"


class Avaliacao(models.Model):
    id_avaliacao = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    id_restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    comentarios = models.CharField(max_length=250, null=True, blank=True)
    estrelas = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Avaliação {self.id_avaliacao} - Restaurante: {self.id_restaurante.nome_do_restaurante}"


class Funcionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='funcionario_profile', null=True, blank=True) 
    nome_funcionario = models.CharField(max_length=50, null=False, blank=False)
    cargo = models.CharField(max_length=30, null=True, blank=True)
    data_contratacao = models.DateField(null=True, blank=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    id_restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_funcionario if self.nome_funcionario else f"Funcionário {self.id_funcionario}"


class Pagamento(models.Model):
    id_pagamento = models.AutoField(primary_key=True)
    id_pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    data_pagamento = models.DateTimeField(default=timezone.now, null=False, blank=False)
    metodo_pagamento = models.CharField(max_length=50, null=False, blank=False)
    status_pagamento = models.CharField(max_length=50, default='Pendente', null=False, blank=False)

    def __str__(self):
        return f"Pagamento {self.id_pagamento} - Pedido: {self.id_pedido.id_pedido}"