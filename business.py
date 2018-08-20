from flask import json
from persistence import db
from persistence.models import Funcionario, MateriaPrima, Produto
import logging

log = logging.getLogger(__name__)
''''
model responsável por controlar a persistencia e lógica da api
'''

class FuncionarioRepository:

    def novo_funcionario(self, dados):
        nome = dados.get('nome')
        jornada_trabalho = dados.get('jornada_trabalho')
        funcionario = Funcionario(nome, jornada_trabalho)
        db.session.add(funcionario)
        db.session.commit()
        return funcionario

    def lista_funcionarios(self):
        return Funcionario.query.all()

    def atualiza_funcionario(self, id_funcionario, dados):
        funcionario = self.get_funcionario_by_id(id_funcionario)
        funcionario.nome = dados.get('nome')
        funcionario.jornada_trabalho = dados.get('jornada_trabalho')
        db.session.add(funcionario)
        db.session.commit()
        return funcionario

    def deleta_funcionario(self, id_funcionario):
        funcionario = self.get_funcionario_by_id(id_funcionario)
        db.session.delete(funcionario)
        db.session.commit()

    def get_funcionario_by_id(self, id_funcionario):
        return Funcionario.query.filter(Funcionario.id == id_funcionario).one()

    def get_funcionario_by_nome(self, nome):
        return Funcionario.query.filter(Funcionario.nome == nome).one()


class MateriaPrimaRepository:

    def nova_materia_prima(self, dados):
        nome = dados.get('nome')
        quantidade = dados.get('quantidade')
        _materia_prima = MateriaPrima(nome, quantidade)
        db.session.add(_materia_prima)
        db.session.commit()
        return _materia_prima

    def lista_materia_primas(self):
        return MateriaPrima.query.all()

    def atualiza_materia_prima(self, id_materia_prima, dados):
        materia_prima = self.get_materia_prima_by_id(id_materia_prima)
        materia_prima.nome = dados.get('nome')
        materia_prima.quantidade = dados.get('quantidade')
        db.session.add(materia_prima)
        db.session.commit()

    def deleta_materia_prima(self, id_materia_prima):
        materia_prima = self.get_materia_prima_by_id(id_materia_prima)
        db.session.delete(materia_prima)
        db.session.commit()

    def get_materia_prima_by_id(self, id_materia_prima):
        return db.session.query(MateriaPrima).filter(MateriaPrima.id == id_materia_prima).one()

    def get_lista_materias_por_quantidade(self, quantidade):
        return db.session.query(MateriaPrima).filter(MateriaPrima.quantidade < quantidade).all()

    def get_materia_prima_by_nome(self, nome):
        return db.session.query(MateriaPrima).filter(MateriaPrima.nome == nome).one()

class ProdutoRepository:

    def novo_produto(self, dados):
        return self._create_or_update(dados)


    def lista_produtos(self):
        return Produto.query.all()

    def atualiza_produto(self, id_produto, dados):
        return self._create_or_update(dados, id_produto)


    def _create_or_update(self, dados, id_produto=None):
        nome = dados.get('nome')
        id_funcionario = dados.get('id_funcionario')
        mat_primas = dados.get('materias_primas')
        materia_prima_list = []

        for dic in mat_primas:
            _materia = MateriaPrimaRepository().get_materia_prima_by_id(dic['id'])
            materia_prima_list.append(_materia)

        if id_produto is not None:
            _produto = self.get_produto_by_id(id_produto)
            _produto.id_funcionario = id_funcionario
            _produto.nome = nome
            _produto.materias_primas.append(materia_prima_list)
        else:
            _produto = Produto(nome, id_funcionario, materia_prima_list)

        db.session.add(_produto)
        db.session.commit()
        return _produto.id

    def deleta_produto(self, id_produto):
        produto = self.get_produto_by_id(id_produto)
        db.session.delete(produto)
        db.session.commit()

    def get_produto_by_id(self, id_produto):
        return db.session.query(Produto).filter(Produto.id == id_produto).one()

    def list_produtos_by_nome_funcionario(self, nome_funcionario):
        _funcionario = FuncionarioRepository().get_funcionario_by_nome(nome_funcionario)
        return db.session.query(Produto).filter(Produto.id_funcionario == _funcionario.id).all()

    def list_produtos_by_materia_prima(self, nome_materia_prima):
        _mat_prima = MateriaPrimaRepository().get_materia_prima_by_nome(nome_materia_prima)
        return db.session.query(Produto).join(MateriaPrima).filter(MateriaPrima.id == _mat_prima.id).all()






