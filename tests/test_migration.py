import pytest
import pandas as pd
import os

def test_csv_file_exists():
    """Test que le fichier CSV existe"""
    csv_path = "data/healthcare_dataset.csv"
    assert os.path.exists(csv_path), f"Le fichier {csv_path} n'existe pas"

def test_csv_loading():
    """Test de chargement du fichier CSV"""
    csv_path = "data/healthcare_dataset.csv"
    df = pd.read_csv(csv_path)
    
    assert len(df) > 0, "Le fichier CSV est vide"
    assert "Name" in df.columns, "Colonne 'Name' manquante"
    assert "Age" in df.columns, "Colonne 'Age' manquante"

def test_simple_migration(test_collection):
    """Test simple de migration"""
    # Données de test simples
    test_data = {
        "Name": "Test Patient",
        "Age": 30,
        "Gender": "Male"
    }
    
    # Insérer directement
    result = test_collection.insert_one(test_data)
    assert result.inserted_id is not None
    
    # Vérifier que le document existe
    found = test_collection.find_one({"Name": "Test Patient"})
    assert found is not None
    assert found["Age"] == 30
