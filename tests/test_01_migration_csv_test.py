import pytest
import pandas as pd
import os

def test_csv_exists():
    """Test que le fichier CSV de test existe"""
    assert os.path.exists("data/test_healthcare_data.csv")

def test_csv_loading():
    """Test de chargement du CSV de test"""
    df = pd.read_csv("data/test_healthcare_data.csv")
    assert len(df) > 0
    assert "Name" in df.columns

def test_migration_workflow(test_collection):
    """Test simple de migration CSV vers MongoDB"""
    # Charger le CSV
    df = pd.read_csv("data/test_healthcare_data.csv")
    
    # Convertir en documents
    documents = df.to_dict('records')
    
    # Insérer dans MongoDB
    test_collection.delete_many({})
    result = test_collection.insert_many(documents)
    
    # Vérifier
    assert len(result.inserted_ids) == len(documents)
    assert test_collection.count_documents({}) == len(documents)