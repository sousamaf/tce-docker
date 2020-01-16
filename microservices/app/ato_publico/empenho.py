from app import db

class Empenho(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    municipio = db.Column(db.String(255), nullable = False)
    descricao = db.Column(db.Text)
    valor = db.Column(db.Float(asdecimal=True))

    def __init__(self, municipio, descricao, valor):
        self.municipio = municipio
        self.descricao = descricao
        self.valor = valor
    
    def __repr__(self):
        return '<Empenho %d>' % self.id