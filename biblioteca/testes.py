from pessoa import Pessoa
from usuario import Usuario
from config import *
from criar_tabelas import *


if __name__ == '__main__':
    
    criar_tabelas()

    # p1 = Pessoa(nome="vitor")
    # p2 = Pessoa(nome="Leonardo")
    u1 = Usuario(nome="vitor", login="oi", email="a@gmail.com", telefone="123", senha="123")

    u2 = Pessoa(nome="joao")

    db.session.add(u1)
    db.session.add(u2)
    db.session.commit()

    # for r in db.session.query(Usuario).all():
    #     print(r)
        
    #     print(type(r))

    # print()


    for r in db.session.query(Pessoa).all():
        print(r)
        print(r.type)
        # print(type(r))
