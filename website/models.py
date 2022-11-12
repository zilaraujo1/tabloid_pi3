from .import db  

from flask_login import UserMixin

from sqlalchemy.sql import func

    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150))
    nome_empresa = db.Column(db.String(150))
    password = db.Column(db.String(150))
    password = db.Column(db.String(150))
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    estabelecimento = db.relationship('Estabelecimentos')

class Estabelecimentos(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    endereco = db.Column(db.String(150))
    telefone = db.Column(db.String)
    hora_func = db.Column(db.String)
    descricao = db.Column(db.Text)
    foto = db.Column(db.Text)
    user_fk = db.Column(db.Integer, db.ForeignKey("user.id"))
    servicos = db.relationship('Comercios_item')
    comercios_item = db.relationship('Servicos')





class Comercios_item(db.Model, UserMixin):
    item_id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(150))
    nome = db.Column(db.String(150))
    marca = db.Column(db.String(150))
    quantidade = db.Column(db.String(150))
    peso = db.Column(db.String(150))
    valor = db.Column(db.String(10))
    fim_promo = db.Column(db.String(150))
    foto = db.Column(db.Text, nullable =False)
    data = db.Column(db.String(20))
    estab_fk = db.Column(db.Integer, db.ForeignKey("estabelecimento.id"))
    


class Servicos(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String)
    descricao = db.Column(db.String(150))
    valor = db.Column(db.String(150))
    horario_func = db.Column(db.String(150))
    foto = db.Column(db.Text)
    data = db.Column(db.String(20))
    estab_fk = db.Column(db.Integer, db.ForeignKey('estabeleciemnto.id'))

