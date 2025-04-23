from pymongo import MongoClient
from datetime import datetime, timedelta

#Conectarse a la base de datos
cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["restaurante"]
coleccion = db["clientes"]

def ver_reserva(cliente):

    cliente_data = coleccion.find_one({"nombre": cliente})
    
    if cliente_data and "reserva" in cliente_data:
        reserva = cliente_data["reserva"]
        if reserva.get("activa"):
            print(f"📅 Fecha: {reserva['fecha']}")
            print(f"🕒 Hora: {reserva['hora']}")
            print(f"🪑 Mesa: {reserva['mesa']}")
        else:
            print("El cliente no tiene una reserva activa.")
    else:
        print("Cliente no encontrado o sin datos de reserva.")