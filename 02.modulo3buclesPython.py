#BUCLE WHILE

# Almacena el actual número más grande aquí.
largest_number = -999999999
 
# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))
 
# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))
 
# Imprime el número más grande.
print("El número más grande es:", largest_number)
 
print("\n"*2)

# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.
 
odd_numbers = 0
even_numbers = 0
 
# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))
 
# 0 termina la ejecución.
while number != 0:
    # Verificar si el número es impar.
    if number % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        even_numbers += 1
    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))
 
# Imprimir resultados.
print("Conteo de números impares:", odd_numbers)
print("Conteo de números pares:", even_numbers)

print("\n"*2)
#Empleando una variable counter para salir del bucle
counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)

print("\n"*2)
"""
Con la funcion PRINT() utilizar comillas triples para imprimir cadenas en varias líneas para
facilitar la lectura del texto o crear un diseño especial basado en texto.
"""
#ADIVINA EL NUMERO SECRETO
secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

number = int(input("Introduce un número: "))

while number!=secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!\n")
    
    number =int(input("Introduce un número: ","\n"))
    

print(number,"¡Bien hecho, muggle! Eres libre ahora.")



#BUCLE FOR
"""
for i in range(100):
    # do_something()
    pass

    
la palabra reservada for abre el bucle for; nota - No hay condición después de eso;
no tienes que pensar en las condiciones, ya que se verifican internamente, sin ninguna intervención.
cualquier variable después de la palabra reservada for es la variable de control del bucle;
cuenta los giros del bucle y lo hace automáticamente.

la palabra reservada in introduce un elemento de sintaxis que describe el rango de valores
posibles que se asignan a la variable de control.

la función range() (esta es una función muy especial) es responsable de generar todos
los valores deseados de la variable de control; en nuestro ejemplo, la función
creará (incluso podemos decir que alimentará el bucle con) valores subsiguientes
del siguiente conjunto: 0, 1, 2 .. 97, 98, 99; nota: en este caso, la función range()
comienza su trabajo desde 0 y lo finaliza un paso (un número entero) antes del valor de su argumento.

la palabra clave pass dentro del cuerpo del bucle - no hace nada en absoluto;
es una instrucción vacía - la colocamos aquí porque la sintaxis del
bucle for exige al menos una instrucción dentro del cuerpo 
"""

print('\n'*2)

for i in range(10):
    print("número: ", i)


print('\n'*2)


#La invocación de la función range() puede estar equipada con dos argumentos
#la función range() solo acepta enteros como argumentos y genera secuencias de enteros

for i in range(2, 8):
    print("El valor de i es", i)

print('\n'*2)
#La función range() también puede aceptar tres argumentos
#El tercer argumento es un incremento

for i in range(2, 8, 3):
    print("El valor de i es", i)

print('\n'*2)
"""
hemos importado el módulo time y hemos utilizado
el método sleep() para suspender la ejecución de cada función posterior
de print() dentro del bucle for durante un segundo
"""
import time

# Escribe un bucle for que cuente hasta cinco.
    # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    # Cuerpo del bucle, emplea : time.sleep(1)

for i in range(1, 6):
    print(i," Mississippi")
    time.sleep(1)

# Escribe una función print con el mensaje final.
print("¡Listos o no, ahí voy!")

print("\n"*3)

"""
break - sale del bucle inmediatamente, e incondicionalmente termina la operación del bucle;
el programa comienza a ejecutar la instrucción más cercana después del cuerpo del bucle.

continue - se comporta como si el programa hubiera llegado repentinamente al final del cuerpo;
el siguiente turno se inicia y la expresión de condición se prueba de inmediato.
"""
# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

#break otro ejemplo
print('\n')

largest_number = -99999999
counter = 0

while True:
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")

#la variante con continue
print('\n')


largest_number = -99999999
counter = 0

number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

if counter:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")

#otro ejemplo con break
print('\n')

palabra_secreta = "hola"

while True:
    word = input("Dime una palabra: ")
    if word == palabra_secreta:
        break

print(" Has dejado el bucle con exito")

print('\n')
"""
CONTINUE- EL FEO DEVORADOR DE VOCALES
"""


# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
user_word = input("hola!, por favor introduce una palabra: ")
user_word = user_word.upper()

for letter in user_word:
    # Completa el cuerpo del bucle for.
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter, "\n")

print("\n"*4)
"""
CONTINUE- EL LINDO DEVORADOR DE VOCALES
"""
word_without_vowels = ""

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.
user_word = input("Ingresa una palabra: ")
user_word = user_word.upper()

for letter in user_word:
    # Completa el cuerpo del bucle.
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter
        
# Imprimir la palabra asignada a word_without_vowels.
print("la palabra resultante es: ", word_without_vowels)

#ALTURA DE PIRAMIDE CONOCIENDO EL NÚMERO DE BLOQUES
print("\n"*4)

bloques = int(input("Ingresa el número de bloques: "))
altura = 1
bloques_consumidos = 0
#
# Escribe tu código aquí.
#	
while bloques_consumidos < bloques:
    bloques -= 1
    altura += 1
    bloques_consumidos += altura

print("La altura de la pirámide:", altura)

print("\n"*4)
#LA HIPOTESIS DE COLLATZ

"""
toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
si es par, evalúa un nuevo c0 como c0 ÷ 2;
de lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1;
si c0 ≠ 1, salta al punto 2.
"""
print(
"""La hipótesis de Collatz dice que,
independientemente del valor inicial de c0,
el valor siempre tiende a 1.
"""
)

numero = int(input("Introduce un numero: "))

count = 0

while numero > 1:
    if numero % 2 == 0:
        numero //= 2
        print ("es par y el numero resultante es: ", numero)
        count += 1
    else: 
        numero = 3 * numero + 1
        print("es impar , asi que el numero resultante es: ", numero)
        count +=1
print("pasos = ", count)

"""
Los bucles while y for también pueden tener una cláusula else en Python.
La cláusula else se ejecuta después de que el bucle finalice su ejecución
siempre y cuando no haya terminado con break, por ejemplo:

n = 0
 
while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")
 
print()
 
for i in range(0, 3):
    print(i)
else:
    print(i, "else")
"""




