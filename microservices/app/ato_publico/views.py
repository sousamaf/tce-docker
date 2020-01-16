# https://code.tutsplus.com/pt/tutorials/building-restful-apis-with-flask-diy--cms-26625
import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from app import db, app
from app.ato_publico.empenho import Empenho

ato = Blueprint('empenho', __name__)

@ato.route('/')
@ato.route('/inicio')

def inicio():
    return "Bem-vindo,"

class EmpenhoView(MethodView):
    def get(self, id=None, page=1):
        empenhos = Empenho.query.paginate(page, 10).items
        res = {}
        for empenho in empenhos:
            continue