import logging

from flask import request
from flask_restplus import Resource
from endpoints.api_config import api
from serializers import materia_prima
from business import MateriaPrimaRepository

log = logging.getLogger(__name__)
ns = api.namespace('materia_prima', description='Serviços relacionados a Matéria Prima')

@ns.route('/')
class MateriaPrimaServiceList(Resource):

    @api.marshal_list_with(materia_prima)
    def get(self):
        '''
           :return: lista de Matérias Primas
        '''
        _materia = MateriaPrimaRepository()
        return _materia.lista_materia_primas()

    @api.response(201, 'Matéria prima criada com sucesso!')
    @api.expect(materia_prima)
    def post(self):
        '''
            Cria nova matéria prima
        '''
        dados = request.json
        _materia = MateriaPrimaRepository()
        _materia.nova_materia_prima(dados)
        return None, 201

@ns.route('/relatorio/<int:quantidade>')
@api.response(404, 'Matérias primas não encontradas para está quantidade!')
class MateriaPrimaReport(Resource):
    @api.marshal_with(materia_prima)
    def get(self, quantidade):
        '''
        :param quantidade:
        :return: List of MateriaPrima
        '''
        _materia = MateriaPrimaRepository()
        return _materia.get_lista_materias_por_quantidade(quantidade)


@ns.route('/<int:id>')
@api.response(404, 'Matéria Prima não encontrada!')
class MateriaPrimaService(Resource):

    @api.marshal_with(materia_prima)
    def get(self, id):
        '''
        :param id_materia_prima:
        :return: MateriaPrima
        '''
        _materia = MateriaPrimaRepository()
        return _materia.get_materia_prima_by_id(id)

    @api.expect(materia_prima)
    @api.response(204, 'Matéria prima atualizada com sucesso!')
    def put(self, id):
        ''' Atualiza os dados da matéria prima. Utilize este método para atualizar os dados desta objeto'''

        dados = request.json
        _materia = MateriaPrimaRepository()
        _materia.atualiza_materia_prima(id, dados)
        return None, 204

    @api.response(204, 'Matéria Prima excluída com sucesso!')
    def delete(self, id):
        ''' Exlcui Matéria Prima '''
        _materia_prima = MateriaPrimaRepository()
        _materia_prima.deleta_materia_prima(id)
        return None, 204