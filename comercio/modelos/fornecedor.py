from .config import *
from .endereco import Endereco


class Fornecedor(db.Model):
    '''
    Uma classe que representa o fornecedor no e-comerce.

    Atributos
    ----------
    cnpj (str):  cnpj do fornecedor (PK)
    nome (str): nome do fornecedor
    endereco_id (int): chave estrangeira, o id do endereco
    endereco (Endereco): dado do tipo Endereco (relationship) 
    '''

    cnpj = db.Column(db.String(11), primary_key=True)
    nome = db.Column(db.String(254))
    endereco_id = db.Column(db.Integer, db.ForeignKey(Endereco.id))
    endereco = db.relationship('Endereco')

    def __str__(self):
        return f'Fornecedor: {self.nome} ({self.cnpj})' +\
            f'{str(self.endereco)}'

    def tamanho(self):
        total = getsizeof(self.cnpj)
        total += getsizeof(self.nome)
        total += getsizeof(self.endereco_id)
        # total += self.endereco.tamanho()

        return total
