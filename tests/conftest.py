import pytest
from pymongo import MongoClient
import os

@pytest.fixture(scope="session")
def mongodb_uri():
    """URI de connexion MongoDB pour les tests"""
    # Utilise l'URI locale avec authentification
    return os.getenv('MONGODB_URI', 'mongodb://admin_user:admin_password_2025@mongodb:27017/healthcare')

@pytest.fixture(scope="session")
def mongodb_client(mongodb_uri):
    """Client MongoDB pour les tests"""
    client = MongoClient(mongodb_uri)
    yield client
    client.close()

@pytest.fixture(scope="function")
def test_database(mongodb_client):
    """Base de données de test (créée et supprimée pour chaque test)"""
    db_name = "test_healthcare"
    db = mongodb_client[db_name]
    yield db
    # Nettoyage après chaque test
    mongodb_client.drop_database(db_name)

@pytest.fixture(scope="function")
def test_collection(test_database):
    """Collection de test"""
    return test_database["test_admission_data"]
