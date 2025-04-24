from pymongo import MongoClient
import json

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["restaurante"]
coleccion = db["clientes"]

with open("Gastronomia_Grupo03.json", "r", encoding='utf-8') as f:
    datos = json.load(f)

coleccion.insert_many(datos)
print("Datos cargados en MongoDB.")
