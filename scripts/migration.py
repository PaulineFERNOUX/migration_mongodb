import pandas as pd
from pymongo import MongoClient
import os

URI = os.getenv('MONGODB_URI', 'mongodb://root:example@mongodb:27017/admin')
client = MongoClient(URI)
db = client["healthcare"]
collection = db["admission_data"]

print("Connexion à MongoDB, début de la migration CSV vers MongoDB")

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