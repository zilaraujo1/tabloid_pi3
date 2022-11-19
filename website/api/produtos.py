from unicodedata import category
from flask import Blueprint, request, jsonify, url_for, Response, json
from flask_login import login_required, current_user
from ..models import Comercios_item

from ..import db

prod = Blueprint('produtos', __name__)


#--------------------------GET PRDUTOS-----------------------------------------------
@prod.route('/api/produtos', methods=['GET'])
def produtos():
    serv_obj = Comercios_item.query.all()
    serv_json = [serv.to_json() for serv in serv_obj]
    #print(serv_json)
    return gera_response(200, "Produtos", serv_json, "ok")


#--------------------------GET PRODUTOS ID-----------------------------------------------
@prod.route('/api/produtos/<id>', methods=['GET'])
def produtos_id(id):
    prod_obj = Comercios_item.query.filter_by(item_id=id).first()
    prod_json = prod_obj.to_json()

    return gera_response(200, "Produto", prod_json)

#--------------------------POST PRODUTOS-----------------------------------------------
@prod.route('/api/produtos', methods=['POST'])
def cria_produtos():
    body = request.get_json()
   
    try:
        prod = Comercios_item(tipo=body["tipo"],nome=body["nome"],marca=body["marca"],
        quantidade=body["quantidade"],peso=body["peso"],valor=body["valor"],
        fim_promo=body["fim_promo"],foto=body["foto"],estab_fk=body["estab_fk"])

        db.session.add(prod)
        db.session.commit()
        return gera_response(201, "Produto", prod.to_json(), "criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "Produto", {}, "Erro ao cadastrar") 

#--------------------------UPDATE PRODUTOS(PUT)----------------------------------------------
@prod.route('/api/produtos/<id>', methods=['PUT'])
def atualiza_produtos(id):
    # pega o serviço
    prod_obj = Comercios_item.query.filter_by(item_id=id).first()
    # pega as modificações
    body = request.get_json()  
     
    try:
        if('tipo' in body):
            prod_obj.tipo = body["tipo"]
        if('nome' in body):
            prod_obj.nome = body["nome"]
        if('marca' in body):
            prod_obj.valor = body["marca"]
        if('quantidade' in body):
            prod_obj.quantidade = body["quantidade"]
        if('peso' in body):
            prod_obj.peso = body["peso"]
        if('valor' in body):
            prod_obj.valor = body["valor"]
        if('foto' in body):
            prod_obj.foto = body["foto"]
        if('fim_promo' in body):
            prod_obj.fim_promo = body["fim_promo"]


        db.session.add(prod_obj)
        db.session.commit()
        return gera_response(200, "Produto", prod_obj.to_json(), "atualizado com sucesso")
    except Exception as e:
        print("ERRO",e)
        return gera_response(400, "Produto", {}, "Erro ao atualizar") 

#--------------------------DELETE PRODUTOS-----------------------------------------------
@prod.route('/api/produtos/<id>', methods=['DELETE'])
def deleta_produtos(id):
     # pega o serviço
    prod_obj = Comercios_item.query.filter_by(item_id=id).first()
    
    try:
        db.session.delete(prod_obj)
        db.session.commit()
        return gera_response(200, "Produto", prod_obj.to_json(), "Deletado com sucesso")
    except Exception as e:
        print("ERRO",e)
        return gera_response(400, "Produto", {}, "Erro ao deletar") 



#--------------------------GERA RESPOSTA-------------------------------------
def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem
    return Response(json.dumps(body), status=status, mimetype="application/json")
