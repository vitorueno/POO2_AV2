if __name__ == "__main__":
    import os
    import sys
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(parentdir)

from modelos.cliente import Cliente
from configs.config import *


class Carrinho(db.Model):
    '''
    Uma classe que representa um Carrinho. 
    Pertence a um cliente e é a partir deste objeto que os produtos 
    vão se relacionar.

    ...

    Atributos
    ----------
    id (int):  id numérico (PK)
    valor_total (float): valor total dos produtos que estão no carrinho
    cliente_id (int): chave estrangeira de cliente (FK)
    cliente (Cliente): dado do tipo Cliente (relationship)

    Metodos
    -------
    '''

    id = db.Column(db.Integer, primary_key=True)
    valor_total = db.Column(db.Float)

    cliente_id = db.Column(
        db.Integer, db.ForeignKey(Cliente.id), nullable=False)
    cliente = db.relationship("Cliente")


    def __str__(self):
        return f''' 
            Cliente: [
                {str(self.cliente)}
            ]
            Valor Total: R$ {self.valor_total:.2f}
        '''
