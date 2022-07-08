if __name__ == "__main__":
    import os
    import sys
    atual = os.path.dirname(os.path.realpath(__file__))
    pai = os.path.dirname(atual)
    sys.path.append(pai)



import numpy as np
import matplotlib.pyplot as plt
from modelos import Endereco, Usuario, Colaborador, Carrinho, Transportador, Fornecedor
from modelos import Produto, ProdutoCarrinho, MetodoPagamento, Venda,  FornecedorProduto
from configs.config import *
from configs.criar_tabelas import *

import os


def clear_data(session):
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        session.execute(table.delete())
    session.commit()


def comparar_memoria_com_bd():
    criar_tabelas()
    base = 4
    n = 7
    lista_tam_memoria = []
    lista_tam_bd = []
    lista_tam_lista = []
    for expoente in range(1, n+1):
        # deletar dados anteriores:
        clear_data(db.session)

        for r in db.session.query(Endereco).all():
            print(r)

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

        tam_mem_fixo = 0
        for reg in registros:
            tam_mem_fixo += reg.tamanho()
            db.session.add(reg)
            db.session.commit()

        for j in range(base**expoente):
            venda = Venda(data=date(2022, 5, 28), carrinho=carrinho_1,
                          metodoPagamento=metodoPagamento_1, transportador=transportador_1,
                          colaborador=vendedor_1)
            registros.append(venda)
            db.session.add(venda)
            db.session.commit()

        

        tam_bd = os.path.getsize(arquivobd)

        lista_tam_bd.append(tam_bd)
        tam_memoria = (base**expoente * venda.tamanho())  # + tam_mem_fixo
        lista_tam_memoria.append(tam_memoria)
        tam_lista = getsizeof(registros)
        lista_tam_lista.append(tam_lista)
        print(f'Quantidade de elementos = {base** expoente}')
        rows = db.session.query(Venda).count()
        print(f'Cadastrou de fato {base**expoente} elementos? ', 'Sim' if rows == base**expoente else 'Não')
        print(
            f'Tamanho dos dados: {tam_memoria} bytes; ' +
            f'Tamanho da lista: {tam_lista} bytes; ' +
            f'Tamanho lista + dados: {tam_memoria + tam_lista} bytes')

        print(
            f'Tamanho do arquivo do banco de dados: {tam_bd} bytes\n')

    y1 = np.array(lista_tam_bd)
    y2 = np.array(lista_tam_memoria)
    x_base = [base**x for x in range(1, n+1)]
    x = np.array(x_base)

    print(x_base)
    print(lista_tam_bd)
    print(lista_tam_memoria)

    plt.title("Comparação dados em memória vs tamanho do arquivo")
    plt.xlabel("Número de registros")
    plt.ylabel("Tamanho em bytes")

    y3 = np.array(lista_tam_lista)
    

    plt.grid()
    plt.plot(x, y1, label='tamanho do arquivo do BD')
    plt.plot(x, y2, label='tamanho dos dados em memória')
    plt.plot(x, y3, label='tamanho da lista')
    
    plt.legend()

    plt.show()


if __name__ == '__main__':
    comparar_memoria_com_bd()
