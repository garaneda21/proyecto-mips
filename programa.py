# Declaración de variables y asignaciones iniciales
precio_videojuego = 20  # Precio de cada videojuego
total_ventas = 0
cantidad_total_vendida = 0

# Función para calcular el total de una compra con posible descuento
def calcular_total_compra(precio, cantidad):
    total = precio * cantidad
    descuento = 0.1  # 10% de descuento
    if cantidad > 3:
        total -= total * descuento
    return total

# Ciclo para registrar varias compras en un solo día
continuar = True
while continuar:
    cantidad_comprados = int(input("Ingrese la cantidad de videojuegos comprados: "))
    
    # Llamada a la función para calcular el total de esta compra
    total_compra = calcular_total_compra(precio_videojuego, cantidad_comprados)
    print(f"Total de esta compra: ${total_compra}")
    
    # Acumulación en total de ventas y cantidad vendida
    total_ventas += total_compra
    cantidad_total_vendida += cantidad_comprados
    
    # Preguntar si desea registrar otra compra
    respuesta = input("¿Desea registrar otra compra? (s/n): ")
    continuar = respuesta.lower() == 's'

# Resultados finales del día
print(f"Total de ventas del día: ${total_ventas}")
print(f"Cantidad total de videojuegos vendidos: {cantidad_total_vendida}")
