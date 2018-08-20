import os
import tempfile
import pytest
from app import app as flaskr
from persistence import db

@pytest.fixture
def client():
    db_file, flaskr.config['DATABASE'] = tempfile.mkstemp()
    flaskr.config['TESTING'] = True
    client  = flaskr.test_client()

    with flaskr.app_context():
        db.init_app(flaskr)

    yield client

    os.close(db_file)
    os.unlink(flaskr.config['DATABASE'])

def test_empty_db(client):
    rv = client.get('localhost:5000/api/')
    assert b'No Entries here so far' in rv.data


