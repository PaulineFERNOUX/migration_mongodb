"""
Configuration pour l'authentification MongoDB
Contient toutes les données statiques pour les rôles, utilisateurs et connexion
"""
import os

# Configuration de connexion MongoDB
MONGODB_CONFIG = {
    "default_uri": f"mongodb://{os.getenv('MONGO_ROOT_USERNAME', 'root')}:{os.getenv('MONGO_ROOT_PASSWORD', 'example')}@mongodb:27017/admin",
    "database_name": os.getenv('MONGO_DATABASE', 'healthcare'),
    "collection_name": os.getenv('MONGO_COLLECTION', 'admission_data')
}

# Configuration des rôles
ROLES_CONFIG = [
    {
        "role": "healthcare_analyst",
        "privileges": [
            {
                "resource": {"db": os.getenv('MONGO_DATABASE', 'healthcare'), "collection": os.getenv('MONGO_COLLECTION', 'admission_data')},
                "actions": ["find"]
            },
            {
                "resource": {"db": os.getenv('MONGO_DATABASE', 'healthcare'), "collection": os.getenv('MONGO_COLLECTION', 'admission_data')},
                "actions": ["listCollections", "listIndexes"]
            }
        ],
        "roles": []
    },
    {
        "role": "healthcare_admin",
        "privileges": [
            {
                "resource": {"db": os.getenv('MONGO_DATABASE', 'healthcare'), "collection": os.getenv('MONGO_COLLECTION', 'admission_data')},
                "actions": ["find", "insert", "update", "remove"]
            },
            {
                "resource": {"db": os.getenv('MONGO_DATABASE', 'healthcare'), "collection": ""},
                "actions": ["listCollections", "listIndexes", "createCollection", "dropCollection", "dropDatabase"]
            }
        ],
        "roles": []
    }
]

# Configuration des utilisateurs
USERS_CONFIG = [
    {
        "user": os.getenv('MONGO_ANALYST_USER', 'analyst_user'),
        "pwd": os.getenv('MONGO_ANALYST_PASSWORD', 'analyst_password_2025'),
        "roles": [{"role": "healthcare_analyst", "db": os.getenv('MONGO_DATABASE', 'healthcare')}]
    },
    {
        "user": os.getenv('MONGO_ADMIN_USER', 'admin_user'),
        "pwd": os.getenv('MONGO_ADMIN_PASSWORD', 'admin_password_2025'), 
        "roles": [
            {"role": "healthcare_admin", "db": os.getenv('MONGO_DATABASE', 'healthcare')},
            {"role": "readWriteAnyDatabase", "db": "admin"}
        ]
    }
]

# Messages de l'application
MESSAGES = {
    "init_start": "Initialisation de l'authentification MongoDB...",
    "creating_roles": "Création des rôles",
    "creating_users": "Création des utilisateurs...",
    "init_success": "Initialisation de l'authentification MongoDB terminée avec succès",
    "role_exists": "Rôle '{role_name}' existe déjà",
    "user_exists": "Utilisateur '{user_name}' existe déjà",
    "role_error": "Erreur création rôle '{role_name}': {error}",
    "user_error": "Erreur création utilisateur '{user_name}': {error}",
    "init_error": "Erreur lors de l'initialisation: {error}"
}