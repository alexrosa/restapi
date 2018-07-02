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

    def lista_funcionarios(self):
        return Funcionario.query.all()

    def atualiza_funcionario(self, id_funcionario, dados):
        funcionario = self.get_funcionario_by_id(id_funcionario)
        funcionario.nome = dados.get('nome')
        funcionario.jornada_trabalho = dados.get('jornada_trabalho')
        db.session.add(funcionario)
        db.session.commit()

    def deleta_funcionario(self, id_funcionario):
        funcionario = self.get_funcionario_by_id(id_funcionario)
        db.session.delete(funcionario)
        db.session.commit()

    def get_funcionario_by_id(self, id_funcionario):
        return Funcionario.query.filter(Funcionario.id == id_funcionario).one()


class MateriaPrimaRepository:

    def nova_materia_prima(self, dados):
        nome = dados.get('nome')
        quantidade = dados.get('quantidade')
        _materia_prima = MateriaPrima(nome, quantidade)
        db.session.add(_materia_prima)
        db.session.commit()

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
        log.info("id_materia_prima ===> "+str(id_materia_prima))
        return db.session.query(MateriaPrima).filter(MateriaPrima.id == id_materia_prima).one()

    def get_lista_materias_por_quantidade(self, quantidade):
        return db.session.query(MateriaPrima).filter(MateriaPrima.quantidade < quantidade).all()


class ProdutoRepository:

    def novo_produto(self, dados):
        nome = dados.get('nome')
        id_funcionario = dados.get('id_funcionario')
        materias_primas = dados.get('materias_primas')

        produto = Produto(nome, id_funcionario, materias_primas)

        db.session.add(produto)
        db.session.commit()

    def lista_produtos(self):
        return Produto.query.all()

    def atualiza_produto(self, id_produto, dados):
        nome = dados.get('nome')
        id_funcionario = dados.get('id_funcionario')
        materias_primas = dados.get('materias_primas')

        produto = self.get_produto_by_id(id_produto)
        produto.id_funcionario = id_funcionario
        produto.nome = nome
        produto.materias_primas = materias_primas

        db.session.add(produto)
        db.session.commit()
        return produto

    def deleta_produto(self, id_produto):
        produto = self.get_produto_by_id(id_produto)
        db.session.delete(produto)
        db.session.commit()

    def get_produto_by_id(self, id_produto):
        return Produto.query.filter(Produto.id == id_produto)





