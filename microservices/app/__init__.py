from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
 
from app.ato_publico.empenho import Empenho
app.register_blueprint(Empenho)
 
db.create_all()