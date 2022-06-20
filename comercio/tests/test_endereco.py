if __name__ == "__main__":
    import os
    import sys
    atual = os.path.dirname(os.path.realpath(__file__))
    pai = os.path.dirname(atual)
    sys.path.append(pai)

from modelos import Endereco
from configs.config import *
from configs.criar_tabelas import *


class Test_Endereco:
    def test_criar(self):
        e1 = Endereco(logradouro='XV de Novembro', bairro='Centro',
                      cidade='Blumenau', cep='89010-000', numero='125',
                      estado='Santa Catarina', pais="Brasil")

        assert (e1.logradouro == 'XV de Novembro' and e1.bairro == 'Centro' and
                e1.cidade == 'Blumenau' and e1.cep == '89010-000' and
                e1.numero == '125' and e1.estado == 'Santa Catarina' and e1.pais == 'Brasil')

    def test_gravacao(self):
        criar_tabelas()
        e1 = Endereco(logradouro='XV de Novembro', bairro='Centro',
                      cidade='Blumenau', cep='89010-000', numero='125',
                      estado='Santa Catarina', pais="Brasil")

        db.session.add(e1)
        db.session.commit()

        r = db.session.query(Endereco).first()

        assert (e1.logradouro == r.logradouro and e1.bairro == r.bairro and
                e1.cidade == r.cidade and e1.cep == r.cep and
                e1.numero == r.numero and e1.estado == r.estado and e1.pais == r.pais)

    def test_permanencia(self):
        r = db.session.query(Endereco).first()
        assert r.cidade == 'Blumenau'

    def test_remocao(self):
        r = db.session.query(Endereco).first()

        r_id = r.id
        # r = Endereco.query.first()
        Endereco.query.filter(Endereco.id == r.id).delete()

        e1 = Endereco.query.get(r_id)

        assert e1 is None
