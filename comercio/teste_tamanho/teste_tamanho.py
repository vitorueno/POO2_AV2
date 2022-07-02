if __name__ == "__main__":
    import os
    import sys
    atual = os.path.dirname(os.path.realpath(__file__))
    pai = os.path.dirname(atual)
    sys.path.append(pai)


from math import log
import numpy as np
import matplotlib.pyplot as plt
from modelos import Endereco, Usuario, Colaborador, Carrinho, Transportador, Fornecedor
from modelos import Produto, ProdutoCarrinho, MetodoPagamento, Venda,  FornecedorProduto
from configs.config import *
from configs.criar_tabelas import *

import os


def comparar_memoria_com_bd():

    criar_tabelas()

    endereco_1 = Endereco(logradouro='XV de Novembro', bairro='Centro',
                          cidade='Blumenau', cep='89010-000', numero='125',
                          estado='Santa Catarina', pais="Brasil")

    cliente_1 = Usuario(cpf='45002418090', nome='vitor',
                        data_nascimento=date(1999, 2, 23), endereco=endereco_1,
                        login='vitor123', email='vitor@gmail.com',
                        telefone='4002-8922', senha='*******', )

    carrinho_1 = Carrinho(valor_total=0.0, usuario=cliente_1)

    fornecedor_1 = Fornecedor(
        cnpj='45002418090', nome='joãozinho fornecimentos', endereco=endereco_1)

    produto_1 = Produto(nome='Mouse Gamer Logitech', descricao='mouse gamer com leds rgb',
                             preco=200.00, peso='80', unidade_de_medida='gramas', estoque=50)

    fornecedor_produto_1 = FornecedorProduto(
        quant=50, produto=produto_1, fornecedor=fornecedor_1)

    prod_carrinho_1 = ProdutoCarrinho(
        quant=1, produto=produto_1, carrinho=carrinho_1)

    metodoPagamento_1 = MetodoPagamento(
        nome='dinheiro', descricao='dinheiro cash din din')

    transportador_1 = Transportador(nome='sedex')

    vendedor_1 = Colaborador(cpf='75393476000', nome='joão',
                             data_nascimento=date(1999, 2, 23),
                             endereco=endereco_1, salario=1000.0, turno='comercial')

    registros = [endereco_1, cliente_1, carrinho_1, produto_1,
                 prod_carrinho_1, metodoPagamento_1, fornecedor_produto_1]

    for reg in registros:
        db.session.add(reg)
        db.session.commit()

    tam_dados = 0
    qnt = 7
    range_x = range(2**qnt + 1)
    xpoints = np.array(list(range_x))
    lista_tam_dados = []
    lista_tam_dados_com_lista = []
    lista_tam_lista = []
    lista_tam_bd = []
    for i in range_x:
        # criando objeto e adicionando à lista
        venda = Venda(data=date(2022, 5, 28), carrinho=carrinho_1,
                      metodoPagamento=metodoPagamento_1, transportador=transportador_1,
                      colaborador=vendedor_1)
        registros.append(venda)
        tam_dados += venda.tamanho()
        tam_lista = getsizeof(registros)
        tam_total_objetos = tam_dados + tam_lista

        lista_tam_dados.append(tam_dados)
        lista_tam_lista.append(tam_lista)
        lista_tam_dados_com_lista.append(tam_total_objetos)

        db.session.add(venda)
        db.session.commit()
        tam_arquivo_bd = os.path.getsize(arquivobd)
        lista_tam_bd.append(tam_arquivo_bd)

        # imprimindo nos 'checkpoints'
        if i != 0 and log(i, 2) in [x for x in range(1, qnt+1)]:
            print(f'i = {i}')
            print(
                f'Tamanho dos dados: {tam_dados} bytes; ' +
                f'Tamanho da lista: {tam_lista} bytes; ' +
                f'Tamanho lista + dados: {tam_total_objetos} bytes')

            print(
                f'Tamanho do arquivo do banco de dados: {tam_arquivo_bd} bytes\n')

    y1 = np.array(lista_tam_bd)
    y2 = np.array(lista_tam_dados)
    y3 = np.array(lista_tam_lista)
    y4 = np.array(lista_tam_dados_com_lista)
    

    plt.title("Comparação dados em memória vs tamanho do arquivo")
    plt.xlabel("Número de registros")
    plt.ylabel("Tamanho em bytes")

    plt.grid()
    plt.plot(xpoints, y1, label='tamanho do arquivo do BD')
    plt.plot(xpoints, y2, label='tamanho dos dados em memória')
    plt.plot(xpoints, y3, label='tamanho da lista')
    plt.plot(xpoints, y4, label='tamanho dos dados em memória + lista')
    
    plt.legend()

    plt.show()


if __name__ == '__main__':
    comparar_memoria_com_bd()
