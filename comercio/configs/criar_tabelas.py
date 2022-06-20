from configs.config import *
from modelos import *


def criar_tabelas():
    if os.path.exists(arquivobd):
        os.remove(arquivobd)
    db.create_all()
    return os.path.exists(arquivobd)


if __name__ == '__main__':
    criar_tabelas()
