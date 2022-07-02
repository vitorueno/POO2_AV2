
from .config import *

from modelos.usuario import Usuario


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
    usuario_cpf (int): chave estrangeira de usuario (FK)
    usuario (Usuario): dado do tipo Usuario (relationship)

    Metodos
    -------
    '''

    id = db.Column(db.Integer, primary_key=True)
    valor_total = db.Column(db.Float)

    usuario_cpf = db.Column(
        db.String, db.ForeignKey(Usuario.cpf), nullable=False)
    usuario = db.relationship("Usuario")

    def __str__(self):
        return f''' 
            Usuario: [
                {str(self.usuario)}
            ]
            Valor Total: R$ {self.valor_total:.2f}
        '''

    def tamanho(self):
        total = getsizeof(self.id)
        total += getsizeof(self.valor_total)
        total += getsizeof(self.usuario_cpf)
        total += self.usuario.tamanho()

        return total
