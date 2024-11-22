#CONTEXTO
#Una tienda de dulces necesita un programa que les ayude a calcular
#el total de sus ventas diarias, verificando si se cumple la meta de ventas en el dia. 
#Cada dulce tiene un precio estándar de $5 y la meta de ventas es vender más de 20 dulces

#Declaración de variables y asignaciones iniciales
precio_dulce = 5        #Precio de cada dulce
total_ventas = 0
cantidad_total_vendida = 0

#Función para calcular el total de una compra con posible descuento
def calcular_total_compra(precio, cantidad):
    total = precio * cantidad
    return total

#Ciclo para registrar varias compras en un solo día
continuar = True
while continuar:
    cantidad_comprados = int(input("Ingrese la cantidad de dulces comprados: "))
    
    #Llamada a la función para calcular el total de esta compra
    total_compra = calcular_total_compra(precio_dulce, cantidad_comprados)
    print(f"Total de esta compra: ${total_compra}")
    
    #Acumulación en total de ventas y cantidad vendida
    total_ventas = total_ventas + total_compra
    cantidad_total_vendida = cantidad_total_vendida + cantidad_comprados
    
    #Preguntar si desea registrar otra compra
    respuesta = input("¿Desea registrar otra compra? (s/n): ")  #s para si y n para no
    continuar = respuesta.lower() == 's'

#Resultados finales del día
print("------------------------------------------------------------")
print(f"Total de ventas del día: ${total_ventas}")
print("------------------------------------------------------------")
print(f"Cantidad total de dulces vendidos: {cantidad_total_vendida}")
print("------------------------------------------------------------")


if(total_ventas>20):
    print("¡Se ha superado la meta de ventas en el día!")
    print("------------------------------------------------------------")
else:
    print("No se ha superado la meta de ventas :(")
    print("------------------------------------------------------------")
