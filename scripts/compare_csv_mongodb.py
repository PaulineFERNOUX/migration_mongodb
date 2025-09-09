import pandas as pd
from pymongo import MongoClient

# Configuration
URI = "mongodb+srv://pauline:Pococo2002@cluster0.iz1s009.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(URI)
collection = client["healthcare"]["admission_data"]

print("COMPARAISON CSV vs MONGODB")

# Charger le CSV
df = pd.read_csv("data/healthcare_dataset.csv")
csv_count = len(df)
print(f"CSV: {csv_count} lignes")

# Compter MongoDB
mongodb_count = collection.count_documents({})
print(f"MongoDB: {mongodb_count} documents")

# Comparer les totaux
if csv_count == mongodb_count:
    print("Même nombre de documents")
else:
    print(f"Différence: {abs(csv_count - mongodb_count)} documents")

# Comparer les âges
csv_age_min = df['Age'].min()
csv_age_max = df['Age'].max()

mongodb_age_min = collection.find().sort("Age", 1).limit(1)[0]["Age"]
mongodb_age_max = collection.find().sort("Age", -1).limit(1)[0]["Age"]

print(f"\nÂGES:")
print(f"  CSV: {csv_age_min} - {csv_age_max}")
print(f"  MongoDB: {mongodb_age_min} - {mongodb_age_max}")

if csv_age_min == mongodb_age_min and csv_age_max == mongodb_age_max:
    print("Âges identiques")
else:
    print("Âges différents")


# Vérifier un échantillon de noms
print(f"\n ÉCHANTILLON DE NOMS:")
csv_names = df['Name'].head(3).tolist()
mongodb_names = [doc["Name"] for doc in collection.find().limit(3)]

print(f"  CSV: {csv_names}")
print(f"  MongoDB: {mongodb_names}")


client.close()
