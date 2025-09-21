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

def test_date_conversion():
    """Test de conversion des dates"""
    df = pd.read_csv("data/healthcare_dataset.csv")
    
    # Test avant conversion
    assert df['Date of Admission'].dtype == 'object'
    
    # Conversion
    df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
    df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])
    
    # Test après conversion
    assert df['Date of Admission'].dtype == 'datetime64[ns]'
    assert df['Discharge Date'].dtype == 'datetime64[ns]'

def test_complete_migration_workflow(test_collection):
    """Test complet du workflow : CSV -> MongoDB"""
    # 1. Charger le CSV (déjà testé par test_csv_loading)
    df = pd.read_csv("data/healthcare_dataset.csv")
    
    # 2. Prendre seulement 3 lignes pour le test
    df_sample = df.head(3)
    
    # 3. Convertir en documents MongoDB
    documents = df_sample.to_dict('records')
    
    # 4. Vider la collection de test
    test_collection.delete_many({})
    
    # 5. Insérer les documents
    result = test_collection.insert_many(documents)
    assert len(result.inserted_ids) == 3
    
    # 6. Vérifier que les documents sont bien insérés
    assert test_collection.count_documents({}) == 3
    
    # 7. Vérifier qu'un document a les bons champs
    sample_doc = test_collection.find_one()
    assert "Name" in sample_doc
    assert "Age" in sample_doc

def test_queries_after_migration(test_collection):
    """Test de requêtes après migration"""
    # Insérer quelques patients de test
    patients = [
        {"Name": "Alice", "Age": 25},
        {"Name": "Bob", "Age": 30},
        {"Name": "Charlie", "Age": 35}
    ]
    test_collection.insert_many(patients)
    
    # Test de recherche simple
    alice = test_collection.find_one({"Name": "Alice"})
    assert alice is not None
    assert alice["Age"] == 25
    
    # Test de recherche avec filtre
    adults = list(test_collection.find({"Age": {"$gte": 30}}))
    assert len(adults) == 2

def test_simple_migration(test_collection):
    """Test simple de migration avec données de test"""
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