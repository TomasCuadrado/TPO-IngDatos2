from pymongo import MongoClient
from datetime import datetime, timedelta


cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["restaurante"]

# Funciones de consultas

def platos_entrada_baratos():
    platos = db.platos.find({
        "categoria": "entrada",
        "precio": {"$lt": 5000},
        "disponible": True
    })
    for plato in platos:
        print(plato)

def contar_clientes_con_reserva():
    total = db.clientes.count_documents({"reserva.activa": True})
    print(f"Clientes con reservas activas: {total}")

def contar_pedidos_ultimo_mes():
    fecha_limite = datetime.now() - timedelta(days=30)
    total = db.pedidos.count_documents({"fecha": {"$gte": fecha_limite}})
    print(f"Pedidos en el último mes: {total}")

def cocineros_antiguos():
    fecha_limite = datetime.now() - timedelta(days=5*365)
    empleados = db.empleados.find({
        "rol": "cocinero",
        "fecha_contratacion": {"$lt": fecha_limite}
    })
    for emp in empleados:
        print(emp)

def promedio_precio_por_categoria():
    resultados = db.platos.aggregate([
        {
            "$group": {
                "_id": "$categoria",
                "precio_promedio": {"$avg": "$precio"}
            }
        }
    ])
    for res in resultados:
        print(f"Categoría: {res['_id']}, Precio Promedio: ${res['precio_promedio']:.2f}")

# Menú interactivo

def menu():
    while True:
        print("\n=== MENÚ DE CONSULTAS ===")
        print("1. Platos disponibles categoría 'entrada' y precio < 5000")
        print("2. Contar clientes con reservas activas")
        print("3. Cantidad de pedidos del último mes")
        print("4. Empleados cocineros con más de 5 años")
        print("5. Promedio de precio por categoría")
        print("6. Salir")

        opcion = input("Selecciona una opción (1-6): ")

        if opcion == "1":
            platos_entrada_baratos()
        elif opcion == "2":
            contar_clientes_con_reserva()
        elif opcion == "3":
            contar_pedidos_ultimo_mes()
        elif opcion == "4":
            cocineros_antiguos()
        elif opcion == "5":
            promedio_precio_por_categoria()
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()