# TPO-IngDatos2
TPO de la materia Ingeniería de datos II, 1er cuatrimestre 2025.
Grupo 3

La idea es armar una base de datos con las siguientes colecciones:
clientes
empleados
platos
pedidos
mesas
categorías (de platos, por ejemplo: entrada, principal, postre)

# Conexión de Python con MongoDB - TP Restaurante 🍽️

Este proyecto conecta Python con una instancia local de MongoDB para el trabajo práctico de la materia.

## Scripts

- `conectar_mongo.py`: Conecta a MongoDB y lista las bases de datos disponibles.
- `crear_restaurante.py`: Crea una base de datos "restaurante" y una colección "platos" con un ejemplo de inserción.
- `insertar_datos.py`:  Inserta datos desde python. Sirve como ejemplo, el resto de colecciones se agregaran desde mongo

## Cómo ejecutar

1. Asegurate de tener MongoDB corriendo localmente.
2. Instalá pymongo

## Agregar colecciones en mongo

Gran parte de colecciones fueron agregadas manualmente con insertOne o insertMany
Queda evidenciado en las capturas
