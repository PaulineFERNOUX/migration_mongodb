from pymongo import MongoClient

uri = "mongodb+srv://pauline:Pococo2002@cluster0.iz1s009.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
database = client.get_database("healthcare")
admission_data = database.get_collection("admission_data")

# CREATE - Ajouter
patients = {"name": "Test Patient", "age": 25, "condition": "Test"},{"name": "Test Patient2", "age": 40, "condition": "Test"}
admission_data.insert_many(patients)

# READ - Lire
patient = admission_data.find_one({"name": "Test Patient"})
print(patient)

# UPDATE - Modifier
admission_data.update_one({"name": "Test Patient"}, {"$set": {"age": 26}})

# DELETE - Supprimer
admission_data.delete_one({"name": "Test Patient"})

client.close()
