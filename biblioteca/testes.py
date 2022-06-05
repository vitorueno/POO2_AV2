from config import *
from criar_tabelas import *
from endereco import Endereco
from pessoa import Pessoa
from usuario import Usuario


if __name__ == '__main__':
    criar_tabelas()

    e1 = Endereco(logradouro='XV de Novembro', bairro='Centro',
                  cidade='Blumenau', cep='89010-000', numero='125',
                  estado='Santa Catarina', pais="Brasil")

    p1 = Pessoa(cpf='45002418090', nome='Jonas',
                data_nascimento=date(1997, 2, 23), endereco=e1)

    u1 = Usuario(cpf='45002418090', nome='Jonas',
                 data_nascimento=date(1997, 2, 23), endereco=e1,
                 login='jonas123', email='jonas@gmail.com',
                 telefone='4002-8922', senha='*******', )

    db.session.add(e1)
    db.session.add(u1)
    db.session.commit()

    for r in db.session.query(Usuario).all():
        print(r)
