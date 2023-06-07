"""
TABLA DE PRIORIDADES CON LOS OPERADORES
Prioridad	Operador	
1	+, -	unario
2	**	
3	*, /, //, %	
4	+, -	binario
5	<, <=, >, >=	
6	==, !=	
"""
#EJERCICIO
"""
Usando uno de los operadores de comparación en Python, escribe un programa simple de dos líneas que tome el parámetro n como entrada, que es un entero,
e imprime False si n es menor que 100, y True if n es mayor o igual que 100.
"""

n = int(input("Ingresa un número: "))
print(n >= 100)

print("\n"*3)

#Ejecución condicional: la sentencia if
#Ejecución condicional: la sentencia if-else
#La sentencia elif

print('¿cómo identificar el mayor de los dos números?:', '\n')

# Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
 
# Elige el número más grande
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
 
# Imprime el resultado
print("El número más grande es:", larger_number, '\n'*2)

print('encontremos el mayor de los tres numeros', '\n')
# Se leen tres números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))
 
# Asumimos temporalmente que el primer número
# es el más grande.
# Lo verificaremos pronto.
largest_number = number1
 
# Comprobamos si el segundo número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number2 > largest_number:
    largest_number = number2
 
# Comprobamos si el tercer número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number3 > largest_number:
    largest_number = number3
 
# Imprime el resultado.
print("El número más grande es:", largest_number)


print("\n"*3)
#otra forma de hacerlo con elif
# Se leen tres números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

if number1 > number2 & number1 > number3:
    numero_mayor = number1
elif number2 > number1 & number2 > number3:
    numero_mayor = number2
else:
    numero_mayor = number3
    
print("El número más grande es: ", numero_mayor)

print("\n"*3)
#otra forma de hacerlo

# Se leen tres números.
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))
 
# Verifica cuál de los números es el mayor
# y pásalo a la variable largest_number.
 
largest_number = max(number1, number2, number3)
 
# Imprime el resultado.
print("El número más grande es:", largest_number)

#a continuación un bucle:
largest_number = -999999999
number = int(input())
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Ir a la línea 02

print("\n"*3)

name = input("Introduce el nombre de la flor: ")

if name == "ESPATIFILIO":
    print("Si, ¡El ESPATIFILIO es la mejor planta de todos los tiempos!")
elif name == "espatifilo":
    print("No, ¡quiero un gran ESPATIFILIO!")
else:
    print("¡ESPATIFILIO!, ¡No", name + "!")

print("\n"*3)
"""
si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal).
si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos.
Si el impuesto calculado es menor que cero, solo significa que no hay impuesto (el impuesto es igual a cero)

"""
income = float(input("Introduce el ingreso anual: "))

if income < 85528:
	tax = income * 0.18 - 556.02
else:
	tax = (income - 85528) * 0.32 + 14839.02

if tax < 0.0:
	tax = 0.0

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")

print("\n"*3)
#AÑO BISIESTO O COMUN
year = int(input("Introduce un año: "))

if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
	if year % 4 != 0:
		print("Año Común")
	elif year % 100 != 0:
		print("Año Bisiesto")
	elif year % 400 != 0:
		print("Año Común")
	else:
		print("Año Bisiesto")


print("\n"*3)
