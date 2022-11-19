from unicodedata import category
from flask import Blueprint, render_template, request, redirect, flash, jsonify, url_for, abort
from flask_login import login_required, current_user

 addfrom models.tables import Estabelecimento 
from .models import User
from .models import Items
from .models import Estabelecimentos

api = Blueprint('api', __name__)

@api.route('/api/produtos')

def produtos():
    nome = "Cerveja"
    preco = "12.00"
    validade = "12/09"
    TotalProd = {'nome': nome, 'preco':preco, 'validade': validade}
    return TotalProd
    

@api.route('/api/item/<id>/')
def item(id):
    
    return 'Aqui será listado apenas um produto com o id:'+id

@api.route('/api/cadastroProduto')
def cadastroProduto():
    return 'Endpoint para cadastro de produto'

