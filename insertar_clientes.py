from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["restaurante"]
coleccion = db["clientes"]

# Para insertar los clientes nuevos, primero definimos una lista de diccionarios
# donde cada diccionario representa un cliente con sus datos.
clientes_nuevos = [ 
    {
    "nombre": "Juan Pérez",
    "telefono": "123456789",
    "correo": "juan@example.com"
    },
    {
    "nombre": "Julia Gomez",
    "telefono": "123456789",
    "correo": "laura@example.com"
    },
    {
    "nombre": "Raul Gonzalez",
    "telefono": "123456789",
    "correo": "raul@example.com"
    },
    {
    "nombre": "German Martinez",
    "telefono": "123456789",
    "correo": "german@example.com"
    } 
]

# Insertar múltiples documentos
resultado = coleccion.insert_many(clientes_nuevos)

# Mostrar los IDs de los documentos insertados, para confirmar la inserción.
print("Clientes insertados con IDs:", resultado.inserted_ids)