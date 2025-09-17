# Tests MongoDB

Ce dossier contient les tests pour vérifier le bon fonctionnement de la migration CSV vers MongoDB.

## Installation

```bash
poetry install
```

## Exécution des tests

### Tous les tests
```bash
poetry run pytest
```

### Tests avec détails
```bash
poetry run pytest -v
```

### Un fichier spécifique
```bash
poetry run pytest tests/test_migration.py
```

## Fichiers de test

- `conftest.py` - Configuration partagée (fixtures MongoDB)
- `test_migration.py` - Tests de migration CSV vers MongoDB
- `test_migration_csv_test.py` - Tests avec CSV de test (5 patients)

## Que testent les tests ?

### test_migration.py
- Existence du fichier CSV
- Chargement correct du CSV
- Conversion des dates
- Migration des données vers MongoDB

### test_migration_csv_test.py
- Tests avec données contrôlées (5 patients)
- Vérification de patients spécifiques
- Tests de requêtes variées
- Tests de recherche par dates

## Configuration

Les tests utilisent une base de données de test séparée (`test_healthcare`) qui est automatiquement nettoyée après chaque test.

L'URI de connexion MongoDB est définie dans `conftest.py`.

## En cas de problème

1. Vérifiez que les fichiers CSV existent dans `data/`
2. Vérifiez votre connexion internet
3. Vérifiez l'URI MongoDB dans `conftest.py`
4. Utilisez `poetry run pytest -v` pour plus de détails sur les erreurs