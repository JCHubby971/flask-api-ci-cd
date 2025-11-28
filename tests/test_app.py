import os
import sys
import pytest

# Ajoute le dossier racine du projet au PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_root_returns_hello(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello CI/CD"}