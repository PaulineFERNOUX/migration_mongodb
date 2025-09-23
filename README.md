# Projet MongoDB - Migration de Données Médicales

Migration automatisée de données médicales d'un fichier CSV vers MongoDB avec Docker, authentification et système de rôles.

## Architecture

Ce projet utilise une architecture modulaire avec configuration externalisée pour faciliter la maintenance et le déploiement.

## Technologies utilisées

- **Python 3.12+** - Langage principal
- **MongoDB 7.0** - Base de données NoSQL
- **Docker & Docker Compose** - Conteneurisation
- **PyMongo 4.14+** - Driver MongoDB Python
- **Pandas 2.3+** - Traitement de données CSV
- **Poetry** - Gestionnaire de dépendances
- **pytest 8.4+** - Framework de tests

## Structure du projet

```
mongodb_project/
├── config/                          # Configuration centralisée
│   ├── __init__.py                   # Module Python
│   └── auth_config.py                # Configuration auth, rôles, messages
├── data/
│   ├── healthcare_dataset.csv       # Dataset source (55k+ patients)
│   └── test_healthcare_data.csv     # Dataset de test (5 patients)
├── scripts/
│   ├── migration.py                 # Migration CSV → MongoDB
│   └── init_auth.py                 # Refactorisé
├── tests/
│   ├── __init__.py
│   ├── conftest.py                  # Configuration tests (DB séparée)
│   ├── test_01_migration_csv_test.py # Tests avec CSV de test
│   └── test_02_migration.py         # Tests complets de migration
├── docker-compose.yml               # Variables d'environnement unifiées
├── Dockerfile                       # Image Docker
├── pyproject.toml                   # Configuration Poetry
├── poetry.lock                      # Verrouillage des dépendances
└── README.md                        # Ce fichier
```

## Objectifs du projet

1. **Migration automatisée** : CSV → MongoDB via Docker
2. **Sécurité** : Système d'authentification et de rôles
3. **Scalabilité** : Architecture conteneurisée
4. **Maintenabilité** : Configuration externalisée
5. **Qualité** : Tests automatisés complets

## Système d'authentification

### Rôles configurés

| Rôle | Utilisateur | Mot de passe | Permissions |
|------|-------------|--------------|-------------|
| **Analyste** | `analyst_user` | `analyst_password_2025` | Lecture seule sur `admission_data` |
| **Administrateur** | `admin_user` | `admin_password_2025` | Tous droits + gestion DB |
| **Root** | `root` | `example` | Super administrateur MongoDB |

### Bases de données

- **Production** : `healthcare` (collection: `admission_data`)
- **Tests** : `healthcare_test` (collection: `test_admission_data`)

## Utilisation avec Docker

### Démarrage complet
```bash
# Cloner le projet
git clone <repo-url>
cd mongodb_project

# Démarrer tous les services (MongoDB + Migration + Tests)
docker-compose up

# Ou en arrière-plan
docker-compose up -d
```

### Services Docker

1. **mongodb** : Base de données MongoDB 7.0
2. **init-auth** : Initialisation rôles et utilisateurs  
3. **test** : Exécution des tests automatisés
4. **migration** : Migration des données CSV

### Tests uniquement
```bash
# Tests locaux (nécessite MongoDB running)
poetry install
poetry run pytest tests/ -v

# Tests via Docker
docker-compose run test
```

## Configuration

### Variables d'environnement

| Variable | Défaut | Description |
|----------|--------|-------------|
| `MONGODB_URI` | `mongodb://root:example@mongodb:27017/admin` | URI de connexion MongoDB |

### Personnalisation

Modifiez `config/auth_config.py` pour :
- Changer les utilisateurs et mots de passe
- Modifier les permissions des rôles
- Adapter les messages de l'application
- Configurer les bases de données

## Schéma de base de données

### Collection : `admission_data`

```javascript
{
  "_id": ObjectId("..."),
  "Name": "John Doe",
  "Age": 45,
  "Gender": "Male",
  "Blood Type": "O+", 
  "Medical Condition": "Diabetes",
  "Date of Admission": ISODate("2023-01-15"),
  "Doctor": "Dr. Smith",
  "Hospital": "General Hospital",
  "Insurance Provider": "HealthCare Inc",
  "Billing Amount": 15000,
  "Room Number": 101,
  "Admission Type": "Emergency",
  "Discharge Date": ISODate("2023-01-20"),
  "Medication": "Insulin",
  "Test Results": "Normal"
}
```

##Tests

Le projet inclut des tests complets :

### Types de tests
- **test_01_migration_csv_test.py** : Tests avec petit dataset
- **test_02_migration.py** : Tests complets de migration
- **conftest.py** : Configuration et fixtures

### Exécution
```bash
# Tous les tests
poetry run pytest tests/ -v

# Test spécifique
poetry run pytest tests/test_01_migration_csv_test.py -v

# Avec couverture
poetry run pytest tests/ --cov=scripts
```

## Vérification 

### Connexion MongoDB
```bash
# Via Docker
docker exec -it mongodb_project-mongodb-1 mongosh "mongodb://root:example@localhost:27017/admin"

# Utiliser la base healthcare
use healthcare

# Vérifier les données
db.admission_data.countDocuments()
db.admission_data.find().limit(3)

# Vérifier les utilisateurs
db.runCommand({usersInfo: "analyst_user", showPrivileges: true})
db.runCommand({usersInfo: "admin_user", showPrivileges: true})
```

### Test d'authentification
```bash
# Connexion analyste (lecture seule)
mongosh "mongodb://analyst_user:analyst_password_2025@localhost:27017/healthcare"

# Connexion admin (tous droits)  
mongosh "mongodb://admin_user:admin_password_2025@localhost:27017/healthcare"
```

## Développement

### Prérequis
- Python 3.12+
- Docker & Docker Compose
- Poetry



**Auteur :** Pauline  
**Formation :** Data Engineer - Projet 5  
**Context :** Migration MongoDB avec Docker  
**Date :** 2025


