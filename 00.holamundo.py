print("hola mundo")
print("Hisssssss...")

print("\n")

"""Un argumento de palabra clave consta de tres elementos: una
palabra clave se identifica el argumento (end aquí); un signo de igual (=); y un valor asignado a ese argumento"""
#cualquier argumento de palabra clave debe colocarse después del último argumento posicional (esto es muy importante)

print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")

"""Dijimos anteriormente que la función print() separa sus argumentos de salida con espacios. Este comportamiento también se puede cambiar.
El argumento de palabra clave que puede hacer esto se denomina sep (como en separador)."""

print("Mi", "nombre", "es", "Monty", "Python.", sep="-")

print("\n", "Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

print("--------------------------\n")
print("Programming","Essentials","in", sep="***", end="...")
print("Python")


print("estoy probando multiplicar cadena string","dejo 5 saltos de linea\n"*5,"*******************\n"*2)


print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

#minimizar el número de invocaciones de la función print() insertando \n en las cadenas

print("    *", "   * *", "  *   *", " *     *", "***   ***", "  *   *", "  *   *",
      "  *****", sep="\n")

#hacer que la flecha sea el doble de grande (pero mantener las proporciones)

print("     *", end="\n"*2)
print("   *   *", end="\n"*2)
print("  *     *", end="\n"*2)
print(" *       *", end="\n"*2)
print("***     ***", end="\n"*2)
print("  *     *", end="\n"*2)
print("  *     *", end="\n"*2)
print("  *******", end="\n"*2)


print("     *","   *   *"," *       *","***     ***", "  *     *",
      "  *     *", "  *******",sep="\n"*2)

print("    *")
print("   * *", sep=" "*2)
print("  *   *")
print(" *     *")
print("* *   * *")
print("  *   *")
print("  *   *")
print("  *****")

"""soluciones propuestas por el curso"""
print("original version:")
###################
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
###################
print("with fewer 'print()' invocations:")
###################
print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")
###################
print("higher:")
###################
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")
###################
print("doubled:")
###################
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)

"""Un literal se refiere a datos cuyos valores están determinados por el literal mismo.
Los literales son notaciones para representar valores fijos en el código. Python tiene varios tipos de literales - es decir, un literal puede ser un número por ejemplo, 123),
o una cadena (por ejemplo, "Yo soy un literal.").
Se utilizan literales para codificar datos y ponerlos dentro del código.
Si se codifica un literal y se coloca dentro del código de Python, la forma del literal
determina la representación (tipo) que Python utilizará para almacenarlo en la memoria.
Python 3.6 ha introducido el guion bajo en los literales numéricos, permitiendo colocar
un guion bajo entre dígitos y después de especificadores de base para mejorar la legibilidad.
Esta característica no está disponible en versiones anteriores de Python.

¿Cómo se codifican los números negativos en Python?
Como normalmente se hace, agregando un signo de menos.
Se puede escribir: -11111111, o -11_111_111."""

"""El punto decimal es esencialmente importante
para reconocer números punto-flotantes en Python.
4 es un número entero mientras que 4.0 es un número punto-flotante.
El punto decimal es lo que determina si es flotante."""

#La letra E (también se puede utilizar la letra minúscula e - proviene de
#la palabra exponente) la cual significa por diez a la n potencia.
#El exponente (el valor después de la E) debe ser un valor entero;
#La base (el valor antes de la E) puede ser un valor entero o flotante.
# Python siempre elige la presentación más corta del número, y esto se debe de tomar en consideración al crear literales.

print("\n")
print('Me gusta "Monty Python"')
print("Me gusta \"Monty Python\"")
"""carácter de escape: La diagonal invertida puede también escapar de la comilla. Una comilla precedida por una diagonal
invertida cambia su significado - no es un limitador, simplemente es una comilla.  """

print('"Estoy"', '""aprendiendo""', '"""Python"""', sep="\n")

#Existe un literal especial más utilizado en Python: el literal None.
#Este literal es llamado un objeto de NoneType,
#y puede ser utilizado para representar la ausencia de un valor.

print("\n")


"""OPERADORES BASICOS"""
print("EXPONENTACION", "\n")
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
#Cuando ambos ** argumentos son enteros, el resultado es entero, también;
#Cuando al menos un ** argumento es flotante, el resultado también es flotante.

print("\n","Multiplicación")
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

print("\n","division")
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
print("\n","El resultado producido por el operador de división siempre es flotante")

print("\n","division entera //")
print(6 // 4)
print(6. // 4)
print("\n","el redondeo siempre va hacia abajo")
print("\n","La division entera también se le suele llamar en inglés floor division.")

print("\n","Residuo (módulo)")
print(14 % 4)
print(12 % 4.5)

print("\n","Suma")
print(-4 + 4)
print(-4. + 8)


print("\n","Resta y operador unario")
print(-4 - 4)
print(4. - 8)
print(-1.1)
print(+2)

"""
Prioridad	Operador	
1	**	
2	+, - (nota: los operadores unarios a la derecha del operador exponencial enlazan con mayor fuerza.)	unario
3	*, /, //, %	
4	+, -	binario

Nota: se han enumerado los operadores en orden de la más alta (1) a la más baja (4) prioridad.
Las sub-expresiones dentro de paréntesis siempre se calculan primero.
"""


#VARIABLES

var = "3.8.5"
print("Python version: " + var)
print("\n")


juan = 3
maria = 5
adan = 6
print(juan, maria, adan, sep=", ")
total_apples= juan + maria + adan
print ("el numero total de manzanas es: ", total_apples, end="\n"*2)


kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

#round redondea la salida del resultado al número de decimales
#especificados en el paréntesis

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

print("\n"*2)


#INPUT
#el resultado de la función input() es una cadena.
"""
La función int() toma un argumento (por ejemplo, una cadena: int(string)) e
intenta convertirlo a un valor entero; si llegase a fallar, el programa entero
fallará también (existe una manera de solucionar esto);
La función float() toma un argumento (por ejemplo,
una cadena: float(string)) e intenta convertirlo a flotante (el resto es lo mismo).
"""
anything = float(input("Ingresa un número: "))
something = anything ** 2.0
print(anything, "a la potencia de 2 es", something)

print("\n"*2)
"""
El signo de + (más), al ser aplicado a dos
cadenas, se convierte en un operador de concatenación:
"""
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")

print("\n"*2)

"""
El signo de * (asterisco), cuando es aplicado a una cadena y a un
número (o a un número y cadena) se convierte en un operador de replicación:
"""
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

print("\n"*2)

"""
name = input("Ingresa tu nombre: ")
print("Hola, " + name + ". '¡Gusto en conocerte'!")
 
print("\nPresiona Enter para terminar el programa.")
input()
print("FIN.")
"""

"""ejercicio calculo hora fin dada una hora de inicio y duracion de evento:
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
mins = mins + dura # encuentra el número total de minutos
hour = hour + mins // 60 # encuentra el número de horas ocultas en los minutos y actualiza las horas
mins = mins % 60 # corrige los minutos para que estén en un rango de (0..59)
hour = hour % 24 # corrige las horas para que estén en un rango de (0..23) 
print(hour, ":", mins, sep='')
"""


