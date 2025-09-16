import pytest

def test_patient_data_structure(test_collection):
    """Test simple de la structure des données de patient"""
    patient = {
        "Name": "John Doe",
        "Age": 30,
        "Gender": "Male"
    }
    
    result = test_collection.insert_one(patient)
    assert result.inserted_id is not None
    
    # Vérifier que les champs sont présents
    inserted_doc = test_collection.find_one({"_id": result.inserted_id})
    assert "Name" in inserted_doc
    assert "Age" in inserted_doc
    assert "Gender" in inserted_doc

def test_age_validation(test_collection):
    """Test simple de validation de l'âge (0-120 ans)"""
    # Test avec un âge valide
    patient = {"Name": "Test Patient", "Age": 25}
    result = test_collection.insert_one(patient)
    assert result.inserted_id is not None

def test_gender_validation(test_collection):
    """Test simple de validation du genre"""
    patient = {"Name": "Test Patient", "Gender": "Female"}
    result = test_collection.insert_one(patient)
    assert result.inserted_id is not None

def test_blood_type_validation(test_collection):
    """Test simple de validation du groupe sanguin"""
    # Test avec un groupe sanguin valide
    patient = {
        "Name": "Test Patient", 
        "Age": 30, 
        "Blood Type": "O+"
    }
    result = test_collection.insert_one(patient)
    assert result.inserted_id is not None
    
    # Vérifier que le groupe sanguin a été correctement stocké
    inserted_doc = test_collection.find_one({"_id": result.inserted_id})
    assert inserted_doc["Blood Type"] == "O+"
