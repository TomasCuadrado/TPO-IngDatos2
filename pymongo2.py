

from pymongo import MongoClient

# Conectarse al servidor local de MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Obtener y mostrar las bases de datos existentes
bases_de_datos = client.list_database_names()
print("Bases de datos disponibles:")
for db in bases_de_datos:
    print("-", db)
