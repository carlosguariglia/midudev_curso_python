###
# 04 - Listas Métodos
# Los métodos más importantes para trabajar con listas
###

import os           # importa el modulo os
import platform     # importa el modulo platform

if platform.system() == "Windows":  
    os.system("cls")  # limpia la consola en Windows
else:
    os.system("clear")  # limpia la consola en sistemas Unix

lista1 = ['a', 'b', 'c', 'd']

# Añadir o insertar elementos a la lista

lista1.append('e') # Añade un elemento al final
print(lista1)

lista1.insert(1, '@') # Inserta un elemento en la posición que le indiquemos como primer argumento
print(lista1)

lista1.extend(['😃', '😍']) # Agrega elementos al final de la lista
print(lista1)

# Eliminar elementos de la lista
lista1.remove('@') # Eliminar la primera aparición de la cadena de texto @
print(lista1)

ultimo = lista1.pop() # Eliminar el último elemento de la lista y además te lo devuelve
print(ultimo)
print(lista1)

lista1.pop(1) # Eliminar el segundo elemento de la lista (es el índice 1)
print(lista1)

# Eliminar por lo bestia
del lista1[-1]
print(lista1)

lista1.clear() # Eliminar todos los elementos de la lista
print(lista1)

# Eliminar un rango de elementos
lista1 = ['🐼', '🐨', '🐶', '😿', '🐹']
del lista1[1:3]
print(lista1)

# Más métodos útiles
print('Ordenar listas modificando la original')
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort()
print(numbers)

print('Ordenar listas creando una nueva lista')
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print("Ordenar una lista de cadenas de texto (todo minúscula)")
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower)
print(frutas)

# Más cositas útiles
animals = ['🐶', '🐼', '🐨', '🐶']
print(len(animals)) # Tamaño de la listas -> 4
print(animals.count('🐶')) # Cuantas veces aparece el elemento '🐶' -> 2
print('🐼' in animals) # Comprueba si hay un '🐼' en la lista -> True
print('🐹' in animals) # -> False

if platform.system() == "Windows":  
    os.system("cls")  # limpia la consola en Windows
else:
    os.system("clear")  # limpia la consola en sistemas Unix

###
# EJERCICOS
# Usa siempre que puedas los métodos que has aprendido
###

print("\n Ejericio 1: Añadir y modificar elementos")

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

lista = [1, 2, 3, 4, 5]
print(f"Lista original: {lista}")
lista.append(6)  # Añade el número 6 al final
lista.insert(2, 10) # Inserta el número 10 en la posición 2
lista[0] = 0 # Modifica el primer elemento de la lista para que sea 0
print(f"Lista modificada: {lista}")

input("\nPresiona Enter para continuar...")
print("\nEjercicio 2: Combinar y limpiar listas")

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]

print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")

lista_a.extend(lista_b) # Extiende lista_a con lista_b
print(f"Lista A extendida: {lista_a}")

lista_a.remove(1) # Elimina la primera aparición del número 1 en lista_a
print(f"Lista A sin el 1: {lista_a}")

elemento_eliminado = lista_a.pop(3) # Elimina el elemento en el índice 3 de lista_a
print(f"Elemento eliminado: {elemento_eliminado}")
print(f"Lista A sin el elemento eliminado: {lista_a}")

lista_b.clear() # Limpia completamente lista_b
print(f"Lista B limpia: {lista_b}")

input("\nPresiona Enter para continuar...")
print("\nEjercicio 3: Slicing y eliminación con del")

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

lista = list(range(1, 11))
print(f"Lista original: {lista}")

del lista[2:6] # Elimina los elementos desde el índice 2 hasta el 5 (sin incluir el 5)
print(f"Lista con elementos eliminados: {lista}")

input("\nPresiona Enter para continuar...")
print("\nEjercicio 4: Ordenar y contar")

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

lista = [5, 2, 8, 1, 9, 4, 2]
print(f"Lista original: {lista}")

lista.sort() # Ordena la lista de forma ascendente
print(f"Lista ordenada: {lista}")

cantidad_dos = lista.count(2) # Cuenta cuántas veces aparece el número 2 en la lista
print(f"Cantidad de 2: {cantidad_dos}")

esta_el_siete = 7 in lista # Comprueba si el número 7 está en la lista
# una forma de hacerlo en una linea es:
# print("¿Está el 7?:", "Sí" if esta_el_siete else "No")
    
# otra forma es: (manipulando el salto de linea por defecto de print)
print("¿Está el 7?: ", end="")  # Evita el salto de línea
if esta_el_siete:
    print("Sí")
else:
    print("No")
    
input("\nPresiona Enter para continuar...")
print("\nEjercicio 5: Copia vs. Referencia")

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

original = [1, 2, 3]
copia_1 = original[:]
copia_2 = original.copy()
referencia = original





print(f"Original: {original}")
print(f"Copia 1: copiada usando slicing {copia_1}")
print(f"Copia 2: copiada usando copy() {copia_2}")
print(f"Referencia: copiada usando referencia {referencia}")

print("Modificando el primer elemento de la lista referencia a 10")
referencia[0] = 10

print(f"Original: {original}")
print(f"Copia 1: copiada usando slicing {copia_1}")
print(f"Copia 2: copiada usando copy() {copia_2}")
print(f"Referencia: copiada usando referencia {referencia}")


print ("Observa que al modificar la referencia se modifica la original")
print ("Esto es porque las listas son mutables y las referencias apuntan al mismo objeto")
print ("Si quieres copiar una lista sin que se modifique la original, usa slicing o copy()")

input("\nPresiona Enter para continuar...")
print("\nEjercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.")

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.

frutas = ["Manzana", "pera", "BANANA", "naranja", "KIWI", "fresa"]
print(f"Frutas: {frutas}")
frutas.sort(key=str.lower) # Ordena la lista sin diferenciar entre mayúsculas y minúsculas
print(f"Frutas ordenadas: {frutas}")