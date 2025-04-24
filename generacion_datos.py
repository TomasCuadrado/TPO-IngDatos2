#Generar un archivo .json de forma automática
import random
import json
from faker import Faker #Antes de utilizarlo debemos instalarlo -> pip install faker
#El módulo Faker en Python se utiliza para generar datos ficticios,
# (fake data) de forma rápida y realista.

fake = Faker()
datos_clientes = []

for _ in range(30):
    cliente = {
        "nombre": fake.name(),
        "telefono": fake.phone_number(),
        "correo": fake.email(),
        "reserva": {
            "activa": random.choice([True, False]),
            "fecha": fake.date_this_month().isoformat(),
            "hora": fake.time(),
            "mesa": random.randint(1, 10)
        }
    }
    datos_clientes.append(cliente)

# Guardar como JSON
with open("Gastronomia_Grupo03.json", "w", encoding='utf-8') as f:
    json.dump(datos_clientes, f, ensure_ascii=False, indent=4)

print("Archivo JSON generado.")


