import pytest

def test_mongodb_connection(mongodb_client):
    """Test simple de connexion à MongoDB"""
    # Test ping - vérifie que MongoDB répond
    result = mongodb_client.admin.command('ping')
    assert result['ok'] == 1

def test_database_creation(test_database):
    """Test de création de base de données"""
    assert test_database.name == "test_healthcare"

def test_collection_creation(test_collection):
    """Test de création de collection"""
    assert test_collection.name == "test_admission_data"
