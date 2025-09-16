import pytest
import pandas as pd
import os
from datetime import datetime

def test_test_csv_exists():
    """Test que le fichier CSV de test existe"""
    csv_path = "data/test_healthcare_data.csv"
    assert os.path.exists(csv_path), f"Le fichier {csv_path} n'existe pas"

def test_test_csv_structure():
    """Test de la structure du CSV de test"""
    df = pd.read_csv("data/test_healthcare_data.csv")
    
    # Vérifier le nombre de lignes attendu
    expected_count = 5
    assert len(df) == expected_count, f"Attendu {expected_count} lignes, trouvé {len(df)}"
    
    # Vérifier les colonnes requises
    required_columns = ["Name", "Age", "Gender", "Blood Type", "Medical Condition", 
                       "Date of Admission", "Doctor", "Hospital", "Insurance Provider", 
                       "Billing Amount", "Room Number", "Admission Type", "Discharge Date", 
                       "Medication", "Test Results"]
    
    for column in required_columns:
        assert column in df.columns, f"Colonne '{column}' manquante dans le CSV de test"

def test_test_csv_data_quality():
    """Test de la qualité des données du CSV de test"""
    df = pd.read_csv("data/test_healthcare_data.csv")
    
    # Vérifier qu'il n'y a pas de valeurs nulles dans les champs critiques
    critical_fields = ["Name", "Age", "Gender", "Date of Admission"]
    for field in critical_fields:
        assert not df[field].isnull().any(), f"Valeurs nulles trouvées dans '{field}'"
    
    # Vérifier les types de données
    assert df["Age"].dtype in ["int64", "int32"], "L'âge doit être un entier"

def test_migration_with_test_csv(test_collection):
    """Test de migration avec le CSV de test"""
    # 1. Charger le CSV de test
    df = pd.read_csv("data/test_healthcare_data.csv")
    expected_count = len(df)
    
    # 2. Convertir les dates (comme dans migration.py)
    df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
    df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])
    documents = df.to_dict('records')
    
    # 3. Vider et remplir la collection
    test_collection.delete_many({})
    result = test_collection.insert_many(documents)
    
    # 4. Vérifier l'insertion
    assert len(result.inserted_ids) == expected_count
    assert test_collection.count_documents({}) == expected_count

def test_specific_patients_after_migration(test_collection):
    """Test de patients spécifiques après migration"""
    # Migrer les données de test
    df = pd.read_csv("data/test_healthcare_data.csv")
    df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
    df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])
    
    test_collection.delete_many({})
    test_collection.insert_many(df.to_dict('records'))
    
    # Tester Alice Smith
    alice = test_collection.find_one({"Name": "Alice Smith"})
    assert alice is not None
    assert alice["Age"] == 25
    assert alice["Gender"] == "Female"
    assert alice["Blood Type"] == "O+"
    assert alice["Medical Condition"] == "Fever"
    assert alice["Billing Amount"] == 1500.50
    assert isinstance(alice["Date of Admission"], datetime)

def test_queries_with_test_data(test_collection):
    """Test de requêtes avec les données de test"""
    # Migrer les données
    df = pd.read_csv("data/test_healthcare_data.csv")
    df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
    df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])
    
    test_collection.delete_many({})
    test_collection.insert_many(df.to_dict('records'))
    
    # Test de recherche par âge
    adults = list(test_collection.find({"Age": {"$gte": 30}}))
    assert len(adults) == 4  # Bob(30), Carol(45), David(60), Emma(35)
    
    # Test de recherche par genre
    females = list(test_collection.find({"Gender": "Female"}))
    assert len(females) == 3  # Alice, Carol, Emma
    
    # Test de recherche par type d'admission
    urgent_cases = list(test_collection.find({"Admission Type": "Urgent"}))
    assert len(urgent_cases) == 2  # Alice, Carol
    
    # Test de recherche par groupe sanguin
    o_positive = list(test_collection.find({"Blood Type": "O+"}))
    assert len(o_positive) == 1  # Alice
    
    # Test de recherche par montant de facturation
    expensive_cases = list(test_collection.find({"Billing Amount": {"$gte": 3000}}))
    assert len(expensive_cases) == 3  # Carol(3200), David(8500.25), Emma(4200)

def test_date_queries_with_test_data(test_collection):
    """Test de requêtes sur les dates avec les données de test"""
    # Migrer les données
    df = pd.read_csv("data/test_healthcare_data.csv")
    df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
    df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])
    
    test_collection.delete_many({})
    test_collection.insert_many(df.to_dict('records'))
    
    # Test de recherche par date d'admission
    from datetime import datetime
    jan_17 = datetime(2024, 1, 17)
    patients_jan_17 = list(test_collection.find({"Date of Admission": jan_17}))
    assert len(patients_jan_17) == 1  # Carol Davis
    
    # Test de recherche par période
    jan_16_to_18 = list(test_collection.find({
        "Date of Admission": {
            "$gte": datetime(2024, 1, 16),
            "$lte": datetime(2024, 1, 18)
        }
    }))
    assert len(jan_16_to_18) == 3  # Bob, Carol, David