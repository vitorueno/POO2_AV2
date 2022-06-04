if __name__ == "__main__":
    import os
    import sys
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(parentdir)

from modelos.endereco import Endereco

from configs.config import *


class Cliente (db.Model):
    '''
    Uma classe que representa um cliente do e-comerce.

    ...

    Atributos
    ----------
    id (int):  id numérico da pessoa (PK)
    nome (str): nome completo da pessoa
    email (str): e-mail da pessoa
    data_nascimento (str): data de nascimento da pessoa
    endereco_id (int): chave estrangeira, o id do endereco da pessoa
    endereco (Endereco): dado do tipo Endereco (relationship) 

    Metodos
    -------
    '''

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    data_nascimento = db.Column(db.String(254))

    endereco_id = db.Column(
        db.Integer, db.ForeignKey(Endereco.id), nullable=False)
    endereco = db.relationship("Endereco")

    def __str__(self):
        return f'''
            Nome: {self.nome}
            E-mail: {self.email}
            Data de Nascimento: {self.data_nascimento}
            Endereço: {str(self.endereco)}
        '''

if __name__ == "__main__":
    pass
