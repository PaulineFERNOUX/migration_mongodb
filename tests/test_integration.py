import pytest
import pandas as pd
import os

def test_simple_workflow(test_collection):
    """Test simple du workflow : CSV -> MongoDB"""
    # 1. Vérifier que le CSV existe
    csv_path = "data/healthcare_dataset.csv"
    assert os.path.exists(csv_path), "Le fichier CSV doit exister"
    
    # 2. Charger le CSV
    df = pd.read_csv(csv_path)
    assert len(df) > 0, "Le CSV ne doit pas être vide"
    
    # 3. Prendre seulement 3 lignes pour le test
    df_sample = df.head(3)
    
    # 4. Convertir en documents MongoDB
    documents = df_sample.to_dict('records')
    
    # 5. Vider la collection de test
    test_collection.delete_many({})
    
    # 6. Insérer les documents
    result = test_collection.insert_many(documents)
    assert len(result.inserted_ids) == 3
    
    # 7. Vérifier que les documents sont bien insérés
    assert test_collection.count_documents({}) == 3
    
    # 8. Vérifier qu'un document a les bons champs
    sample_doc = test_collection.find_one()
    assert "Name" in sample_doc
    assert "Age" in sample_doc

def test_simple_queries(test_collection):
    """Test de requêtes simples"""
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