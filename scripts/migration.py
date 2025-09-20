import pandas as pd
from pymongo import MongoClient
import os
import sys

def connect_to_mongodb():
    """Connexion sécurisée à MongoDB avec authentification"""
    # URI de connexion pour la migration (utilise l'utilisateur admin)
    uri = os.getenv('MONGODB_URI', 'mongodb://admin_user:admin_password_2025@mongodb:27017/healthcare')
    
    try:
        client = MongoClient(uri)
        client.admin.command('ping')
        print("Connexion à MongoDB établie avec authentification")
        return client
    except Exception as e:
        print(f"Erreur de connexion à MongoDB: {e}")
        sys.exit(1)

client = connect_to_mongodb()
db = client["healthcare"]
collection = db["admission_data"]

print("Connexion à MongoDB avec authentification, début de la migration CSV vers MongoDB")

#1- Charger le CSV
print("Chargement du CSV")
df = pd.read_csv("data/healthcare_dataset.csv")
print(f"CSV chargé avec {len(df)} lignes")

#2- Convertir les dates
print("Conversion des dates")
df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])
documents = df.to_dict('records')

#3- Supprimer les documents existants
print("Suppression des documents existants")
collection.delete_many({})

#4- Insérer les documents
print("Insertion des documents")
collection.insert_many(documents)
print(f"{len(documents)} documents insérés!")
print("Migration terminée")

client.close()