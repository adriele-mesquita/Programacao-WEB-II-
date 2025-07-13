from .models import Produto, CategoriaProduto, Restaurante

class ProdutoService:
    def get_all_produtos(self):
        return Produto.objects.all()

    def get_produto_by_id(self, produto_id):
        return Produto.objects.get(pk=produto_id)

    def create_produto(self, form):
        return form.save()

    def update_produto(self, form):
        return form.save()

    def delete_produto(self, produto_id):
        produto = self.get_produto_by_id(produto_id)
        produto.delete()