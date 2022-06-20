

from .config import *

from modelos.produto import Produto
from modelos.carrinho import Carrinho


class ProdutoCarrinho(db.Model):
    '''
    Uma classe que representa a relação entre carrinho e os produtos.
    Onde um produto com uma certa quantidade se relaciona com um carrinho de um Cliente.

    ...

    Atributos
    ----------
    id (int):  id numérico (PK)
    quant (int): quantidade de um certo produto
    produto_id (int): chave estrangeira do produto (FK)
    produto (Produto): dado do tipo Produto (relationship)
    carrinho_id (int): chave estrangeira do carrinho (FK)
    carrinho (Carrinho): dado do tipo Carrinho (relationship)

    Metodos
    -------
    '''

    id = db.Column(db.Integer, primary_key=True)
    quant = db.Column(db.Integer)

    produto_id = db.Column(
        db.Integer, db.ForeignKey(Produto.id), nullable=False)
    produto = db.relationship("Produto")

    carrinho_id = db.Column(
        db.Integer, db.ForeignKey(Carrinho.id), nullable=False)
    carrinho = db.relationship("Carrinho")

    def __str__(self):
        return f'{str(self.produto)} Quantidade: {self.quant}'
