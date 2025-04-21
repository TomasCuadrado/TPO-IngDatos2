from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["restaurante"]
coleccion = db["categorias"]

# Insertar categorias nuevas, en este caso solo una.
categoria_nueva = {
        "nombre": "Bebidas",
    }

print("Categoria insertada.")

# Insertar documento
resultado = coleccion.insert_one(categoria_nueva)

# Mostrar los IDs de los documentos insertados, para confirmar la inserción.
print("Categoria insertada con ID:", resultado.inserted_id)