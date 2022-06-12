''' 
classe Colaborador criada pelo grupo 3 com algumas modificações
autores: Sandy Hoffmann e Erick José Heiler
'''
from .config import *
from .pessoa import Pessoa


class Colaborador(Pessoa):
    '''
    Uma classe que representa um colaborador, que é uma pessoa.

    Atributos Herdados:
    ----------
    cpf (str): cpf da pessoa (PK)
    nome (str): nome da pessoa
    dataNascimento (str): nome do bairro do endereço
    endereco_id (int): chave estrangeira, o id do endereco da pessoa
    endereco (Endereco): dado do tipo Endereco (relationship) 

    Atributos Próprios: 
    ----------
    salario (float): salario do colaborador
    turno (str): turno do colaborador
    '''

    cpf = db.Column(db.String(11), db.ForeignKey(
        'pessoa.cpf', ondelete="CASCADE"), primary_key=True)
    salario = db.Column(db.Float)
    turno = db.Column(db.String(254))

    __mapper_args__ = {
        'polymorphic_identity': 'colaborador'
    }

    def __str__(self):
        return super().__str__() + f' - Turno {self.turno} - salario: {self.salario}'
