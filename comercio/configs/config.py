# importações
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import date
from sys import getsizeof

# flask
app = Flask(__name__)

# sqlalchemy com sqlite
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'comercio.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db = SQLAlchemy(app)
