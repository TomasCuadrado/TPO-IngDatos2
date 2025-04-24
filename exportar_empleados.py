from pymongo import MongoClient
import pandas as pd
from datetime import datetime

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["restaurante"]
collection = db["empleados"]

# Obtener empleados como lista, excluyendo el campo _id
empleados = list(collection.find({}, {"_id": 0}))

# Crear DataFrame de pandas
df = pd.DataFrame(empleados)

# Si quisieramos ordenarlos por edad (algo que no se hace en el código original)
# df = df.sort_values(by="edad", ascending=False) # Ordenar por edad (de mayor a menor)



# Agregar la fecha actual al nombre del archivo
fecha = datetime.now().strftime("%Y-%m-%d")
nombre_archivo = f"empleados_exportados_{fecha}.csv"

# Exportar a CSV
df.to_csv(nombre_archivo, index=False)

print(f"✅ Datos exportados correctamente a '{nombre_archivo}'")
