from .config import *


class Transportador(db.Model):
    '''
    Uma classe que representa o transportador no e-comerce.

    Atributos
    ----------
    id (int):  id numérico (PK)
    nome (str): nome do transportador
    '''

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))

    def __str__(self):
        return f'transportador: {self.nome}'

    def tamanho(self):
        total = getsizeof(self.id)
        total += getsizeof(self.nome)

        return total
