from pymongo import MongoClient
cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["restaurante"]
coleccion = db["clientes"]

#Actualizar clientes para agregar el campo "reserva"
coleccion.update_many({}, 
                      {
                          "$set": 
                              {"reserva": {
                                "fecha": None,
                                "hora": None,
                                "mesa": None,
                                "activa": False
                                  }
                               }
                            }
                      )
print("Clientes actualizados correctamente.")
