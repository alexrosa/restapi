import logging.config
import os
import settings
from endpoints.funcionario import ns as funcionario_namespace
from endpoints.materia_prima import ns as materia_prima_namespace
from endpoints.produto import ns as produto_namespace
from flask import Flask, Blueprint
from persistence import db
from endpoints.api_config import api


app = Flask(__name__)
'''Configurações de logging'''
logging_conf_path = os.path.normcase(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)

def config_app(flask_app):
    '''Configurando a aplicação'''
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDADE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

def start_app(flask_app):
    '''Inicialização da API'''
    config_app(flask_app)

    bprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(bprint)
    '''Adiciona a configuração dos name spaces'''
    api.add_namespace(funcionario_namespace)
    api.add_namespace(materia_prima_namespace)
    api.add_namespace(produto_namespace)

    flask_app.register_blueprint(bprint)
    ''' inicializa o banco de dados '''
    db.init_app(flask_app)

    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    start_app(app)
    log.info('==== Iniciando api ====')
    app.run(debug=settings.FLASK_DEBUG)
