from flask import Blueprint
from flask import abort
from flask import jsonify
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from my_app import db
from my_app import app
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
from my_app.denuncia.models import *
import decimal

app.config['GOOGLEMAPS_KEY'] = "AIzaSyDeKhMCtFrlcFvMR3al-FHkspe2qivMJ2o"

GoogleMaps(app, key="AIzaSyDeKhMCtFrlcFvMR3al-FHkspe2qivMJ2o")

denuncia = Blueprint('denuncia', __name__)

@denuncia.route('/',methods=['GET'])
def home():
    res = []
    dnns = Denuncia.query.all()
    if dnns:
        for dn in dnns:
            res.append({
                'icon': icons.dots.yellow,
                'lat': dn.lat,
                'lng': dn.lon,
                'infobox': dn.descripcion
                })

    mymap = Map(
        identifier = "view-side",
        style = (
            "height:400px;"
            "width:100%;"
            "position:relative;"
        ),
        varname = "mymap",
        lat = -17.7862900,
        lng = -63.1811700,
        markers = res
    )
    return render_template('index.html', mymap=mymap )

#@grupo%

@denuncia.route('/api/grupo',methods=['GET'])
def returnAllgroup():
    res = []
    groups = Grupo.query.all()
    if groups:
        for gr in groups:
            res.append({
                'id': gr.id,
                'nombre': gr.nombre
                })
    else:
        res = [{'messaje':'no =v'}]
    return jsonify(res)

@denuncia.route('/api/grupo/<string:id>', methods=['GET'])
def getXidgroup(id = None):
    res = []
    gr = Grupo.query.get(id)
    if gr:
        res.append({
                'id': gr.id,
                'nombre': gr.nombre
                })
    else:
        res = [{'messaje':'no :v'}]
    return jsonify(res)


@denuncia.route('/api/grupo', methods=['POST'])
def addgroup():
    json_args = request.get_json()
    nombre = json_args['nombre'] if 'nombre' in request.json else None
    
    try:
        gr = Grupo(nombre)
        db.session.add(gr)
        db.session.commit()
    except:
        db.session.rollback()
    return jsonify({'message': 'insert ok :v'})

#@usuario%

@denuncia.route('/api/user',methods=['GET'])
def returnAll():
    res = []
    users = User.query.all()
    if users:
        for usr in users:
            res.append({
                'id': usr.id,
                'ci': usr.ci,
                'nombres': usr.nombres,
                'telefono': usr.telefono,
                'username': usr.username,
                'password': usr.password,
                'grupo': usr.grupo
                })
    else:
        res = [{'messaje':'no :v'}]
    return jsonify(res)

@denuncia.route('/api/user/<string:id>', methods=['GET'])
def getXid(id = None):
    res = []
    usr = User.query.get(id)
    if usr:
        res.append({
                'id': usr.id,
                'ci': usr.ci,
                'nombres': usr.nombres,
                'telefono': usr.telefono,
                'username': usr.username,
                'password': usr.password,
                'grupo': usr.grupo
                })
    else:
        res = [{'messaje':'no :v'}]
    return jsonify(res)

@denuncia.route('/api/user', methods=['POST'])
def add():
    json_args = request.get_json()
    ci = json_args['ci'] if 'ci' in request.json else None
    nombres = json_args['nombres'] if 'nombres' in request.json else None
    telefono = json_args['telefono'] if 'telefono' in request.json else None
    username = json_args['username'] if 'username' in request.json else None
    password = json_args['password'] if 'password' in request.json else None
    grupo = json_args['grupo'] if 'grupo' in request.json else None
    
    try:
        usr = User(ci, nombres, telefono, username, password, grupo)
        db.session.add(usr)
        db.session.commit()
    except:
        db.session.rollback()
    return jsonify({'message': 'insert ok :v'})

#@denuncia%

@denuncia.route('/api/denuncia',methods=['GET'])
def returnAlldnnc():
    res = []
    dnncs = Denuncia.query.all()
    if dnncs:
        for dnnc in dnncs:
            res.append({
                'id': dnnc.id,
                'tipo': dnnc.tipo,
                'foto': dnnc.foto,
                'descripcion': dnnc.descripcion,
                'lat': dnnc.lat,
                'lon': dnnc.lon,
                'user': dnnc.user
                })
    else:
        res = [{'messaje':'no :v'}]
    return jsonify(res)

@denuncia.route('/api/denuncia', methods=['POST'])
def addDnnc():
    json_args = request.get_json()
    tipo = json_args['tipo'] if 'tipo' in request.json else None
    foto = json_args['foto'] if 'foto' in request.json else None
    descripcion = json_args['descripcion'] if 'descripcion' in request.json else None
    lat = json_args['lat'] if 'lat' in request.json else None
    lon = json_args['lon'] if 'lon' in request.json else None
    user = json_args['user'] if 'user' in request.json else None
    
    try:
        dnnc = Denuncia(tipo, foto, descripcion, lat, lon, user)
        db.session.add(dnnc)
        db.session.commit()
    except:
        db.session.rollback()
    return jsonify({'message': 'insert ok :v'})


#@image%

@denuncia.route('/api/image/<string:id>', methods=['GET'])
def getImaXdnnc(id = None):
    res = []
    images = Image.query.filter_by(denuncia = id) 
    if images:
        for ima in images:
            res.append({
                    'id': ima.id,
                    'namefile': ima.namefile
                    })
    else:
        res = [{'messaje':'no :v'}]
    return jsonify(res)

@denuncia.route('/api/image', methods=['POST'])
def addImage():
    json_args = request.get_json()
    namefile = json_args['namefile'] if 'namefile' in request.json else None
    
    try:
        ima = User(namefile)
        db.session.add(ima)
        db.session.commit()
    except:
        db.session.rollback()
    return jsonify({'message': 'insert ok :v'})

#@formulario% ojo

@denuncia.route('/api/form/<string:id>', methods=['GET'])
def getXidform(id = None):
    res = []
    frm = Formulario.query.filter_by(user = id) 
    if frm:
        res.append({
                'id': usr.id,
                'user': usr.user
                })
    else:
        res = [{'messaje':'no :v'}]
    return jsonify(res)

@denuncia.route('/api/form', methods=['POST'])
def addForm():
    json_args = request.get_json()
    user = json_args['user'] if 'user' in request.json else None
    
    try:
        frm = Formulario(user)
        db.session.add(frm)
        db.session.commit()
    except:
        db.session.rollback()
    return jsonify({'message': 'insert ok :v'})


#@predio%
'''@denuncia.route('/api/ubi/<string:id>', methods=['GET'])
def returnAllubi():
    res = []
    ubis = Ubicacion.query.filter_by(denuncia = id) 
    if ubis:
        for ub in ubis:
            res.append({
                'id': ub.id,
                'name': usr.name,
                'lat': usr.lat,
                'lon': usr.lon
                })
    else:
        res = [{'messaje':'no :v'}]
    return jsonify(res)


@denuncia.route('/api/form', methods=['POST'])
def addForm():
    json_args = request.get_json()
    user = json_args['user'] if 'user' in request.json else None
    
    try:
        frm = Formulario(user)
        db.session.add(frm)
        db.session.commit()
    except:
        db.session.rollback()
    return jsonify({'message': 'insert ok :v'})

'''
#@criadero%
#@glosario%
#@centrosalud%
