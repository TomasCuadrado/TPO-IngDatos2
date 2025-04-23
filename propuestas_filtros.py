#Ctrl + B = F5

from pymongo import MongoClient
from datetime import datetime, timedelta

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["restaurante"]

#Funciones
#Filtrar platos por categoria
def filtrar_platos_categoria(categoria):
    coleccion = db["platos"]
    platos = coleccion.find({"categoria": categoria})
    return list(platos)

#Filtrar platos por precio
def filtrar_platos_precio(precio_minimo, precio_maximo):
    coleccion = db["platos"]
    platos = coleccion.find({"precio": {"$gte": precio_minimo, "$lte": precio_maximo}})
    return list(platos)

#Filtrar empleados por rol
def filtrar_empleados_rol(rol):
    coleccion = db["empleados"]
    empleados = coleccion.find({"rol": rol})
    return list(empleados)

#Filtrar mesas que esten disponibles
def filtrar_mesas_disponibles():
    coleccion = db["mesas"]
    mesas = coleccion.find({"disponible": True})
    return list(mesas)

#Filtrar clientes con reservas "activas"
def filtrar_clientes_reservas_activas():
    coleccion = db["clientes"]
    clientes = coleccion.find({"reserva.activa": True})
    return list(clientes)

#Filtrar por pedidos con estado de pago pendiente
def filtrar_pedidos_pagos_pendientes():
    coleccion = db[pedidos]
    pedidos = coleccion.find({"estado_pago": "pendiente"})
    return list(pedidos)

#Filtrar pedidos realizados hoy
def filtrar_pedidos_hoy():
    coleccion = db["pedidos"]
    hoy = datetime.now().date()
    pedidos = coleccion.find({"fecha": {"$gte": hoy}})
    return list(pedidos)

#Cancelar reserva de un cliente.
def cancelar_reserva(cliente):
    coleccion = db["clientes"]
    
    resultado = coleccion.update_one(
        {"nombre": cliente},
        {
            "$set": {
                "reserva.activa": False,
                "reserva.fecha": None,
                "reserva.hora": None,
                "reserva.mesa": None
            }
        }
    )

    if resultado.modified_count > 0:
        print("Reserva cancelada exitosamente.")
    else:
        print("No se encontró la reserva o ya estaba cancelada.")

#Ver reservas de un cliente
def ver_reserva(cliente):
    coleccion = db["clientes"]
    
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

#Programa principal
def main():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Filtrar platos por categoría")
        print("2. Filtrar platos por precio")
        print("3. Filtrar empleados por rol")
        print("4. Ver mesas disponibles")
        print("5. Ver clientes con reservas activas")
        print("6. Ver pedidos con pago pendiente")
        print("7. Ver pedidos realizados hoy")
        print("8. Cancelar reserva de un cliente")
        print("9. Ver reserva de un cliente")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            categoria = input("Ingrese la categoría del plato: ")
            resultados = filtrar_platos_categoria(categoria)
        elif opcion == "2":
            precio_min = float(input("Precio mínimo: "))
            precio_max = float(input("Precio máximo: "))
            resultados = filtrar_platos_precio(precio_min, precio_max)
        elif opcion == "3":
            rol = input("Ingrese el rol del empleado (ej: mozo, cocinero): ")
            resultados = filtrar_empleados_rol(rol)
        elif opcion == "4":
            resultados = filtrar_mesas_disponibles()
        elif opcion == "5":
            resultados = filtrar_clientes_reservas_activas()
        elif opcion == "6":
            resultados = filtrar_pedidos_pagos_pendientes()
        elif opcion == "7":
            resultados = filtrar_pedidos_hoy()
        elif opcion == "8":
            nombre = input("Nombre del cliente: ")
            cancelar_reserva(nombre)
        elif opcion == "9":
            nombre = input("Nombre del cliente: ")
            ver_reserva(nombre)
        elif opcion == "0":
                print("Saliendo del programa.")
                break
        else:
            print("Opción inválida.")
            continue
        print("\n--- RESULTADOS ---")
        for doc in resultados:
            print(doc)

if __name__ == "__main__":
    main()