.data
# Constantes y mensajes
precio_dulce: .word 5           # Precio fijo por dulce (entero)
mensaje_ingrese: .asciiz "Ingrese la cantidad de dulces comprados: "
mensaje_total: .asciiz "Total de esta compra: $"
mensaje_registrar: .asciiz "¿Desea registrar otra compra? (s/n): "
mensaje_separador: .asciiz "\n------------------------------------------------------------\n"
mensaje_total_ventas: .asciiz "Total de ventas del día: $"
mensaje_total_cantidad: .asciiz "Cantidad total de dulces vendidos: "
mensaje_superado: .asciiz "¡Se ha superado la meta de ventas en el día!\n"
mensaje_no_superado: .asciiz "No se ha superado la meta de ventas :(\n"
mensaje_saltolinea: .asciiz "\n"
respuesta: .space 4         # Espacio para respuesta (s/n) (reserva solo para una letra (4byte))

# Variables
total_ventas: .word 0                 # Total acumulado de ventas (entero)
cantidad_total_vendida: .word 0       # Total acumulado de dulces vendidos (entero)

.text
.globl main

main:
    # Inicialización
    li $t0, 1                         # continuar = True (1)

# Ciclo while ------------------------------------------------------------------------------

loop: 
    # Mostrar mensaje "Ingrese la cantidad de dulces comprados"
    li $v0, 4
    la $a0, mensaje_ingrese
    syscall

    # Leer cantidad_comprados
    li $v0, 5                         # Leer un entero
    syscall
    move $t1, $v0                     # Guardar cantidad_comprados en $t1

    # Llamar a calcular_total_compra
    lw $t2, precio_dulce              # Cargar precio_dulce en $t2
    mul $t3, $t1, $t2                 # total_compra = precio * cantidad

    # Mostrar "Total de esta compra: $"
    li $v0, 4
    la $a0, mensaje_total
    syscall
    
    # Imprimir total_compra
    li $v0, 1                         # Imprimir entero
    move $a0, $t3                     # Cargar total_compra en $a0
    syscall

    # Salto de linea
    li $v0, 4
    la $a0, mensaje_saltolinea
    syscall
    

    # Actualizar total_ventas y cantidad_total_vendida
    lw $t4, total_ventas              # Cargar total_ventas en $t4
    add $t4, $t4, $t3                 # total_ventas += total_compra
    sw $t4, total_ventas              # Guardar nuevo total_ventas

    lw $t5, cantidad_total_vendida    # Cargar cantidad_total_vendida en $t5
    add $t5, $t5, $t1                 # cantidad_total_vendida += cantidad_comprados
    sw $t5, cantidad_total_vendida    # Guardar nueva cantidad_total_vendida

    # Preguntar "¿Desea registrar otra compra? (s/n)"
    li $v0, 4
    la $a0, mensaje_registrar
    syscall

    # Leer respuesta
    li $v0, 8                         # Leer cadena
    la $a0, respuesta
    li $a1, 4                         # Máximo de 4 caracteres
    syscall
    
    #Salto de linea
    li $v0, 4
    la $a0, mensaje_saltolinea
    syscall         
	
    # Verificar si la respuesta es 's'
    lb $t6, respuesta                 # Cargar primer carácter de respuesta
    li $t7, 's'
    beq $t6, $t7, loop                # Si respuesta == 's', continuar el ciclo

# end while -------------------------------------------------------------------------

# Mostrar resultados finales del día
    li $v0, 4
    la $a0, mensaje_separador            # Línea separadora
    syscall

    li $v0, 4
    la $a0, mensaje_total_ventas      # "Total de ventas del día: $"
    syscall

    li $v0, 1
    lw $a0, total_ventas              # Imprimir total_ventas
    syscall

    li $v0, 4
    la $a0, mensaje_separador            # Línea separadora
    syscall

    li $v0, 4
    la $a0, mensaje_total_cantidad    # "Cantidad total de dulces vendidos: "
    syscall

    li $v0, 1
    lw $a0, cantidad_total_vendida    # Imprimir cantidad_total_vendida
    syscall

    li $v0, 4
    la $a0, mensaje_separador            # Línea separadora
    syscall

# Sencencia if ------------------------------------------------------------------

# Verificar si total_cantidad supera 20
    lw $t4, cantidad_total_vendida    # Cargar total_cantidad
    li $t8, 20                        # Meta de ventas
    ble $t4, $t8, no_superado         # Si total_ventas <= 20, ir a no_superado

    # Mostrar mensaje de éxito
    li $v0, 4
    la $a0, mensaje_superado
    syscall
    j fin                             # Saltar a fin

no_superado:
    # Mostrar mensaje de no éxito
    li $v0, 4
    la $a0, mensaje_no_superado
    syscall

# end if ---------------------------------------------------------------------------------

fin:
    # Salida del programa
    li $v0, 10
    syscall
