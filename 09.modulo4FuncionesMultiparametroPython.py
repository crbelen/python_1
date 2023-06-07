##CALCULO DEL IMC
#IMC = PESO EN KILOGRAMOS/ALTURA EN METROS CUADRADOS

def imc (peso, altura):
    
    if altura < 1.0 or altura >2.5 or \
    peso < 20 or peso > 200:
        return None
    
    return peso / altura ** 2

print(imc(80, 1.66))
print(imc(250, 1.64))
#el símbolo de diagonal invertida (\) es empleado. 
#Si se termina una línea de código con el, Python entenderá que la línea continua en la siguiente.
print("\n"*2)

#para convertir unidades del sistema inglés al sistema métrico. Comencemos con las pulgadas.
#Es bien conocido que 1 lb = 0.45359237 kg
#los pies y pulgadas: 1 ft = 0.3048 m, y 1 in(inch) = 2.54 cm = 0.0254 m
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
 
 
def lb_to_kg(lb):
    return lb * 0.4535923
 
 
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
 
    return weight / height ** 2
 
 
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))

print("\n"*2)
##VERIFICAR SI TRES LADOS PUEDEN FORMAR UN TRIANGULO

#LA FUNCION TENDRA TRES PARAMETROS

def is_a_triangle(lado1, lado2, lado3):
    if lado1 + lado2 <= lado3:
        return False
    elif lado2 + lado3 <= lado1:
        return False
    elif lado3 + lado1 <= lado2:
        return False
    else:
        return True
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 2, 3))

print("\n"*2)
#versión más compacta:
def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True
 
 
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

print("\n"*2)
#se puede compactar aun mas y obtener una expresion universal para probar triangulos
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
 
 
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

print("\n"*2)
##Triángulos y el Teorema de Pitágoras
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


a = float(input('Ingresa la longitud del primer lado: '))
b = float(input('Ingresa la longitud del segundo lado: '))
c = float(input('Ingresa la longitud del tercer lado: '))

if is_a_triangle(a, b, c):
    print('Si, si puede ser un triángulo.')
else:
    print('No, no puede ser un triángulo.')

print("\n"*2)
#ahora intentaremos verificar si es un triangulo rectangulo con el Teorema de Pitagoras c**2 = a**2 + b**2
#la hipotenusa es el lado mas largo
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2 
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))

print("\n"*2)

##EVALUAR EL AREA DE UN TRIANGULO
##FORMULA DE HERON 
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
 
 
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
 
 
def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)
 
 
print(area_of_triangle(1., 1., 2. ** .5))

print("\n"*2)

##FUNCION QUE CALCULA FACTORIALES
#UN FACTORIAL SE EXPRESA CON UN SIGNO DE EXCLAMACION Y ES
#EL PRODUCTO DE TODOS LOS NUMEROS NATURALES PREVIOS AL ARGUMENTO DADO

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1 
    
    product = 1
    for i in range(2, n+1):
        product *= i
    return product

for n in range (1, 6):
    print (n, factorial_function(n))

print("\n"*2)
##NUMEROS FIBONACCI
#el primero y segundo son ambos igual a 1,
#los restantes son el resultado de la suma de los 
#dos numeros anteriores

def fib(n):
    if n <1:
        return None
    if n < 3:
        return 1
    elem_1 = elem_2 = 1
    suma = 0
    for i in range(3, n+1):
        suma = elem_1 + elem_2
        elem_1, elem_2 = elem_2, suma
    return suma

for n in range (1, 10):
    print(n, "->", fib(n))


print("\n"*2)
##RECURSIVIDAD
#Tecnica donde una funcion se invoca a si misma
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

print("\n"*2)

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)
for n in range (1, 6):   
    print (n, "->", factorial_function(n))

