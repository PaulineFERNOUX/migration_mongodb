import pandas as pd
from pymongo import MongoClient

# Configuration
URI = "mongodb+srv://pauline:Pococo2002@cluster0.iz1s009.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(URI)
db = client["healthcare"]
collection = db["admission_data"]

print("Chargement du CSV")
df = pd.read_csv("data/healthcare_dataset.csv")

# Convertir les dates
df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])

# Convertir en dictionnaires
documents = df.to_dict('records')

# Insérer
collection.delete_many({})
collection.insert_many(documents)

print(f"{len(documents)} documents insérés!")
client.close()