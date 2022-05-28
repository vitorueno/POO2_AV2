from config import *
from modelos import *


def criar_tabelas():
    if os.path.exists(arquivobd):
        os.remove(arquivobd)
    db.create_all()


if __name__ == '__main__':
    criar_tabelas()
