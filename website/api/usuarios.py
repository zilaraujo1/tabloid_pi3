from unicodedata import category
from flask import Blueprint, request, jsonify, url_for, Response, json
from flask_login import login_required, current_user
from ..models import User

from ..import db

api = Blueprint('usuarios', __name__)


#--------------------------GET USUARIOS-----------------------------------------------
@api.route('/api/usuarios', methods=['GET'])
def usuarios():
    user_obj = User.query.all()
    user_json = [user.to_json() for user in user_obj]
    #print(serv_json)
    return gera_response(200, "Usuarios", user_json, "ok")


#--------------------------GET USUARIOS ID-----------------------------------------------
@api.route('/api/usuarios/<id>', methods=['GET'])
def usuarios_id(id):
    user_obj = User.query.filter_by(id=id).first()
    user_json = user_obj.to_json()

    return gera_response(200, "Usuarios", user_json)

#--------------------------POST USUARIOS-----------------------------------------------
@api.route('/api/usuarios', methods=['POST'])
def cria_usuarios():
    body = request.get_json()
   
    try:
        user = User(email=body["email"],cnpj=body["cnpj"],password=body["password"])

        db.session.add(user)
        db.session.commit()
        return gera_response(201, "Usuarios", user.to_json(), "criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "Usuarios", {}, "Erro ao cadastrar") 

#--------------------------UPDATE USUARIOS(PUT)----------------------------------------------
@api.route('/api/usuarios/<id>', methods=['PUT'])
def atualiza_usuarios(id):
    # pega o serviço
    user_obj = User.query.filter_by(id=id).first()
    # pega as modificações
    body = request.get_json()  
     
    try:
        if('email' in body):
            user_obj.email = body["email"]
        if('cnpj' in body):
            user_obj.cnpj = body["cnpj"]
        if('password' in body):
            user_obj.password = body["password"]
       

        db.session.add(user_obj)
        db.session.commit()
        return gera_response(200, "Usuario", user_obj.to_json(), "atualizado com sucesso")
    except Exception as e:
        print("ERRO",e)
        return gera_response(400, "Usuario", {}, "Erro ao atualizar") 

#--------------------------DELETE USUARIOS-----------------------------------------------
@api.route('/api/usuarios/<id>', methods=['DELETE'])
def deleta_usuario(id):
     # pega o serviço
    user_obj = User.query.filter_by(id=id).first()
    
    try:
        db.session.delete(user_obj)
        db.session.commit()
        return gera_response(200, "Usuario", user_obj.to_json(), "Deletado com sucesso")
    except Exception as e:
        print("ERRO",e)
        return gera_response(400, "Usuario", {}, "Erro ao deletar") 



#--------------------------GERA RESPOSTA-------------------------------------
def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem
    return Response(json.dumps(body), status=status, mimetype="application/json")
