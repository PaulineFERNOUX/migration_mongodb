#!/usr/bin/env python3
"""
Script simple pour lancer les tests du projet MongoDB
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Exécute une commande et affiche le résultat"""
    print(f"\n{'='*40}")
    print(f"🧪 {description}")
    print(f"{'='*40}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur: {e}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        return False

def main():
    """Fonction principale"""
    print("🚀 Tests du projet MongoDB")
    
    # Vérifier que nous sommes dans le bon répertoire
    if not os.path.exists("pyproject.toml"):
        print("❌ Erreur: pyproject.toml non trouvé.")
        sys.exit(1)
    
    # Menu simple
    print("\n📋 Que voulez-vous tester ?")
    print("1. Tous les tests")
    print("2. Tests de connexion")
    print("3. Tests CRUD")
    print("4. Tests de migration")
    print("5. Tests d'intégration")
    print("0. Quitter")
    
    choice = input("\n👉 Votre choix (0-5): ").strip()
    
    commands = {
        "1": ("poetry run pytest", "Tous les tests"),
        "2": ("poetry run pytest tests/test_connection.py -v", "Tests de connexion"),
        "3": ("poetry run pytest tests/test_crud.py -v", "Tests CRUD"),
        "4": ("poetry run pytest tests/test_migration.py -v", "Tests de migration"),
        "5": ("poetry run pytest tests/test_integration.py -v", "Tests d'intégration")
    }
    
    if choice == "0":
        print("👋 Au revoir!")
        sys.exit(0)
    elif choice in commands:
        command, description = commands[choice]
        success = run_command(command, description)
        
        if success:
            print(f"\n✅ {description} réussis!")
        else:
            print(f"\n❌ {description} échoués!")
            sys.exit(1)
    else:
        print("❌ Choix invalide!")
        sys.exit(1)

if __name__ == "__main__":
    main()
