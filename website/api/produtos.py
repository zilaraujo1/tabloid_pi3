from unicodedata import category
from flask import Blueprint, request, jsonify, url_for
from flask_login import login_required, current_user

from ..mysql import mydb

prod = Blueprint('produtos', __name__)


#--------------------------GET ITEMS-----------------------------------------------
@prod.route('/api/produtos', methods=['GET'])
def produtos():
    try:
        cursor = mydb.cursor()
        sql = "SELECT I.item_id, I.tipo, I.nome, I.marca, I.quantidade, I.peso, I.valor, I.fim_promo,I.foto, I.data, E.nome FROM comercios_item AS I INNER JOIN estabelecimentos AS E on E.id = I.estab_fk"
        #sql = "SELECT * FROM comercios_item"
        cursor.execute(sql)
        item = cursor.fetchall()
       
       # print(item)
        itemList = list()
        for items in item:
            itemList.append(
                {
                    "id": items[0],
                    "tipo":items[1],
                    "nome": items[2],
                    "marca": items[3],
                    "qtde": items[4],
                    "peso": items[5],
                    "valor": items[6],
                    "fim da promoção": items[7],
                    "foto": items[8],
                    "data":items[9],
                    #"Comércio": items[10]
                    

                }
            )
            return jsonify(
                mensagem = 'Lista de Itens',
                dados= item,
                comercio = items[10]
            )
    except Exception as ex:
        return jsonify({'menssagem': "ERRO: dados não existe!"})

   
    
#-------------------------------GET ITEMS ID--------------------------------------------------

@prod.route('/api/produtos/<int:id>', methods=['GET'])
def obter_item_por_id(id):
    try:
        cursor = mydb.cursor()

        sql = "SELECT I.item_id, I.tipo, I.nome, I.marca, I.quantidade, I.peso, I.valor, I.fim_promo,I.foto, E.nome FROM comercios_item AS I INNER JOIN estabelecimentos AS E on E.id = I.estab_fk WHERE item_id = '{0}' ".format(id)
        cursor.execute(sql)
    
        item = cursor.fetchone()
        
        dados = {'id':item[0], 'tipo':item[1],'nome':item[2], 'marca': item[3], 'qtde': item[4], 'peso': item[5], 'valor': item[6], 'fim da promoção': item[7], 'foto': item[8], 'comércio': item[9]}
        return jsonify(dados)
    except Exception as ex:
        return jsonify ({'menssagem': "Erro: registro não encontrado!"})

#-------------------------------POST---------------------------------------------------
@prod.route('/api/produtos', methods=['POST'])

def incluir_item():
    try:
        item = request.json
       # print(item)
        cursor = mydb.cursor()
        sql ="""INSERT INTO comercios_item (item_id, tipo,nome, marca, quantidade, peso, valor, fim_promo, foto, data, estab_fk) VALUES ({0},'{1}','{2}','{3}','{4}', '{5}','{6}','{7}','{8}','{9}',{10})""".format(item['item_id'],item['tipo'],item['nome'], item['marca'], item['quantidade'], item['peso'], item['valor'],item['fim promo'], item['foto'], item['data'], item['estab_fk'])
        
        cursor.execute(sql)
    
        mydb.commit()

        
        return jsonify(
            mensagem="Item cadastrado com sucesso",
        )
    except Exception as ex:
        return jsonify({'menssagem': "Error"})

#--------------------------DELETE ITEMS-----------------------------------------------