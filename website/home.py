from unicodedata import category
from flask import Blueprint, render_template, request, redirect, flash, jsonify, url_for, abort
from flask_login import login_required, current_user


from .models import User
from .models import Comercios_item
from .models import Estabelecimentos
from .models import Servicos


from . import db
import json

import os

"""
    Como o arquivo estará em binario será necessário essa lib para salvar
"""
from werkzeug.utils import secure_filename

UPLOAD = 'website/static/uploads'

UPLOAD_FOLDER = os.path.join(os.getcwd(), UPLOAD)

ind = Blueprint('home', __name__)


#-------------- Rota da home --------------------------------

@ind.route('/servicos/<id>', methods=['GET', 'POST'])
#@login_required
def servicos(id):
    
    #serv = Servicos.query.get(estab_fk)
    dono = Estabelecimentos.query.get(id)
    estab = db.session.query(Servicos).filter(Servicos.estab_fk==id)

    if  not dono or not estab :
        flash("Não há nenhum serviço cadastrado ainda", category="error")
        return redirect('/')

    else:
        for result in estab:
            

            serv = result
    print(dono.id)
    return render_template("beleza.html",dono=dono, serv=serv, user=current_user)