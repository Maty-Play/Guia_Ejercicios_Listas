import os
os.system("cls")

# Banco de ejercicios — Listas en Python
# Ejercicio 1: Mostrar elementos
# Dada la lista:
# numeros = [4, 7, 2, 9, 1]
# Muestra en pantalla cada elemento de la lista usando un ciclo.

# numeros = [4, 7, 2, 9, 1]
# for numeros in numeros:
#     print(numeros)

# ________________________________________
# Ejercicio 2: Suma total
# Dada la lista:
# numeros = [5, 8, 3, 10]
# Calcula y muestra la suma de todos los elementos sin usar sum().

# numeros = [5, 8, 3, 10]
# suma = 0
# for numeros in numeros:
#     suma +=numeros
# print(f"La suma totas es: {suma}")

# ________________________________________
# Ejercicio 3: Contar pares
# Dada la lista:
# numeros = [2, 5, 8, 11, 14, 7]
# Cuenta cuántos números pares hay en la lista.

# numeros = [2, 5, 8, 11, 14, 7]
# contador = 0
# for numeros in numeros:
#     if numeros % 2 == 0:
#         contador += 1
# print(f"Los numeros pares de la lista son estos: {contador}")

# ________________________________________
# Ejercicio 4: Buscar el mayor
# Dada la lista:
# numeros = [12, 4, 19, 7, 15]
# Encuentra y muestra el número más grande sin usar max().

# numeros = [12, 4, 19, 7, 15]
# mayor = numeros[0]
# for numeros in numeros:
#     if numeros > mayor:
#         mayor = numeros
# print(f"El numero mayor de la lista es: {mayor}")

# ________________________________________
# Ejercicio 5: Promedio
# Dada la lista:
# notas = [5.5, 6.0, 4.8, 7.0, 5.9]
# Calcula el promedio de las notas.

# notas = [5.5, 6.0, 4.8, 7.0, 5.9]
# suma = 0
# for nota in notas:
#     suma += nota
# promedio = suma / len(notas)
# print(f"El promedio es: {promedio:.1f}")

# ________________________________________
# Ejercicio 6: Crear una nueva lista
# Dada la lista
# numeros = [1, 2, 3, 4, 5]
# Crea una nueva lista llamada dobles que contenga el doble de cada número.
# Resultado esperado:
# [2, 4, 6, 8, 10]

# numeros = [1, 2, 3, 4, 5]
# dobles = []
# for numeros in numeros:
#     dobles.append(numeros * 2)
# print(f"El doble de la lista es : {dobles}")

# ________________________________________
# Ejercicio 7: Contar apariciones
# Dada la lista:
# frutas = ["manzana", "pera", "manzana", "uva", "pera", "manzana"]
# Cuenta cuántas veces aparece "manzana".

# frutas = ["manzana", "pera", "manzana", "uva", "pera", "manzana"]
# print(frutas.count("manzana"))

# ________________________________________
# Ejercicio 8: Invertir una lista
# Dada la lista:
# numeros = [1, 2, 3, 4, 5]
# Crea una nueva lista con los elementos en orden inverso.
# Resultado esperado:
# [5, 4, 3, 2, 1]

# numeros = [1, 2, 3, 4, 5]
# inverso = []
# for i in range(len(numeros) -1,-1,-1):
#     inverso.append(numeros[i])
# print(inverso)

# ________________________________________
# Ejercicio 9: Eliminar repetidos
# Dada la lista:
# numeros = [1, 2, 2, 3, 4, 4, 5]
# Crea una nueva lista sin elementos repetidos.
# Resultado esperado:
# [1, 2, 3, 4, 5]

# numeros = [1, 2, 2, 3, 4, 4, 5]
# sin_repetidos = []
# for numeros in numeros:
#     if numeros not in sin_repetidos:
#         sin_repetidos.append(numeros)
# print(sin_repetidos)

# ________________________________________
# Ejercicio 10: Separar pares e impares
# Dada la lista:
# numeros = [3, 8, 1, 10, 5, 2, 7]
# Crea dos listas:
# •	una con los números pares 
# •	otra con los números impares 
# Muestra ambas listas.

# numeros = [3, 8, 1, 10, 5, 2, 7]
# pares = []
# impares = []
# for numero in numeros:
#     if numero % 2 == 0:
#         pares.append(numero)
#     else:
#         impares.append(numero)
# print("Pares:", pares)
# print("Impares:", impares)

# ________________________________________
# Desafío extra (opcional)
# Pide al usuario 5 números y guárdalos en una lista. Luego:
# •	muestra la lista, 
# •	muestra el mayor, 
# •	muestra el menor, 
# •	calcula el promedio. 

# numeros = []
# for i in range(5):
#     num = float(input("Ingresa un número: "))
#     numeros.append(num)
# print("Lista:", numeros)
# mayor = numeros[0]
# menor = numeros[0]
# suma = 0
# for num in numeros:
#     suma += num
#     if num > mayor:
#         mayor = num
#     if num < menor:
#         menor = num
# promedio = suma / len(numeros)
# print(f"Mayor: {mayor:.1f}")
# print(f"Menor: {menor:.1f}")
# print(f"Promedio: {promedio:.1f}")