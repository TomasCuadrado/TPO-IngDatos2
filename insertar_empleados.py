from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["restaurante"]
coleccion = db["empleados"]

# Insertar empleados nuevos, en este caso solo uno.
empleado_nuevo = {
        "nombre": "Laura Gomez",
        "rol": "moza",
        "dni": "12345678",
    }

print("Empleado insertado.")

# Insertar documento
resultado = coleccion.insert_one(empleado_nuevo)

# Mostrar los IDs de los documentos insertados, para confirmar la inserción.
print("Empleado insertado con ID:", resultado.inserted_id)
