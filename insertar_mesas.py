from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["restaurante"]
coleccion = db["mesas"]

# Insertar mesas nuevas, en este caso solo una.
mesa_nueva = {
        "numero": 5,
        "capacidad": 4
    }

print("Mesa insertada.")

# Insertar documento
resultado = coleccion.insert_one(mesa_nueva)

# Mostrar los IDs de los documentos insertados, para confirmar la inserción.
print("Mesa insertada con ID:", resultado.inserted_id)