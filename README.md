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

## Structure du projet
mongodb_project/
├── data/
│ └── healthcare_dataset.csv # Dataset source (55k+ patients)
├── scripts/
│ ├── quickstart.py # Création de la base MongoDB
│ ├── crud_operations.py # Tests des opérations CRUD
│ ├── analysis_csv_data.py # Analyse du fichier CSV
│ ├── migration.py # Migration CSV → MongoDB
│ └── compare_csv_mongodb.py # Comparaison CSV vs MongoDB
├── src/
│ └── mongodb_project/
└── tests/

## Étapes du projet

### Étape 1 : Configuration de MongoDB Atlas

**Script :** `scripts/quickstart.py`

Cette étape initialise la base de données MongoDB Atlas et teste la connexion en insérant un patient de test.

```bash
poetry run python scripts/quickstart.py
```

**Ce qui se passe :**
- Connexion à MongoDB Atlas
- Création de la base `healthcare`
- Création de la collection `admission_data`
- Insertion d'un patient de test (Bobby Jackson)
- Vérification de l'insertion

**Résultat attendu :** Affichage du document inséré avec toutes ses propriétés.

### Étape 2 : Tests des opérations CRUD

**Script :** `scripts/crud_operations.py`

Cette étape valide que toutes les opérations de base fonctionnent correctement.

```bash
poetry run python scripts/crud_operations.py
```

**Opérations testées :**
- **CREATE** : Insertion de plusieurs patients
- **READ** : Recherche d'un patient spécifique
- **UPDATE** : Modification de l'âge d'un patient
- **DELETE** : Suppression d'un patient

**Résultat attendu :** Confirmation que toutes les opérations CRUD fonctionnent.

### Étape 3 : Analyse du fichier CSV

**Script :** `scripts/analysis_csv_data.py`

Cette étape analyse le fichier source pour comprendre la structure des données et identifier les problèmes potentiels.

```bash
poetry run python scripts/analysis_csv_data.py
```

**Analyses effectuées :**
- **Structure** : Nombre de lignes, colonnes, types de données
- **Valeurs manquantes** : Identification des colonnes avec des données manquantes
- **Âges** : Min, max
- **Genres** : Valeurs uniques présentes
- **Groupes sanguins** : Valeurs uniques présentes

### Étape 4 : Migration des données

**Script :** `scripts/migration.py`

Cette étape migre toutes les données du CSV vers MongoDB.

```bash
poetry run python scripts/migration.py
```

**Processus de migration :**
- Chargement du fichier CSV (55k+ patients)
- Conversion des dates au format datetime
- Transformation en documents MongoDB
- Suppression des données existantes
- Insertion par lots pour optimiser les performances

**Résultat attendu :** Confirmation de l'insertion de tous les documents.

### Étape 5 : Comparaison et validation

**Script :** `scripts/compare_csv_mongodb.py`

Cette étape finale compare les données source (CSV) avec les données migrées (MongoDB) pour s'assurer de l'intégrité.

```bash
poetry run python scripts/compare_csv_mongodb.py
```

**Comparaisons effectuées :**
- **Nombre de documents** : CSV vs MongoDB
- **Âges** : Min/max identiques
- **Échantillon de noms** : Vérification de la cohérence

**Résultat attendu :** Toutes les comparaisons doivent être identiques.

## Données traitées

Le dataset contient des informations sur **55,000+ patients hospitaliers** avec les champs suivants :

- **Identité** : Name, Age, Gender
- **Médical** : Blood Type, Medical Condition, Medication, Test Results
- **Hospitalisation** : Date of Admission, Discharge Date, Admission Type
- **Administratif** : Doctor, Hospital, Insurance Provider, Billing Amount, Room Number

## Tests d'intégrité

Le projet implémente plusieurs niveaux de validation :

1. **Validation de structure** : Vérification des champs requis
2. **Validation de types** : Contrôle des types de données
3. **Validation de cohérence** : Vérification des règles métier
4. **Validation de complétude** : Détection des valeurs manquantes
5. **Validation de migration** : Comparaison avant/après

## Gestion des erreurs

Chaque script inclut :
- Gestion des exceptions
- Messages d'erreur explicites
- Fermeture propre des connexions
- Validation des données avant insertion


## Configuration

### Prérequis
```bash
# Installation des dépendances
poetry install

```

### Variables d'environnement
Les scripts utilisent une URI MongoDB Atlas hardcodée. Pour la production, utilisez des variables d'environnement :

```python
import os
URI = os.getenv("MONGODB_URI", "votre_uri_par_défaut")
```

## Résultats attendus

### Après l'exécution complète :
- Base de données `healthcare` créée
- Collection `admission_data` avec 55k+ documents
- Toutes les opérations CRUD fonctionnelles
- Intégrité des données validée
- Migration réussie sans perte de données

## Objectifs pédagogiques

Ce projet démontre :
- La migration de données relationnelles vers NoSQL
- Les tests d'intégrité des données
- La gestion des erreurs en Python
- L'utilisation de MongoDB Atlas
- Les bonnes pratiques de migration de données

---

**Auteur :** Pauline  
**Formation :** Projet 5 - MongoDB  
**Date :** 2025