from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def reset_database():
    from persistence.models import Funcionario, MateriaPrima, Produto
    db.drop_all()
    db.create_all()