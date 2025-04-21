from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["restaurante"]
coleccion = db["clientes"]

# Insertar cliente
cliente_nuevo = {
    "nombre": "Juan Pérez",
    "telefono": "123456789",
    "correo": "juan@example.com"
}

coleccion.insert_one(cliente_nuevo)
print("Cliente insertado.")
