from pymongo import MongoClient

# Conectarse a la base de datos
cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["restaurante"]
coleccion = db["clientes"]  # Cambiá por la colección que quieras consultar

# Obtener todos los documentos (para obtener todos los datos utilizamos solamente ".find()" )
documentos = coleccion.find()

# Mostrar los documentos
for doc in documentos:
    print(doc)
