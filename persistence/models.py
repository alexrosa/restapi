from datetime import datetime
from persistence import db

class Funcionario(db.Model):
    __tablename__="funcionario"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    jornada_trabalho = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, nome, jornada_trabalho):
        self.nome = nome
        self.jornada_trabalho = jornada_trabalho

    def __rper__(self):
        return '<Funcionario %r>' % self.nome

class MateriaPrima(db.Model):
    __tablename__ = "materia_prima"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    quantidade = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime.utcnow())
    id_produto = db.Column(db.ForeignKey('produto.id'))

    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def __repr__(self):
        return '<MateriaPrima %r>' % self.nome


class Produto(db.Model):
    __tablename__ = "produto"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    created = db.Column(db.DateTime, default=datetime.utcnow())
    id_funcionario = db.Column(db.Integer, db.ForeignKey(Funcionario.id))
    materias_primas = db.relationship(MateriaPrima, cascade="all, delete-orphan")

    def __init__(self, nome, id_funcionario, materias_primas):
        self.nome = nome
        self.id_funcionario = id_funcionario
        self.materias_primas.extend(materias_primas)

    def __rper__(self):
        return '<Produto %r>' % self.nome


class ProdutoMateriaPrima(db.Model):
    __tablename__ = "produto_materia_prima"
    id_produto = db.Column(db.Integer, db.ForeignKey(Produto.id), primary_key=True)
    id_materia_prima = db.Column(db.Integer, db.ForeignKey(MateriaPrima.id))

    def __init__(self, id_produto, id_materia_prima):
        self.id_produto = id_produto
        self.id_materia_prima = id_materia_prima

    def __rper__(self):
        return '<ProdutoMateriaPrima %r' % self.id_produto
