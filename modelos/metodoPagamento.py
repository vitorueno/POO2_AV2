if __name__ == "__main__":
    import os
    import sys
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(parentdir)

from config import *


class MetodoPagamento(db.Model):
    '''
    Uma classe que representa um método de pagamento (cartão, dinheiro...).

    ...

    Atributos
    ----------
    id (int):  id numérico (PK)
    nome (str): nome do método de pagamento
    descricao (str): descricao do tipo de pagamento

    Metodos
    -------
    '''

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    descricao = db.Column(db.String(254))

    def __str__(self):
        return f'Método de Pagamento: {self.nome} - {self.descricao}'
