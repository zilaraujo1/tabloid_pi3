from unicodedata import category
from flask import Blueprint, request, jsonify, url_for, Response, json
from flask_login import login_required, current_user
from ..models import Estabelecimentos

from ..import db

estab = Blueprint('negocios', __name__)


#--------------------------GET ESTABELECIMENTOS-----------------------------------------------
@estab.route('/api/estabelecimentos', methods=['GET'])
def estabelecimento():
    estab_obj = Estabelecimentos.query.all()
    estab_json = [estab.to_json() for estab in estab_obj]
    #print(serv_json)
    return gera_response(200, "estabelecimento", estab_json, "ok")


#--------------------------GET ESTABELECIMENTOS ID-----------------------------------------------
@estab.route('/api/estabelecimentos/<id>', methods=['GET'])
def estabelecimento_id(id):
    estab_obj = Estabelecimentos.query.filter_by(id=id).first()
    estab_json = estab_obj.to_json()

    return gera_response(200, "estabelecimento", estab_json)

#--------------------------POST ESTABELECIMENTOS-----------------------------------------------
@estab.route('/api/estabelecimentos', methods=['POST'])
def cria_estabelecimento():
    body = request.get_json()
   
    try:
        estab = Estabelecimentos(nome=body["nome"],endereco=body["endereco"],
        telefone=body["telefone"], hora_func=body["hora_func"], descricao=body["descricao"],
        foto=body["foto"], fotob=body["fotob"], fotoc=body["fotoc"], fotod=body["fotod"],
        user_fk=body["user_fk"])

        db.session.add(estab)
        db.session.commit()
        return gera_response(201, "estabelecimento", estab.to_json(), "criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "estabelecimento", {}, "Erro ao cadastrar") 

#--------------------------UPDATE ESTABELECIMENTOS(PUT)----------------------------------------------
@estab.route('/api/estabelecimentos/<id>', methods=['PUT'])
def atualiza_estbelecimento(id):
    # pega o serviço
    estab_obj = Estabelecimentos.query.filter_by(id=id).first()
    # pega as modificações
    body = request.get_json()  
     
    try:
        if('nome' in body):
            estab_obj.nome = body["nome"]
        if('endereco' in body):
            estab_obj.endereco = body["endereco"]
        if('telefone' in body):
            estab_obj.telefone = body["telefone"]
        if('hora_func' in body):
            estab_obj.hora_func = body["hora_func"]
        if('descricao' in body):
            estab_obj.descricao = body["descricao"]
        if('foto' in body):
            estab_obj.foto = body["foto"]
        if('fotob' in body):
            estab_obj.fotob = body["fotob"]
        if('fotoc' in body):
            estab_obj.fotoc = body["fotoc"]
        if('fotod' in body):
            estab_obj.fotod = body["fotod"]
        
       

        db.session.add(estab_obj)
        db.session.commit()
        return gera_response(200, "estabelecimento", estab_obj.to_json(), "atualizado com sucesso")
    except Exception as e:
        print("ERRO",e)
        return gera_response(400, "estabelecimento", {}, "Erro ao atualizar") 

#--------------------------DELETE ESTABELECIMENTOS-----------------------------------------------
@estab.route('/api/estabelecimentos/<id>', methods=['DELETE'])
def deleta_estabelecimento(id):
     # pega o serviço
    estab_obj = Estabelecimentos.query.filter_by(id=id).first()
    
    try:
        db.session.delete(estab_obj)
        db.session.commit()
        return gera_response(200, "estabelecimento", estab_obj.to_json(), "Deletado com sucesso")
    except Exception as e:
        print("ERRO",e)
        return gera_response(400, "estabelecimento", {}, "Erro ao deletar") 



#--------------------------GERA RESPOSTA-------------------------------------
def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem
    return Response(json.dumps(body), status=status, mimetype="application/json")
