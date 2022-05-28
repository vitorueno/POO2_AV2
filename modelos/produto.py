if __name__ == "__main__":
    import os
    import sys
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(parentdir)

from config import *


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
