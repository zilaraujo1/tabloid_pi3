from unicodedata import category
from flask import Blueprint, render_template, request, redirect, flash, jsonify, url_for, abort
from flask_login import login_required, current_user

#from models.tables import Estabelecimento 
from .models import User
from .models import Items
from .models import Estabelecimentos


from . import db
import json

import os

"""
    Como o arquivo estará em binario será necessário essa lib para salvar
"""
from werkzeug.utils import secure_filename

UPLOAD = 'website/static/uploads'

UPLOAD_FOLDER = os.path.join(os.getcwd(), UPLOAD)

views = Blueprint('views', __name__)


#-------------- Rota da home --------------------------------

@views.route('/', methods=['GET', 'POST'])
#@login_required
def home():

    return render_template("home.html", user=current_user)

################# Rotas do crud (Criar, editar, deletar)###############################

@views.route('/delete/<id>/', methods=['GET','POST'])
def delete(id):
   
    return redirect(url_for('views.admin'))
     


@views.route('/admin')
@login_required
def admin():
     
    return render_template("admin.html", user=current_user)

@views.route('/cadastro')
def teste():
    return render_template("cadastro.html", user=current_user)

@views.route('/form/<id>', methods=['GET','POST'])
def form(id):
    mercado = Estabelecimentos.query.get(id)
    
    return render_template('form.html', mercado=mercado, user=current_user)

##-----------Update de produtos -------------------------------------------------##
@views.route('/update', methods=['GET','POST'])
def update():

    return render_template('form.html', mercado=mercado, user=current_user)

@views.route("/editar/<id>/")
def editar(id):
    
    return render_template('editar.html', user = current_user)


##------------------API DO GOOGLE MAPS---------------------------------------------

class Comercio:
    def __init__(self, key, name, lat, lng):
        self.key  = key
        self.name = name
        self.lat  = lat
        self.lng  = lng

# AS coordenadas do endereço
comercios = (
    Comercio('mercadoA',      'Mercadinho A',  -23.571319422733524, -46.414629246163614),
    Comercio('mercadoB', 'Mercadinho B',           -23.591198056010676, -46.403604962487194),
    Comercio('mercadoC',     'Mercadinho C', -23.588869063417768, -46.40864850869)
)
comercios_by_key = {comercio.key: comercio for comercio in comercios}


@views.route('/mercadoa' ) #endpoints
def mercadoa ():
    
    mercado = db.session.query(Estabelecimentos).filter(Estabelecimentos.id==19)

    dados_items = db.session.query(Items).filter(Items.estabelecimento_id==19)
    return render_template("mercadoa.html", mercado=mercado , ofertas=dados_items, comercios=comercios, user=current_user)

@views.route ( '/mercadob' )
def  mercadob ():
    mercado = db.session.query(Estabelecimentos).filter(Estabelecimentos.id==2)

    dados_items = db.session.query(Items).filter(Items.estabelecimento_id==20)
    return  render_template ( "mercadob.html",comercios=comercios,  ofertas=dados_items,  user = current_user  )

@views.route( '/mercadoc' )
def  mercado ():
     mercado = db.session.query(Estabelecimentos).filter(Estabelecimentos.id==21)

     dados_items = db.session.query(Items).filter(Items.estabelecimento_id==21)

     return  render_template ( "mercadoc.html", comercios=comercios, ofertas=dados_items, user = current_user )

#GoogleMaps
@views.route("/<comercio_code>")
def show_comercio(comercio_code):
    comercio = comercios_by_key.get(comercio_code)
    if comercio:
        return render_template('map.html', comercio=comercio)
    else:
        abort(404)



