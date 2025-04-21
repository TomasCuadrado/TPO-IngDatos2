# archivo: crear_restaurante.py

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

# Crear o acceder a una base de datos llamada "restaurante"
db = client["restaurante"]

# Crear una colección llamada "platos"
coleccion = db["platos"]

# Insertar un documento de ejemplo
plato = {"nombre": "Pizza Margarita", "precio": 2500, "disponible": True}
resultado = coleccion.insert_one(plato)

print(f"Documento insertado con ID: {resultado.inserted_id}")
