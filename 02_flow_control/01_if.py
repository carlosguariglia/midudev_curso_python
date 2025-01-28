###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

import os           # importa el modulo os
import platform     # importa el modulo platform

if platform.system() == "Windows":  
    os.system("cls")  # limpia la consola en Windows
else:
    os.system("clear")  # limpia la consola en sistemas Unix

print("\n Sentencia simple condicional")

edad = 18
if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")

edad = 15
if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")

print("\n Sentencia condicional con else")
edad = 15
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")

print("\n Sentencia condicional con elif")
nota = 5

if nota >= 9:
  print("¡Sobresaliente!")
elif nota >= 7:
  print("Notable!")
elif nota >= 5:
  print("¡Aprobado!")
else:
  print("¡No está calificado!")

print("\n Condiciones múltiples")
edad = 16
tiene_carnet = True

# JavaScript
# && -> and
# || -> or

# 🇻🇪 un pueblo de Valencia
if edad >= 18 and tiene_carnet:
  print("Puedes conducir 🚗")
else:
  print("POLICIA 🚔!!!1!!!")

# 🇻🇪 un pueblo de Isla Margarita
if edad >= 18 or tiene_carnet:
  print("Puedes conducir en la Isla Margarita 🚗")
else:
  print("Paga al policía y te deja conducir!!!")

es_fin_de_semana = False
# JavaScript -> !
if not es_fin_de_semana:
  print("¡midu, venga que hay que streamear!")


print("\n Anidar condicionales")
edad = 20
tiene_dinero = True

if edad >= 18:
  if tiene_dinero:
    print("Puedes ir a la discoteca")
  else:
    print("Quédate en casa")
else:
  print("No puedes entrar a la disco")

# Más fácil:
# if edad < 18:
#   print("No puedes entrar a la disco")
# elif tiene_dinero:
#   print("Puedes ir a la discoteca")
# else:
#   print("Quédate en casa")

numero = 5
if numero: # True
  print("El número no es cero")

numero = 0
if numero: # False
  print("Aquí no entrará nunca")

nombre = ""
if nombre:
  print("El nombre no es vacío")

numero = 3 # asignación
es_el_tres = numero == 3 # comparación

if es_el_tres:
  print("El número es 3")


print("\nLa condición ternaria:")
# es una forma concisa de un if-else en una línea de código
# [código si cumple la condición] if [condicion] else [codigo si no cumple]

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)

if platform.system() == "Windows":  
    os.system("cls")  # limpia la consola en Windows
else:
    os.system("clear")  # limpia la consola en sistemas Unix

print("\n Ejericio 1: Determinar el mayor de dos números")
###
# EJERCICOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

numero1 = float(input("Ingresa el primer numero: "))
numero2 = float(input("Ingresa el segundo numero: "))

if numero1 > numero2:
  print(f"{numero1} es mayor que {numero2}")
elif numero2 > numero1:
  print(f"{numero2} es mayor que {numero1}")
else:
  print("Los números son iguales")

input("Presiona Enter para continuar...")

print("\n Ejericio 2: Calculadora simple")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

numero1 = float(input("Ingresa el primer numero: "))
numero2 = float(input("Ingresa el segundo numero: "))
operacion = input("Ingresa la operación (+, -, *, /): ")

if operacion == "+":
  resultado = numero1 + numero2
elif operacion == "-":
  resultado = numero1 - numero2
elif operacion == "*":
  resultado = numero1 * numero2
elif operacion == "/":
  if numero2 == 0:
    print("No se puede dividir por cero")
  else:
    resultado = numero1 / numero2
else:
  print("Operación no reconocida")

print(f"El resultado es: {resultado}")

input("Presiona Enter para continuar...")

print("\n Ejericio 3: Año bisiesto")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

anio = int(input("Ingresa un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
  print(f"{anio} es un año bisiesto.")
else:
  print(f"{anio} no es un año bisiesto.")
  
input("Presiona Enter para continuar...")

print("\n Ejericio 4: Categorizar edades")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = int(input("Ingresa tu edad: "))

if 0 <= edad <= 2:
  print("Bebé")
elif 3 <= edad <= 12:
  print("Niño")
elif 13 <= edad <= 17:
  print("Adolescente")
elif 18 <= edad <= 64:
  print("Adulto")
elif edad >= 65:
  print("Adulto mayor")
else:
  print("Edad no reconocida")