from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["restaurante"]
coleccion = db["platos"]

platos_nuevos = [ 
    {
    "nombre": "Pizza Margarita",
    "precio": 12500,
    "disponible": True,
    },
    {
    "nombre": "Pizza Cuatro Quesos",
    "precio": 14500,
    "disponible": True,
    },
    {
    "nombre": "Milanesa con papas",
    "precio": 9500,
    "disponible": True,
    },
    {
    "nombre": "Ensalada Caesar",
    "precio": 8500,
    "disponible": False,
    }
]

# Insertar múltiples documentos
resultado = coleccion.insert_many(platos_nuevos)

# Mostrar los IDs de los documentos insertados, para confirmar la inserción.
print("Platos insertados con IDs:", resultado.inserted_ids)