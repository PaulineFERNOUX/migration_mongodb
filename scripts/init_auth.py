from pymongo import MongoClient
import os
import sys

def create_roles_and_users():
    """Crée les rôles et utilisateurs pour le système de données médicales"""
    
    # URI de connexion
    uri = os.getenv('MONGODB_URI', 'mongodb://root:example@mongodb:27017/admin')
    
    try:
        client = MongoClient(uri)
        admin_db = client.admin
        
        print("Initialisation de l'authentification MongoDB...")
        
        # 1. Création base de données healthcare
        healthcare_db = client["healthcare"]
        
        # 2. Création des rôles
        print("Création des rôles")
        
        # Rôle : Lecture seule pour l'analyse
        analyst_role = {
            "role": "healthcare_analyst",
            "privileges": [
                {
                    "resource": {"db": "healthcare", "collection": "admission_data"},
                    "actions": ["find"]
                },
                {
                    "resource": {"db": "healthcare", "collection": "admission_data"},
                    "actions": ["listCollections", "listIndexes"]
                }
            ],
            "roles": []
        }
        
        
        # Rôle : Admin pour les administrateurs système
        admin_role = {
            "role": "healthcare_admin",
            "privileges": [
                {
                    "resource": {"db": "healthcare", "collection": "admission_data"},
                    "actions": ["find", "insert", "update", "remove"]
                },
                {
                    "resource": {"db": "healthcare", "collection": ""},
                    "actions": ["listCollections", "listIndexes", "createCollection", "dropCollection"]
                }
            ],
    "roles": []
}
        
        
        
        roles_to_create = [analyst_role, admin_role]
        
        for role in roles_to_create:
            try:
                admin_db.command("createRole", role["role"], privileges=role["privileges"], roles=role["roles"])
            except Exception as e:
                if "already exists" in str(e):
                    print(f"Rôle '{role['role']}' existe déjà")
                else:
                    print(f"Erreur création rôle '{role['role']}': {e}")
        
        # 3. Création des utilisateurs
        print("Création des utilisateurs...")
        
        users_to_create = [
            {
                "user": "analyst_user",
                "pwd": "analyst_password_2025",
                "roles": [{"role": "healthcare_analyst", "db": "healthcare"}]
            },
            {
                "user": "admin_user",
                "pwd": "admin_password_2025", 
                "roles": [{"role": "healthcare_admin", "db": "healthcare"}]
            }
        ]
        
        for user in users_to_create:
            try:
                admin_db.command("createUser", user["user"], pwd=user["pwd"], roles=user["roles"])
            except Exception as e:
                if "already exists" in str(e):
                    print(f"Utilisateur '{user['user']}' existe déjà")
                else:
                    print(f"Erreur création utilisateur '{user['user']}': {e}")
        
    except Exception as e:
        print(f"Erreur lors de l'initialisation: {e}")
        return False

if __name__ == "__main__":
    success = create_roles_and_users()
    sys.exit(0 if success else 1)
