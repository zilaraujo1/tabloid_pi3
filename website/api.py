from unicodedata import category
from flask import Blueprint, render_template, request, redirect, flash, jsonify, url_for, abort
from flask_login import login_required, current_user

#from models.tables import Estabelecimento 
from .models import User
from .models import Items
from .models import Estabelecimentos

from .mysql import mydb

api = Blueprint('api', __name__)

#---------------------------USUARIOS GET-------------------------------------------------------
@api.route('/api/usuarios', methods=['GET'])
def getUsuario():
    cursor = mydb.cursor()
    sql = "SELECT * FROM usuario"
    cursor.execute(sql)

    users = cursor.fetchall()
    userList = list()
    for usuario in users:
        userList.append(
            {
               'id': usuario[0],
               'nome': usuario[1],
               'cpf': usuario[2],
               'telefone': usuario[3]


            }
        )
    return jsonify(
        mensagem = 'Lista de Usuários',
        dados= userList
    )
#---------------------------USUARIOS ID--------------------------------------------------------
@api.route('/api/usuario/<int:id>', methods=['GET'])
def obter_usuario_por_id(id):
    
    cursor = mydb.cursor()

    sql = "SELECT * FROM usuario WHERE id = '{0}' ".format(id)
    cursor.execute(sql)
  
    user = cursor.fetchone()
    
    return jsonify(user)

#-------------------------POST------------------------------------------------
@api.route('/api/usuario', methods=['POST'])
def incluir_usuario():
    user = request.json
    cursor = mydb.cursor()
    sql = f"INSERT INTO usuario (nome,cpf, telefone) VALUES ('{user['nome']}','{user['cpf']}','{user['telefone']} ')"
    cursor.execute(sql)
    mydb.commit()

    return jsonify(
        mensagem="Usuário cadastrato com sucesso",
        video=user
    )
#-----------------------------------------------------------------------------------
@api.route('/api/produtos')

def produtos():
    nome = "Cerveja"
    preco = "12.00"
    validade = "12/09"
    TotalProd = {'nome': nome, 'preco':preco, 'validade': validade}
    return TotalProd
    
#-----------------------------------------------------------------------------------
@api.route('/api/item/<id>/')
def item(id):
    
    return 'Aqui será listado apenas um produto com o id:'+id
#-----------------------------------------------------------------------------------
@api.route('/api/cadastroProduto')
def cadastroProduto():
    return 'Endpoint para cadastro de produto'

