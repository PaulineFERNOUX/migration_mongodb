import pytest

def test_insert_patient(test_collection):
    """Test d'insertion d'un patient"""
    patient = {
        "name": "Test Patient",
        "age": 30,
        "gender": "Male"
    }
    
    result = test_collection.insert_one(patient)
    assert result.inserted_id is not None

def test_find_patient(test_collection):
    """Test de recherche d'un patient"""
    # Insérer un patient de test
    patient = {"name": "John Doe", "age": 25}
    test_collection.insert_one(patient)
    
    # Rechercher le patient
    found = test_collection.find_one({"name": "John Doe"})
    assert found is not None
    assert found["age"] == 25

def test_update_patient(test_collection):
    """Test de mise à jour d'un patient"""
    # Insérer un patient
    patient = {"name": "Jane Doe", "age": 30}
    result = test_collection.insert_one(patient)
    
    # Mettre à jour l'âge
    test_collection.update_one(
        {"_id": result.inserted_id},
        {"$set": {"age": 31}}
    )
    
    # Vérifier la mise à jour
    updated = test_collection.find_one({"_id": result.inserted_id})
    assert updated["age"] == 31

def test_delete_patient(test_collection):
    """Test de suppression d'un patient"""
    # Insérer un patient
    patient = {"name": "Delete Me", "age": 40}
    result = test_collection.insert_one(patient)
    
    # Supprimer le patient
    delete_result = test_collection.delete_one({"_id": result.inserted_id})
    assert delete_result.deleted_count == 1
