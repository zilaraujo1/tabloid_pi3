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

@ind.route('/beleza', methods=['GET', 'POST'])
#@login_required
def home():

    return render_template("beleza.html", user=current_user)