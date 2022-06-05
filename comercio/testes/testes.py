if __name__ == "__main__":
    import os
    import sys
    atual = os.path.dirname(os.path.realpath(__file__))
    pai = os.path.dirname(atual)
    sys.path.append(pai)

from modelos import Endereco, Usuario, Carrinho, Produto, ProdutoCarrinho, MetodoPagamento, Venda
from configs.config import *
from configs.criar_tabelas import *


# obs.: quando uma compra é realizada, algumas informações precisam ser atualizadas (ex.: estoque do produto)
# ainda não estamos fazendo isso


def teste_exemplo():
    endereco_1 = Endereco(logradouro='XV de Novembro', bairro='Centro',
                          cidade='Blumenau', cep='89010-000', numero='125',
                          estado='Santa Catarina', pais="Brasil")

    cliente_1 = Usuario(cpf='45002418090', nome='vitor',
                        data_nascimento=date(1999, 2, 23), endereco=endereco_1,
                        login='vitor123', email='vitor@gmail.com',
                        telefone='4002-8922', senha='*******', )

    registros = [endereco_1, cliente_1]

    carrinho_1 = Carrinho(valor_total=0.0, usuario=cliente_1)

    produto_1 = Produto(nome='Mouse Gamer Logitech', descricao='mouse gamer com leds rgb',
                             preco=200.00, peso='80', unidade_de_medida='gramas', estoque=50)

    produto_2 = Produto(nome='MousePad grande', descricao='mousepad que parece um tapete',
                             preco=150.00, peso='40', unidade_de_medida='gramas', estoque=70)

    produto_3 = Produto(nome='Teclado mecânico Razer', descricao='teclado que faz tec tec',
                             preco=350.00, peso='300', unidade_de_medida='gramas', estoque=30)

    prod_carrinho_1 = ProdutoCarrinho(
        quant=1, produto=produto_1, carrinho=carrinho_1)

    prod_carrinho_2 = ProdutoCarrinho(
        quant=2, produto=produto_2, carrinho=carrinho_1)

    metodoPagamento_1 = MetodoPagamento(
        nome='dinheiro', descricao='dinheiro cash din din')

    venda_1 = Venda(data='28/05/2022', carrinho=carrinho_1,
                    metodoPagamento=metodoPagamento_1)

    registros = [endereco_1, cliente_1, carrinho_1, produto_1, produto_2,
                 produto_3, prod_carrinho_1, prod_carrinho_2, metodoPagamento_1, venda_1]

    for r in registros:
        db.session.add(r)
        db.session.commit()


if __name__ == '__main__':
    # deletando o bd e criando novamente
    criar_tabelas()

    teste_exemplo()

    for r in db.session.query(Venda).all():
        print(r)
