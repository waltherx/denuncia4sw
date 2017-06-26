from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://onfskipauhwatv:1ffb28081815308fc763ebd8187557fe4d1bfe75beb9a59c055e9e47bbf2b32e@ec2-107-21-108-204.compute-1.amazonaws.com:5432/df2dl4os00mlfj'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from my_app.denuncia.controllers import denuncia

app.register_blueprint(denuncia)

db.create_all()