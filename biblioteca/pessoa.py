''' 
classe Pessoa criada pelo grupo 1 com algumas modificações
autores: Gustavo Lofrese Carvalho e Eduardo Meneghim Alves Silva
'''

from .config import *

from .endereco import Endereco


class Pessoa(db.Model):
    '''
    Uma classe que representa uma pessoa genérica.

    ...

    Atributos
    ----------
    cpf (str): cpf da pessoa (PK)
    nome (str): nome da pessoa
    dataNascimento (str): nome do bairro do endereço
    endereco_id (int): chave estrangeira, o id do endereco da pessoa
    endereco (Endereco): dado do tipo Endereco (relationship) 
    '''

    cpf = db.Column(db.String(11), primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date(), nullable=False)
    endereco_id = db.Column(db.Integer, db.ForeignKey(Endereco.id))
    endereco = db.relationship('Endereco')

    type = db.Column(db.String(50))

    # definições de mapeamento da classe mãe
    __mapper_args__ = {
        'polymorphic_identity': 'pessoa',
        'polymorphic_on': type
    }

    def __str__(self):
        return f'{self.nome} (CPF: {self.cpf}) - data nascimento: {self.data_nascimento}' +\
            f'\nEndereço: {str(self.endereco)}'

    def tamanho(self):
        total = getsizeof(self.cpf)
        total += getsizeof(self.nome)
        total += getsizeof(self.data_nascimento)
        total += getsizeof(self.endereco_id)
        total += self.endereco.tamanho()

        return total
