import logging

from flask import request
from flask_restplus import Resource
from endpoints.api_config import api
from serializers import produto
from business import ProdutoRepository

log = logging.getLogger(__name__)
ns = api.namespace('produto', description='Serviços relacionados ao Produto')

@ns.route('/')
class ProdutoServiceList(Resource):

    @api.marshal_list_with(produto)
    def get(self):
        ''' Retorna uma lista dos produtos '''
        _produto = ProdutoRepository()
        return _produto.lista_produtos()

    @api.response(201, 'Produto criado com sucesso!')
    @api.expect(produto)
    def post(self):
        '''Cria um novo produto'''
        dados = request.json
        log.info(dados)
        _produto = ProdutoRepository()
        _produto.novo_produto(dados)
        return None, 201

@ns.route('/<int:id>')
@api.response(404, 'Produto não encontrado!')
class ProdutoService(Resource):

    @api.marshal_with(produto)
    def get(self, id):
        ''' Retorna um Produto'''
        return ProdutoRepository().get_produto_by_id(id)

    @api.expect(produto)
    @api.response(204, 'Produto atualizado com sucesso!')
    def put(self, id):
        ''' Atualiza os dados do produto. Utilize este método para atualizar os dados deste objeto'''

        dados = request.json
        _produto = ProdutoRepository()
        _produto.atualiza_produto(id, dados)
        return None, 204

    @api.response(204, 'Produto excluído com sucesso!')
    def delete(self, id):
        ''' Exlcui um Produto  '''
        ProdutoRepository().deleta_produto(id)
        return None, 204

'''=== reports ===='''
@ns.route('/relatorio/funcionario/<string:nome_funcionario>')
@api.response(404, 'Lista os produtos encontrados para um determinado funcionário {id_funcionario}!')
class ProdutoFuncionarioReport(Resource):
    @api.marshal_list_with(produto)
    def get(self, nome_funcionario):
        ''' Retorna uma lista de Produtos Finais pelo Funcionario.nome'''
        return ProdutoRepository().list_produtos_by_nome_funcionario(nome_funcionario)

@ns.route('/relatorio/produto/<string:materia_prima>')
@api.response(404, 'Lista os produtos encontrados para uma determinada Máteria Prima {MateriaPrima.nome}!')
class ProdutoMateriaPrimaReport(Resource):
    @api.marshal_list_with(produto)
    def get(self, materia_prima):
        ''' Retorna uma lista de Produtos Finais pelo MateriaPrima.nome'''
        return ProdutoRepository().list_produtos_by_materia_prima(materia_prima)
