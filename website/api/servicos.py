from unicodedata import category
from flask import Blueprint, request, jsonify, url_for, Response, json
from flask_login import login_required, current_user
from ..models import Servicos

from ..import db

serv = Blueprint('servicos', __name__)


#--------------------------GET SERVICOS-----------------------------------------------
@serv.route('/api/servicos', methods=['GET'])
def servicos():
    serv_obj = Servicos.query.all()
    serv_json = [serv.to_json() for serv in serv_obj]
    #print(serv_json)
    return gera_response(200, "servicos", serv_json, "ok")


#--------------------------GET SERVICOS ID-----------------------------------------------
@serv.route('/api/servicos/<id>', methods=['GET'])
def servicos_id(id):
    serv_obj = Servicos.query.filter_by(id=id).first()
    serv_json = serv_obj.to_json()

    return gera_response(200, "Serviços", serv_json)

#--------------------------POST SERVICOS-----------------------------------------------
@serv.route('/api/servicos', methods=['POST'])
def cria_servicos():
    body = request.get_json()
   
    try:
        serv = Servicos(tipo=body["tipo"],descricao=body["descricao"],valor=body["valor"],horario_func=body["horario_func"],foto=body["foto"],fotob=body["fotob"],fotoc=body["fotoc"],fotod=body["fotod"],estab_fk=body["estab_fk"])
        db.session.add(serv)
        db.session.commit()
        return gera_response(201, "Serviço", serv.to_json(), "criado com sucesso")
    except Exception as e:
        print(e)
        return gera_response(400, "Serviço", {}, "Erro ao cadastrar") 

#--------------------------UPDATE SERVICOS(PUT)----------------------------------------------
@serv.route('/api/servicos', methods=['PUT'])
def atualiza_servicos():  


        return gera_response(400, "Serviço", {}, "Erro ao atualizar") 

#--------------------------DELETE SERVICOS-----------------------------------------------
@serv.route('/api/servicos', methods=['DELETE'])
def deleta_servicos():  
        return gera_response(400, "Serviço", {}, "Erro ao deletar") 



#--------------------------GERA RESPOSTA-------------------------------------
def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem
    return Response(json.dumps(body), status=status, mimetype="application/json")
