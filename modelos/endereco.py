if __name__ == '__main__':
    import os
    import sys
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(parentdir)

from config import *


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
    rua = db.Column(db.String(254))
    bairro = db.Column(db.String(254))
    cidade = db.Column(db.String(254))
    numero = db.Column(db.String(254))

    def __str__(self):
        return f'{self.rua}, {self.numero} - {self.bairro}, {self.cidade}'


if __name__ == '__main__':

    endereco = Endereco(rua='XV de Novembro', bairro='Centro',
                        cidade='Blumenau', numero='125')

    print(endereco.rua)
