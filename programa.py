#CONTEXTO
#Una tienda de dulces necesita un programa que les ayude a calcular
#los costos y descuentos de sus ventas diarias. Cada dulce tiene un
#precio estándar, pero si el cliente compra una cantidad equivalente a un numero primo de dulces recibe
#un descuento especial. La tienda también quiere saber el total de ventas
#al final del día y cuántos dulces en total se vendieron.

# Declaración de variables y asignaciones iniciales
precio_dulce = 5  # Precio de cada dulce
total_ventas = 0
cantidad_total_vendida = 0

# Función para verificar si la cantidad es primo
def es_primo(n):
    if n<2:
        return False  
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

# Función para calcular el total de una compra con posible descuento
def calcular_total_compra(precio, cantidad):
    total = precio * cantidad
    descuento = 0.1  # 10% de descuento
    if es_primo(cantidad):      # Si la cantidad es primo se le aplica el descuento del 20%
        total = total - (total * descuento)
    return total

# Ciclo para registrar varias compras en un solo día
continuar = True
while continuar:
    cantidad_comprados = int(input("Ingrese la cantidad de dulces comprados: "))
    
    # Llamada a la función para calcular el total de esta compra
    total_compra = calcular_total_compra(precio_dulce, cantidad_comprados)
    print(f"Total de esta compra: ${total_compra}")
    
    # Acumulación en total de ventas y cantidad vendida
    total_ventas = total_ventas + total_compra
    cantidad_total_vendida = cantidad_total_vendida + cantidad_comprados
    
    # Preguntar si desea registrar otra compra
    respuesta = input("¿Desea registrar otra compra? (s/n): ")
    continuar = respuesta.lower() == 's'

# Resultados finales del día
print(f"Total de ventas del día: ${total_ventas}")
print(f"Cantidad total de dulces vendidos: {cantidad_total_vendida}")
