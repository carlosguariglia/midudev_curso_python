###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

name = input("Ingresa tu nombre: ")
city = input("Ingresa tu ciudad: ")


# imprime name y city en dos líneas
print(f"Salida por consola en 2 lineas usando 2 lineas de codigo")
print(f"Hola {name}, encantado de conocerte")
print(f"Vives en {city}")

#refactoriza las 2 lineas anteriores en una sola linea de codigo que haga lo mismo

print(f"Salida por consola en 2 lineas usando 1 lineas de codigo")
print(f"Hola {name}, encantado de conocerte\nVives en {city}")


print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

print(f"a: {a} es de tipo {type(a)}")
print(f"b: {b} es de tipo {type(b)}")
print(f"c: {c} es de tipo {type(c)}")
print(f"d: {d} es de tipo {type(d)}")
print(f"e: {e} es de tipo {type(e)}")

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

cadena = "12345"
print(f"cadena: {cadena} es de tipo {type(cadena)}")

entero = int(cadena)
print(f"a entero: {entero}")

real = float(cadena)
print(f"a float: {real}")

casi_cuatro = int(3.99)
print(f"el numero 3.99 a entero es: {casi_cuatro}")
print(f"al castear un float a entero se pierde la parte decimal, no redondea")

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

name = "Carlos"
age = 48
altura = 1.76

print(f"Hola! Me llamo {name} y tengo {age} anos, mido {altura} metros")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

PI = 3.14159

print(f"El numero PI es: {PI}")

print(f"El numero PI redondeado es: {round(PI)}")

print(f"El numero PI (redondeado) dividido por 2 (division entera) es: {round(PI) // 2}")



