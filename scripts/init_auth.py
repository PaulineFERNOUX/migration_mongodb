from pymongo import MongoClient
import os
import sys
from config.auth_config import MONGODB_CONFIG, ROLES_CONFIG, USERS_CONFIG, MESSAGES


def get_mongodb_uri():
    """Récupère l'URI MongoDB depuis les variables d'environnement ou utilise la valeur par défaut"""
    return os.getenv('MONGODB_URI', MONGODB_CONFIG["default_uri"])


def create_role(client, role_config):
    """Crée un rôle dans MongoDB"""
    try:
        client[MONGODB_CONFIG["database_name"]].command(
            "createRole", 
            role_config["role"], 
            privileges=role_config["privileges"], 
            roles=role_config["roles"]
        )
        return True
    except Exception as e:
        if "already exists" in str(e):
            print(MESSAGES["role_exists"].format(role_name=role_config["role"]))
            return True
        else:
            print(MESSAGES["role_error"].format(role_name=role_config["role"], error=e))
            return False


def create_user(client, user_config):
    """Crée un utilisateur dans MongoDB"""
    try:
        client[MONGODB_CONFIG["database_name"]].command(
            "createUser", 
            user_config["user"], 
            pwd=user_config["pwd"], 
            roles=user_config["roles"]
        )
        return True
    except Exception as e:
        if "already exists" in str(e):
            print(MESSAGES["user_exists"].format(user_name=user_config["user"]))
            return True
        else:
            print(MESSAGES["user_error"].format(user_name=user_config["user"], error=e))
            return False


def create_roles_and_users():
    """Crée les rôles et utilisateurs pour le système de données médicales"""
    
    try:
        client = MongoClient(get_mongodb_uri())
        healthcare_db = client[MONGODB_CONFIG["database_name"]]
        
        print(MESSAGES["init_start"])
        
        # Création des rôles
        print(MESSAGES["creating_roles"])
        roles_success = all(create_role(client, role) for role in ROLES_CONFIG)
        
        # Création des utilisateurs
        print(MESSAGES["creating_users"])
        users_success = all(create_user(client, user) for user in USERS_CONFIG)
        
        if roles_success and users_success:
            print(MESSAGES["init_success"])
            return True
        return False
        
    except Exception as e:
        print(MESSAGES["init_error"].format(error=e))
        return False


if __name__ == "__main__":
    success = create_roles_and_users()
    sys.exit(0 if success else 1)