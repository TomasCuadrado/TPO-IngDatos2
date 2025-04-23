from pymongo import MongoClient
from datetime import datetime, timedelta

#Conectarse a la base de datos
cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["restaurante"]
coleccion = db["clientes"]

#Actualizar reservas de cliente
def reserva(cliente):
    # Obtener la fecha y hora actual
    fecha_hora_actual = datetime.now()
    
    # Calcular la fecha y hora de la reserva (dentro de 2 horas)
    reserva_fecha_hora = fecha_hora_actual + timedelta(hours=2)
    
    # Formatear la fecha y hora en el formato deseado
    reserva_fecha = reserva_fecha_hora.strftime("%Y-%m-%d")
    reserva_hora = reserva_fecha_hora.strftime("%H:%M:%S")
    
    # Actualizar el cliente con la nueva reserva
    coleccion.update_one(
        {"nombre": cliente},
        {
            "$set": {
                "reserva.fecha": reserva_fecha,
                "reserva.hora": reserva_hora,
                "reserva.mesa": 5,  # Asignar mesa 1 como ejemplo
                "reserva.activa": True
            }
        }
    )
