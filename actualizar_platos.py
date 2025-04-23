from pymongo import MongoClient

#Conectarse a la base de datos
cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["restaurante"]
coleccion = db["platos"] 

#Lista de categorias a asignar manualmente (segun el nomnbre del plato)
coleccion.update_one({"nombre": "Ensalada Caesar"}, {"$set": {"categoria": "Ensaladas"}})
coleccion.update_one({"nombre": "Pizza Margarita"}, {"$set": {"categoria": "Pizzas"}})
coleccion.update_one({"nombre": "Milanesa con papas"}, {"$set": {"categoria": "Carnes"}})
coleccion.update_one({"nombre": "Pizza Cuatro Quesos"}, {"$set": {"categoria": "Pizzas"}})

print("Platos actualizados correctamente.")