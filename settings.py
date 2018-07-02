# Configurações do Flask
FLASK_SERVER_NAME = 'localhost:5000'
FLASK_DEBUG = True

# Configurações do Flask-Restplus e SwaggerUI
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = False
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# Configurações do SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'sqlite:///db_app.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False
