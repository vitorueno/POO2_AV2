if __name__ == "__main__":
    import os
    import sys
    currentdir = os.path.dirname(os.path.realpath(__file__))
    parentdir = os.path.dirname(currentdir)
    sys.path.append(parentdir)

from modelos.carrinho import Carrinho
from modelos.metodoPagamento import MetodoPagamento
from modelos.produtoCarrinho import ProdutoCarrinho

from config import *


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
    data = db.Column(db.String(254))

    carrinho_id = db.Column(
        db.Integer, db.ForeignKey(Carrinho.id), nullable=False)
    carrinho = db.relationship("Carrinho")

    metodoPagamento_id = db.Column(
        db.Integer, db.ForeignKey(MetodoPagamento.id), nullable=False)
    metodoPagamento = db.relationship("MetodoPagamento")


    def __str__(self):
        itens = db.session.query(ProdutoCarrinho).filter_by(carrinho_id = self.carrinho.id)

        retorno =  f''' 
            Data da compra: {self.data}
            Cliente <
                {str(self.carrinho.cliente)}
            >

            Itens [ ''' 

        for i in itens:  
            retorno += str(i) 

        retorno += f'''
            ]

            Valor Total: {self.carrinho.valor_total}
            '''
        return retorno

        
            
        