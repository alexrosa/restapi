import logging

from flask import request
from flask_restplus import Resource
from api_config import api
from serializers import produto
from business import ProdutoRepository

log = logging.getLogger(__name__)
ns = api.namespace('produto', description='Serviços relacionados ao Produto')

@ns.route('/')
class ProdutoServiceList(Resource):

    @api.marshal_list_with(produto)
    def get(self):
        ''' lista os produtos '''
        _produto = ProdutoRepository()
        return _produto.lista_produtos()

    @api.response(201, 'Produto criado com sucesso!')
    @api.expect(produto)
    def post(self):
        '''Cria novo produto'''
        dados = request.json
        _produto = ProdutoRepository()
        _produto.novo_produto(dados)
        return _produto, 201

@ns.route('/<int:id>')
@api.response(404, 'Produto não encontrado!')
class MateriaPrimaService(Resource):

    @api.marshal_with(produto)
    def get(self, id):
        ''' :param id_produto:
            :return Produto:
         '''
        return ProdutoRepository().get_produto_by_id(id)

    @api.expect(produto)
    @api.response(204, 'Produto atualizado com sucesso!')
    def put(self, id):
        ''' Atualiza os dados do produto. Utilize este método para atualizar os dados deste objeto'''

        dados = request.json
        _produto = ProdutoRepository()
        produto = _produto.atualiza_produto(id, dados)
        return produto, 204

    @api.response(204, 'Produto excluído com sucesso!')
    def delete(self, id):
        ''' Exlcui Produto  '''
        ProdutoRepository().deleta_produto(id)
        return None, 204