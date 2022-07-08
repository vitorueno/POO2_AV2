''' 
classe Endereco criada pelo grupo 2 com algumas modificações
autores: Halena Kulmann Duarte e Luana Alves Pinto
'''

from .config import *


class Endereco(db.Model):
    '''
    Uma classe que representa o Endereco de um cliente do e-comerce.

    ...

    Atributos
    ----------
    id (int):  id numérico (PK)
    rua (str): nome da rua do endereço
    bairro (str): nome do bairro do endereço
    cidade (str): cidade do endereço
    numero (str): número da casa/apartamento... do endereço

    Metodos
    -------
    '''

    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(254))
    logradouro = db.Column(db.String(254))
    bairro = db.Column(db.String(254))
    cidade = db.Column(db.String(254))
    cep = db.Column(db.String(254))
    estado = db.Column(db.String(254))
    pais = db.Column(db.String(254))

    def __str__(self):
        return f'{self.logradouro}, {self.numero} - {self.bairro} (CEP: {self.cep}), ' +\
            f'{self.cidade} - {self.estado} - {self.pais}'

    def tamanho(self):
        total = getsizeof(self.id)
        total += getsizeof(self.numero)
        total += getsizeof(self.logradouro)
        total += getsizeof(self.bairro)
        total += getsizeof(self.cidade)
        total += getsizeof(self.cep)
        total += getsizeof(self.estado)
        total += getsizeof(self.pais)
        return total
