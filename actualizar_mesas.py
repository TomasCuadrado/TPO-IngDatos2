from pymongo import MongoClient
from datetime import datetime, timedelta

#Conectarse a la base de datos
cliente = MongoClient("mongodb://localhost:27017/") 
db = cliente["restaurante"]
coleccion = db["mesas"]


#Actualizar una mesa para agregar el campo "disponible" y "reservada"
"""
coleccion.update_one({"numero": 5}, 
                      {
                          "$set": 
                              {"disponible": True,
                               "reservada": False
                              }
                           }
                      )
"""
"""
#Actualizar mesas para agregar el campo "disponible" y "reservada"
coleccion.update_many({}, 
                      {
                          "$set": 
                              {"disponible": True,
                               "reservada": False
                              }
                           }
                      )
"""
print("Mesas actualizadas correctamente.")