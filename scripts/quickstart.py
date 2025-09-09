from pymongo import MongoClient
from datetime import datetime

uri = "mongodb+srv://pauline:Pococo2002@cluster0.iz1s009.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

try:
    database = client.get_database("healthcare")
    admission_data = database.get_collection("admission_data")
    
    # Insérer le document Bobby Jackson
    patient = {
        "name": "Bobby Jackson",
        "age": 30,
        "gender": "Male",
        "blood_type": "B-",
        "medical_condition": "Cancer",
        "date_of_admission": datetime(2024, 1, 31),
        "doctor": "Matthew Smith",
        "hospital": "Sons and Miller",
        "insurance_provider": "Blue Cross",
        "billing_amount": 18856.28,
        "room_number": 328,
        "admission_type": "Urgent",
        "discharge_date": datetime(2024, 2, 2),
        "medication": "Paracetamol",
        "test_results": "Normal"
    }
    
    admission_data.insert_one(patient)
    
    # Chercher le patient
    query = {"name": "Bobby Jackson"}
    found_patient = admission_data.find_one(query)
    print(found_patient)
    
    client.close()
except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)
