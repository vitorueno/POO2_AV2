from modelos import *
from config import *
from criar_tabelas import *

# obs.: quando uma compra é realizada, algumas informações precisam ser atualizadas (ex.: estoque do produto)
# ainda não estamos fazendo isso


def teste_exemplo():
    endereco_1 = endereco.Endereco(rua='XV de Novembro', bairro='Centro',
                                   cidade='Blumenau', numero='125')

    cliente_1 = cliente.Cliente(nome='vitor', email='abc@gmail.com',
                                data_nascimento='23/05/2022', endereco=endereco_1)

    carrinho_1 = carrinho.Carrinho(valor_total=0.0, cliente=cliente_1)

    produto_1 = produto.Produto(nome='Mouse Gamer Logitech', descricao='mouse gamer com leds rgb',
                                preco=200.00, peso='80', unidade_de_medida='gramas', estoque=50)

    produto_2 = produto.Produto(nome='MousePad grande', descricao='mousepad que parece um tapete',
                                preco=150.00, peso='40', unidade_de_medida='gramas', estoque=70)

    produto_3 = produto.Produto(nome='Teclado mecânico Razer', descricao='teclado que faz tec tec',
                                preco=350.00, peso='300', unidade_de_medida='gramas', estoque=30)

    prod_carrinho_1 = produtoCarrinho.ProdutoCarrinho(
        quant=1, produto=produto_1, carrinho=carrinho_1)

    prod_carrinho_2 = produtoCarrinho.ProdutoCarrinho(
        quant=2, produto=produto_2, carrinho=carrinho_1)

    metodoPagamento_1 = metodoPagamento.MetodoPagamento(
        nome='dinheiro', descricao='dinheiro cash din din')

    venda_1 = venda.Venda(data='28/05/2022', carrinho=carrinho_1,
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

    frase_print = '='*10 + 'Produtos cadastrados' + '='*10
    print(frase_print)
    for p in db.session.query(produto.Produto).all():
        print('nome: ', p.nome)
        print('descrição: ', p.descricao)
        print('preço: ', p.preco, '\n')

    print('='*len(frase_print))