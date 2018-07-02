from flask_restplus import fields
from endpoints.api_config import api

'''
Serializers (JSON) para os objetos do Model 
'''

materia_prima = api.model('MateriaPrima', {
    'id': fields.Integer(readOnly=True, description='Chave única da Matéria Prima'),
    'nome': fields.String(required=True, description='Descreve o nome da máteria prima - Máximo 100 caracteres'),
    'quantidade': fields.Integer(required=True, description='Representa a quantidade de máteria prima disponível')
})

funcionario = api.model('Funcionario', {
    'id': fields.Integer(readOnly=True, description='Chave única do usuário'),
    'nome': fields.String(required=True, description='Nome do usuário - Máximo 100 caracteres'),
    'jornada_trabalho': fields.Integer(required=True, enum=['4', '6', '8'], description='Representa a jornada de trabalho do usuário (4h00, 6h00 e 8h00')
})

produto = api.model('Produto', {
    'id': fields.Integer(readOnly=True, description='Chave única do produto'),
    'nome': fields.String(required=True, description='Nome do produto - Máximo de 100 caracteres'),
    'id_funcionario': fields.Integer(attribute='id_funcionario', description='ID do funcionário'),
    'materias_primas': fields.String(attribute='materia_prima.nome', description='Lista de matérias primas utilizadas no produto')
})