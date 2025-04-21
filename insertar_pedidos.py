import datetime
from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["restaurante"]
coleccion = db["pedidos"]

# Obtener la fecha actual en formato YYYY-MM-DD
fecha_str = datetime.datetime.now().strftime("%Y-%m-%d")

# Insertar pedidos nuevos, en este caso solo uno.
# Asegúrate de que la fecha esté en el formato correcto.
pedidos_nuevos = {
    "cliente": "Juan Perez",
    "mesa": 5,
    "plato": "Milanesa con papas",
    "fecha": fecha_str,
    "estado_pago": "pendiente",
    }


# Insertar documento
resultado = coleccion.insert_one(pedidos_nuevos)

# Mostrar los IDs de los documentos insertados, para confirmar la inserción.
print("Pedido insertados con ID:", resultado.inserted_id)