# Tests MongoDB - Guide Simple

Ce guide explique comment utiliser les tests de manière simple et accessible.

## 🚀 Installation

```bash
# Installer pytest
poetry add --group dev pytest

# Lancer tous les tests
poetry run pytest
```

## 📁 Fichiers de Test

- `test_connection.py` - Tests de connexion à MongoDB
- `test_crud.py` - Tests des opérations de base (créer, lire, modifier, supprimer)
- `test_migration.py` - Tests de migration CSV vers MongoDB
- `test_data_validation.py` - Tests de validation des données
- `test_integration.py` - Tests d'intégration complets

## 🎯 Commandes Simples

### Lancer tous les tests
```bash
poetry run pytest
```

### Lancer un fichier spécifique
```bash
poetry run pytest tests/test_connection.py
```

### Lancer avec plus de détails
```bash
poetry run pytest -v
```

### Utiliser le script interactif
```bash
python run_tests.py
```

## 📝 Exemple de Test

```python
def test_insert_patient(test_collection):
    """Test d'insertion d'un patient"""
    patient = {
        "name": "Test Patient",
        "age": 30,
        "gender": "Male"
    }
    
    result = test_collection.insert_one(patient)
    assert result.inserted_id is not None
```

## ✅ Que Testent les Tests ?

### Tests de Connexion
- ✅ Connexion à MongoDB
- ✅ Création de base de données
- ✅ Création de collection

### Tests CRUD
- ✅ Insérer un patient
- ✅ Rechercher un patient
- ✅ Modifier un patient
- ✅ Supprimer un patient

### Tests de Migration
- ✅ Le fichier CSV existe
- ✅ Le CSV se charge correctement
- ✅ Les données peuvent être insérées en MongoDB

### Tests de Validation
- ✅ Structure des données
- ✅ Types de données corrects

### Tests d'Intégration
- ✅ Workflow complet CSV → MongoDB
- ✅ Requêtes simples fonctionnent

## 🚨 En Cas de Problème

### Erreur de connexion
- Vérifiez votre connexion internet
- Vérifiez l'URI MongoDB dans `conftest.py`

### Tests qui échouent
- Utilisez `-v` pour plus de détails
- Vérifiez que le fichier CSV existe dans `data/`

### Installation
- Assurez-vous d'avoir fait `poetry install`
- Vérifiez que pytest est installé

## 🎯 Objectif

Ces tests vérifient que votre projet MongoDB fonctionne correctement :
- La connexion à la base de données
- Les opérations de base (CRUD)
- La migration des données CSV
- L'intégrité des données

C'est tout ! Simple et efficace. 🎉
