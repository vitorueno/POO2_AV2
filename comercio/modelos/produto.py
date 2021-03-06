

from modelos.fornecedor import Fornecedor
from .config import *


class Produto(db.Model):
    '''
    Uma classe que representa o Endereco de um cliente do e-comerce.

    ...

    Atributos
    ----------
    id (int):  id numérico (PK)
    nome (str): nome do produto
    descricao (str): descrição do produto
    preco (float): preço unitário do produto
    peso (float): massa unitária do produto
    unidade_de_medida (str): unidade de medida do qual o peso se refere
    estoque (int): quantidade do produto em estoque  

    Metodos
    -------
    '''

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    descricao = db.Column(db.String(254))
    preco = db.Column(db.Float)
    peso = db.Column(db.Float)
    unidade_de_medida = db.Column(db.String(254))
    estoque = db.Column(db.Integer)

    def __str__(self):
        return f'Nome do produto: {self.nome} Descrição: {self.descricao} Preço: R$ {self.preco: .2f} Peso: {self.peso} {self.unidade_de_medida} Estoque: {self.estoque}'

    def tamanho(self):
        total = getsizeof(self.id)
        total += getsizeof(self.nome)
        total += getsizeof(self.descricao)
        total += getsizeof(self.preco)
        total += getsizeof(self.peso)
        total += getsizeof(self.unidade_de_medida)
        total += getsizeof(self.estoque)

        return total
