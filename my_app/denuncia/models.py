from my_app import db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import datetime
import json

class Grupo(db.Model):
    __tablename__ = 'GRUPOS'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80))
    users = db.relationship('User')

    def __init__(self, nombre):
        self.nombre = nombre

class User(db.Model):
    __tablename__ = 'USERS'

    id = db.Column(db.Integer, primary_key=True)
    ci = db.Column(db.String(14))
    nombres = db.Column(db.String(140))
    telefono = db.Column(db.String(14))
    username = db.Column(db.String(24))
    password = db.Column(db.String(24))
    grupo = db.Column(db.Integer, db.ForeignKey('GRUPOS.id'))
    denuncia = db.relationship('Denuncia')
    formulario = db.relationship('Formulario')

    def __init__(self, ci = None, nombre = None, telefono = None, username = None, password = None, grupo = None):
        self.ci = ci
        self.nombres = nombre
        self.telefono = telefono        
        self.username = username
        self.password = password
        self.grupo = grupo

    def __create_password(self, passw):
        return generate_password_hash(passw)

    def verify_password(self, passw):
        return check_password_hash(self.password, passw)


class Denuncia(db.Model):
    __tablename__ = 'DENUNCIAS'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(80))
    foto = db.Column(db.String(180))
    descripcion = db.Column(db.String(240))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    user = db.Column(db.Integer, db.ForeignKey('USERS.id'))
    image = db.relationship('Image')
    
    def __init__(self, tipo = None, 
                       foto = None, 
                       descripcion = None,
                       lat = None,
                       lon = None,
                       user = None):
        self.tipo = tipo
        self.foto = foto
        self.descripcion = descripcion
        self.lat = lat
        self.lon = lon
        self.user = user

class Image(db.Model):
    __tablename__ = 'IMAGES'

    id = db.Column(db.Integer, primary_key=True)
    namefile = db.Column(db.String(248))
    denuncia = db.Column(db.Integer, db.ForeignKey('DENUNCIAS.id'))
    
    def __init__(self, namefile):
        self.namefile = namefile

class Formulario(db.Model):
    __tablename__ = 'FORMULARIOS'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('USERS.id'))
    formulario = db.relationship('Predio')
    
    def __init__(self, user):
        self.user = user

class Predio(db.Model):
    __tablename__ = 'PREDIOS'

    id = db.Column(db.Integer, primary_key=True)
    condgnrl = db.Column(db.String(240))
    direccion = db.Column(db.String(120))
    elimres = db.Column(db.String(120))
    numadultos = db.Column(db.Integer)
    numninios = db.Column(db.Integer)
    proposito = db.Column(db.String(120))
    protecventana = db.Column(db.String(120))
    suministroagua = db.Column(db.String(120))
    form = db.Column(db.Integer, db.ForeignKey('FORMULARIOS.id'))
    formulario = db.relationship('Criadero')
    
    def __init__(self, 
                    condgnrl = None, 
                    direccion = None, 
                    elimres = None, 
                    numadultos = None, 
                    numninios= None, 
                    proposito =None, 
                    protecventana = None, 
                    suministroagua = None, 
                    form = None):
        self.condgnrl = condgnrl
        self.direccion = direccion
        self.elimres = elimres
        self.numadultos = numadultos
        self.numninios = numninios
        self.proposito = proposito
        self.protecventana = protecventana
        self.suministroagua = suministroagua
        self.elimres = elimres
        self.form = form

class Criadero(db.Model):
    __tablename__ = 'CRIADEROS'

    id = db.Column(db.Integer, primary_key=True)
    cantpculex = db.Column(db.Integer)
    cantpaedes = db.Column(db.Integer)
    preslculex = db.Column(db.String(80))
    preslaedes = db.Column(db.String(80))
    tipocriad = db.Column(db.String(240))
    volcriad = db.Column(db.Integer)
    predio = db.Column(db.Integer, db.ForeignKey('PREDIOS.id'))
    
    def __init__(self, 
                    cantpculex = None, 
                    cantpaedes = None, 
                    preslculex = None, 
                    preslaedes = None, 
                    tipocriad = None, 
                    volcriad = None, 
                    predio = None):
        self.cantpculex = cantpculex
        self.cantpaedes = cantpaedes
        self.preslaedes = preslaedes
        self.preslculex = preslculex
        self.tipocriad = tipocriad
        self.volcriad = volcriad
        self.predio = predio

class Glosario(db.Model):
    __tablename__ = 'GLOSARIO'

    id = db.Column(db.Integer, primary_key=True)
    imagen = db.Column(db.String(240))
    name = db.Column(db.String(120))
    precauciones = db.Column(db.String(240))
    sintomas = db.Column(db.String(240))
    
    def __init__(self, imagen = None, name = None, precauciones = None, sintomas= None):
        self.imagen = imagen
        self.name = name
        self.precauciones = precauciones
        self.sintomas = sintomas

class Centrosalud(db.Model):
    __tablename__ = 'CENTROS'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    descripcion = db.Column(db.String(240))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    
    def __init__(self, name = None, descripcion = None, lat = None, lon = None):
        self.name = name
        self.descripcion = descripcion
        self.lat = lat
        self.lon = lon