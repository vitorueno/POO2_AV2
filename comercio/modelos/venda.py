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

    
    transportador_id = db.Column( db.Integer, db.ForeignKey(Transportador.id), nullable=False)
    transportador = db.relationship("Transportador")

    def __str__(self):
        itens = db.session.query(ProdutoCarrinho).filter_by(
            carrinho_id=self.carrinho.id)

        retorno = f''' 
            Data da compra: {self.data}
            Usuario <
                {str(self.carrinho.usuario)}
            >

            Itens [ '''

        for i in itens:
            retorno += str(i)

        retorno += f'''
            ]

            Valor Total: {self.carrinho.valor_total}
             {self.transportador}
            '''
        if self.colaborador:
            retorno += f'''
            Vendedor: {self.colaborador}
            '''
        return retorno
