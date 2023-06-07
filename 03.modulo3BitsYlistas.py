#OPERADORES LOGICOS Y BITS
"""
1. Python es compatible con los siguientes operadores lógicos:

and → si ambos operandos son verdaderos, la condición es verdadera, por ejemplo, (True and True) es True.
or → si alguno de los operandos es verdadero, la condición es verdadera, por ejemplo, (True or False) es True.
not → devuelve False si el resultado es verdadero y devuelve True si es falso, por ejemplo, not True es False.
2. Puedes utilizar operadores bit a bit para manipular bits de datos individuales. Los siguientes datos de muestra:

x = 15, el cual es 0000 1111 en binario,
y = 16, el cual es 0001 0000 en binario.
Se utilizarán para ilustrar el significado de operadores bit a bit en Python. Analiza los ejemplos a continuación:

& hace un bit a bit and (y), por ejemplo, x & y = 0, el cual es 0000 0000 en binario,
| hace un bit a bit or (o), por ejemplo, x | y = 31, el cual es 0001 1111 en binario,
˜ hace un bit a bit not (no), por ejemplo, ˜ x = 240*, el cual es 1111 0000 en binario,
^ hace un bit a bit xor, por ejemplo, x ^ y = 31, el cual es 0001 1111 en binario,
>> hace un desplazamiento bit a bit a la derecha, por ejemplo, y >> 1 = 8, el cual es 0000 1000 en binario,
<< hace un desplazamiento bit a bit a la izquierda, por ejemplo, y << 3 = , el cual es 1000 0000 en binario.
"""

#LISTAS
numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

numbers[0] = 111
print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.



print('\n'*2)

#funcion len(); oma el nombre de la lista como un argumento y devuelve
#el número de elementos almacenados actualmente dentro de la lista.

print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

print('\n'*2)

#eliminando elementos de la lista
#INSTRUCCION del

del numbers[1]
print(len(numbers))
print(numbers)

#INDICES NEGATIVOS
"""
Los índices negativos son válidos, y pueden ser muy útiles.
Un elemento con un índice igual a -1 es el último en la lista.
"""
print('\n'*2)

numbers = [111, 7, 2, 1]
print(numbers[-1])

numbers = [111, 7, 2, 1]
print(numbers[-2])

print('\n'*2)

#LABORATORIO

hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.
print (hat_list)
# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
new_number = int(input("Ingresa un número para sustituir a otro en el sombrero: "))
hat_list[2] = new_number
print(hat_list, '\n')
# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list [-1]
# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("La longitud de la lista es: ", len(hat_list))

print("la nueva lista tras los cambios es: ", hat_list)

print('\n'*2)
#Agregando elementos a una lista: append() y insert()
"""
append(). Toma el valor de su argumento y lo coloca al final de la lista que posee el método.
insert() es un poco más inteligente - puede agregar un nuevo elemento en cualquier lugar de la lista:
list.insert(location, value)

"""
print("append() e insert()")
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#CREAR LISTA A PARTIR DE LISTA VACIA Y BUCLE FOR
print('\n'*2, "Completamos lista vacia con bucle for y append")

my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

print("ahora completamos lista con bucle for e insert()")
my_list = []  # Creando una lista vacía.
 
for i in range(5):
    my_list.insert(0, i + 1)#al ir insertando los numeros van desplazandose a la derecha y por ello vemos la lista en orden inverso a la lista de append
 
print(my_list)
 

#calcular la suma de todos los valores almacenados en la lista my_list.
print('\n'*2)

my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

##otra forma de hacerlo
my_list = [10, 1, 8, 3, 5]
total = 0
 
for i in my_list:
    total += i
 
print(total)





#INTERCAMBIAR LOS VALORES DE DOS VARIABLES
variable_1 = 1
variable_2 = 2
 
auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary

#OTRA FORMA MÁS CONVENIENTE

print("Forma adecuada de intercambiar el valor de variables en python:\n")

variable_1 = 1
variable_2 = 2

print("variable_1 = ", variable_1,  "variable_2 = ", variable_2)

variable_1, variable_2 = variable_2, variable_1

print("variable_1 = ", variable_1,  "variable_2 = ", variable_2)

#Intercambiar fácilmente los elementos de la lista para revertir su orden:

"""
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
print(my_list)
 
Nota:

hemos asignado la variable length a la longitud de la lista actual (esto hace que nuestro código sea un poco más claro y más corto)
hemos preparado el bucle for para que se ejecute su cuerpo length // 2 veces (esto funciona bien para listas con longitudes pares e
impares, porque cuando la lista contiene un número impar de elementos, el del medio permanece intacto)
hemos intercambiado el elemento i (desde el principio de la lista) por el que tiene un índice igual
a (length - i - 1) (desde el final de la lista); en nuestro ejemplo, for i igual a 0 a la (length - i - 1) da 4;
for i igual a 3, da 3 - esto es exactamente lo que necesitábamos.
"""

####REVERTIR EL ORDEN DE LOS ELEMENTOS EN UNA LISTA

"""
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
print(my_list)

hemos asignado la variable length a la longitud de la lista actual (esto hace que nuestro código sea un poco más claro y más corto)

hemos preparado el bucle for para que se ejecute su cuerpo length // 2 veces (esto funciona bien para listas con longitudes
pares e impares, porque cuando la lista contiene un número impar de elementos, el del medio permanece intacto)
hemos intercambiado el elemento i (desde el principio de la lista) por el que tiene un índice igual a (length - i - 1)
(desde el final de la lista); en nuestro ejemplo, for i igual a 0 a la (length - i - 1) da 4; for i igual a 3,
da 3 - esto es exactamente lo que necesitábamos.
"""

print("\n"*3)
#LAB LOS BEATLES
# paso 1
beatles = []
print("Paso 1:", beatles)

# paso 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# paso 3
for i in range(2):
    i = input("Agrega el siguiente miembro de la banda: (Stu Sutcliffe y Pete Best)" )
    beatles.append(i)
print("Paso 3:", beatles)

# paso 4
del beatles[-1]
del beatles[-1]
print("Paso 4:", beatles)

# paso 5
beatles.insert(0, "Ringo")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))
