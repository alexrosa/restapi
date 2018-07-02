import logging

from flask import request
from flask_restplus import Resource
from endpoints.api_config import api
from serializers import funcionario
from business import FuncionarioRepository

log = logging.getLogger(__name__)
ns = api.namespace('funcionario', description='Serviços relacionados ao Funcionario')

@ns.route('/')
class FuncionarioServiceList(Resource):

    @api.marshal_list_with(funcionario)
    def get(self):
        '''
           :return: lista de funcionários
        '''
        func = FuncionarioRepository()
        return func.lista_funcionarios()

    @api.response(201, 'Funcionário criado com sucesso')
    @api.expect(funcionario)
    def post(self):
        '''
            Cria um novo usuário
        '''
        dados = request.json
        func = FuncionarioRepository()
        func.novo_funcionario(dados)
        return None, 201

@ns.route('/<int:id>')
@api.response(404, 'Funcionário não encontrado!')
class FuncionarioService(Resource):

    @api.marshal_with(funcionario)
    def get(self, id):
        '''
        :param id_funcionario:
        :return: Funcionario
        '''
        func = FuncionarioRepository()
        return func.get_funcionario_by_id(id)

    @api.expect(funcionario)
    @api.response(204, 'Funcionário atualizado com sucesso!')
    def put(self, id):
        ''' Atualiza os dados do funcionario. Utilize este método para atualizar os dados do funcionário '''

        dados_funcionario = request.json
        func = FuncionarioRepository()
        func.atualiza_funcionario(id, dados_funcionario)
        return None, 204

    @api.response(204, 'Funcionário excluído com sucesso!')
    def delete(self, id):
        ''' Exlcui funcionario '''
        FuncionarioRepository().deleta_funcionario(id)
        return None, 204