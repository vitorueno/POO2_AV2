from .config import *

from modelos.produto import Produto
from modelos.fornecedor import Fornecedor


class FornecedorProduto(db.Model):
    '''
    Uma classe que representa a relação entre produto e fornecedor.
    Onde um produto com uma certa quantidade se relaciona com o fornecedor que o forneceu.

    Atributos
    ----------
    id (int):  id numérico (PK)
    quant (int): quantidade de um certo produto
    produto_id (int): chave estrangeira do produto (FK)
    produto (Produto): dado do tipo Produto (relationship)
    fornecedor_cnpj (str): chave estrangeira do fornecedor (FK)
    fornecedor (Fornecedor): dado do tipo Fornecedor (relationship)
    '''

    id = db.Column(db.Integer, primary_key=True)
    quant = db.Column(db.Integer)

    produto_id = db.Column(
        db.Integer, db.ForeignKey(Produto.id), nullable=False)
    produto = db.relationship("Produto")

    fornecedor_cnpj = db.Column(db.String(11), db.ForeignKey(Fornecedor.cnpj), nullable=False)
    fornecedor = db.relationship("Fornecedor")

    def __str__(self):
        return f'Produto: {str(self.produto)}\n{str(self.fornecedor)}\nQuantidade: {self.quant}'
        