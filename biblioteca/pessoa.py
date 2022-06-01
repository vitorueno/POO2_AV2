from config import *

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))

    type = db.Column(db.String(50))
    
    # definições de mapeamento da classe mãe
    __mapper_args__ = {
        'polymorphic_identity':'pessoa', 
        'polymorphic_on': type # nome do campo que vincula os filhos
    }

    def __str__(self):
        return self.nome