# Projet MongoDB - Migration de Données Médicales

Migration de données médicales d'un fichier CSV vers MongoDB avec Docker et authentification.

## Technologies utilisées

- **Python 3.12+**
- **MongoDB** (Docker)
- **PyMongo** (driver MongoDB)
- **Pandas** (traitement CSV)
- **Poetry** (dépendances)
- **pytest** (tests)

## Structure du projet

mongodb_project/
├── data/
│   ├── healthcare_dataset.csv      # Dataset source (55k+ patients)
│   └── test_healthcare_data.csv    # Dataset de test (5 patients)
├── scripts/
│   ├── migration.py                # Migration CSV → MongoDB
│   └── init_auth.py                # Configuration authentification
├── tests/
│   ├── conftest.py                 # Configuration des tests
│   ├── test_migration.py           # Tests de migration
│   └── test_migration_csv_test.py  # Tests avec CSV de test
├── docker-compose.yml              # Configuration Docker
├── Dockerfile                      # Image Docker
├── pyproject.toml                  # Configuration Poetry
├── poetry.lock                     # Verrouillage des dépendances
└── README.md                       # Ce fichier


## Objectif

Migration de données médicales CSV vers MongoDB avec Docker et système d'authentification.

## Authentification

- **Analyste** : `analyst_user` / `analyst_password_2025` (lecture seule)
- **Admin** : `admin_user` / `admin_password_2025` (tous droits)

## Utilisation

### Démarrage
```bash
# Démarrer MongoDB et migration
docker-compose up

# Tests
python -m pytest tests/
```

### Vérification
```bash
# Se connecter à MongoDB
docker exec -it mongodb_project-mongodb-1 mongosh "mongodb://root:example@localhost:27017/admin"
use healthcare
db.admission_data.find().limit(5)

db.runCommand({usersInfo: "analyst_user", showPrivileges: true})
```

**Auteur :** Pauline  
**Formation :** Projet 5 - MongoDB