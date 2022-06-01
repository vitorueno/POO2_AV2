from pessoa import Pessoa 
from config import *

class Usuario(Pessoa):
    id = db.Column(db.Integer, db.ForeignKey('pessoa.id', ondelete="CASCADE"), primary_key=True)
    login = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))
    senha = db.Column(db.String(254))

    
    # definições de mapeamento da classe mãe
    __mapper_args__ = {
        'polymorphic_identity':'usuario', 
    }

    def __str__(self):
        retorno = super().__str__()
        retorno += f'\nLogin:{self.login}\nEmail:{self.email}\nTelefone:{self.telefone}'
        return retorno