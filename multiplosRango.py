"""ENUNCIADO: Hallar cuantos múltiplos de M hay en un rango de números enteros.

ANÁLISIS: Para la solución de este problema, se requiere que el usuario ingrese tres números (NumInicial, NumFinal y NumMúltiplo). luego el sistema devuelve la cantidad de múltiplos que hay en el rango."""


# Variables | Ingresar Datos.
valor1 = int(input('Número inicial: '))
valor2 = int(input('Número final: '))
multiplo = int(input('Número múltiplo: '))
valor2 += 1
cantidad = 0


# Solución
for numero in range(valor1, valor2):
    if numero % multiplo == 0:
        cantidad += 1


# Mostrar Datos
print('Cantidad: ', cantidad)
