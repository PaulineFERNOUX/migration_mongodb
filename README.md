# Projet MongoDB - Migration de Données Médicales

Ce projet démontre la migration de données médicales d'un fichier CSV vers MongoDB Atlas, avec des tests d'intégrité complets.

## Vue d'ensemble

Le projet suit une approche méthodique pour migrer des données de patients hospitaliers vers MongoDB, en s'assurant de l'intégrité des données à chaque étape.

## Technologies utilisées

- **Python 3.12+**
- **MongoDB Atlas** (base de données cloud)
- **PyMongo** (driver MongoDB pour Python)
- **Pandas** (traitement des données CSV)
- **Poetry** (gestion des dépendances)
- **pytest** (tests automatisés)

## Structure du projet
mongodb_project/
├── data/
│ └── healthcare_dataset.csv # Dataset source (55k+ patients)
├── scripts/
│ ├── migration.py # Migration CSV → MongoDB
├── src/
│ └── mongodb_project/
├── tests/                  # Tests automatisés
   ├── test_connection.py  # Tests de connexion MongoDB
   ├── test_crud.py        # Tests des opérations CRUD
   ├── test_migration.py   # Tests de migration CSV → MongoDB
   ├── test_data_validation.py # Tests de validation des données
   ├── test_integration.py # Tests d'intégration complets
   └── README.md           # Guide des tests


##Objectif
Migration des données de santé d'un fichier CSV vers MongoDB.

##Utilisation

### Migration
```bash
poetry run python scripts/migration.py
```

### Tests
```bash
poetry run pytest
```

##Structure
- `scripts/migration.py` : Script principal de migration (étapes claires)
- `data/` : Données source (CSV)
- `tests/` : Tests automatisés

##Fichiers d'apprentissage
Les fichiers d'entraînement sont disponibles dans la branche `learning` :
- `scripts/quickstart.py` : Test de connexion
- `scripts/analysis_csv_data.py` : Analyse des données CSV
- `scripts/compare_csv_mongodb.py` : Comparaison CSV vs MongoDB
- `scripts/crud_operations.py` : Opérations CRUD de base

**Auteur :** Pauline  
**Formation :** Projet 5 - MongoDB  
**Date :** 2025