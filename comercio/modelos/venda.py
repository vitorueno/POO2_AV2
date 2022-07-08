from modelos.transportador import Transportador
from modelos.carrinho import Carrinho
from modelos.metodoPagamento import MetodoPagamento
from modelos.produtoCarrinho import ProdutoCarrinho
from modelos.colaborador import Colaborador

from .config import *


class Venda(db.Model):
    '''
    Uma classe que representa uma venda no e-comerce. 
    Representa o pagamento de um certo carrinho de compras
    Envolve um método de pagamento. 

    ...

    Atributos
    ----------
    id (int):  id numérico (PK)
    data (str): data da venda
    carrinho_id (int): chave estrangeira do carrinho (FK)
    carrinho (Carrinho): dado do tipo Carrinho (relationship)
    metodoPagamento_id (int): chave estrangeira do método de pagamento
    metodoPagamento (MetodoPagamento): dado do tipo MetodoPagamento (relationship)

    Metodos
    -------
    '''

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date(), nullable=False)

    carrinho_id = db.Column(
        db.Integer, db.ForeignKey(Carrinho.id), nullable=False)
    carrinho = db.relationship("Carrinho")

    metodoPagamento_id = db.Column(
        db.Integer, db.ForeignKey(MetodoPagamento.id), nullable=False)
    metodoPagamento = db.relationship("MetodoPagamento")

    colaborador_cpf = db.Column(
        db.String(11), db.ForeignKey(Colaborador.cpf), nullable=True)
    colaborador = db.relationship("Colaborador")

    transportador_id = db.Column(
        db.Integer, db.ForeignKey(Transportador.id), nullable=False)
    transportador = db.relationship("Transportador")

    def __str__(self):
        itens = db.session.query(ProdutoCarrinho).filter_by(
            carrinho_id=self.carrinho.id)

        retorno = f'Data da Compra: {self.data}\n'
        retorno += f'Usuário: {self.carrinho.usuario}\n'
        retorno += '='*50
        retorno += f'\nitens:\n'
        retorno += '='*50
        for i in itens:
            retorno += '\n' + str(i) + '\n'
        retorno += '='*50
        retorno += f'\nValor total: {self.carrinho.valor_total}\n'

        if self.colaborador:
            retorno += f'\nVendedor: {self.colaborador}\n'

        return retorno

    def tamanho(self):
        total = getsizeof(self.id)
        total += getsizeof(self.data)
        total += getsizeof(self.carrinho_id)
        # total += self.carrinho.tamanho()
        total += getsizeof(self.metodoPagamento_id)
        # total += self.metodoPagamento.tamanho()
        total += getsizeof(self.colaborador_cpf)
        # total += self.colaborador.tamanho()
        total += getsizeof(self.transportador_id)
        # total += self.transportador.tamanho()

        return total
