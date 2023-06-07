##No se debe invocar una función antes de que se haya definido.

##Una función y una variable no pueden compartir el mismo nombre.

def message(): # definiendo una función
    print("Hello") # cuerpo de la función
 
message() # invocación de la función

print("\n"*2)

#funcion con argumentos
def hello(name): # definiendo una función
    print("Hello,", name) # cuerpo de la función
 
 
name = input("Ingresa tu nombre: ")
 
hello(name) # invocación de la función

print("\n"*2)

##FUNCIONES PARAMETRIZADAS

"""
especificar uno o más parámetros en la definición de
la función es un requerimiento, y se debe de cumplir durante
la invocación de la misma. Se debe proveer el mismo número
de argumentos como haya parámetros definidos.
"""

def message(number):
    print("Ingresa un número:", number)

print("\n"*2)

##Paso de argumentos de palabra clave
#el significado del argumento está definido por su nombre, no su posición
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)
 
introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

print("\n"*2)
#Es posible combinar ambos tipos si se desea - solo hay una regla
#inquebrantable: se deben colocar primero los argumentos posicionales y después los de palabra clave.

##VALOR DE PARAMETRO POR PREDETERMINADA 
#El valor por predeterminada para el parámetro se asigna de la siguiente manera:
def introduction(first_name="Juan", last_name="González"):
    print("Hola, mi nombre es", first_name, last_name)
introduction()

#Si solo se especifica un argumento de palabra clave, el restante tomará
#el valor por predeterminada:
introduction(last_name="Rodríguez")

print("\n"*2)
##a instrucción return

#return sin una expresión

def happy_new_year(wishes = True):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return
 
    print("¡Feliz año nuevo!")

print("\n"*2)

#return con una expresión ->"transporta" el valor de la expresión al lugar donde se ha invocado la función.
def boring_function():
    return 123
 
x = boring_function()
 
print("La función boring_function ha devuelto su resultado. Es:", x)


print("\n"*2)

##NONE
"""
None es una palabra clave reservada.

Solo existen dos tipos de circunstancias en las que None se puede usar de manera segura:

    cuando se le asigna a una variable (o se devuelve como el resultado de una función)
    cuando se compara con una variable para diagnosticar su estado interno.
"""
def strange_function(n):
    if(n % 2 == 0):
        return True

print(strange_function(2))
print(strange_function(1))

print("\n"*2)
##¿Se puede enviar una lista a una función como un argumento?
def list_sum(lst):
    s = 0
 
    for elem in lst:
        s += elem
 
    return s

print(list_sum([5, 4, 3]))


print("\n"*2)
## ¿Puede una lista ser el resultado de una función?
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))


print("\n"*2)
##LABORATORIOS

#¿ES AÑO BISIESTO?
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0 & year % 400 != 0:
        return False
    else:
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"-> ",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")

print("\n"*2)
##CUANTOS DÍAS TIENE EL MES DE TAL AÑO
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0 & year % 400 != 0:
        return False
    else:
        return True
    
def days_in_month(year,month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

print(days_in_month(2023, 2))

test_years = [1900, 2000, 2016, 1987]
test_months = [ 2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr,mo,"-> ",end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")



print("\n"*2)
##DIA DEL AÑO
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0 & year % 400 != 0:
        return False
    else:
        return True
    
def days_in_month(year,month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

def day_of_year(year, month, day):
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None

print(day_of_year(2000, 12, 31))


##ENCONTRAR NÚMERO PRIMO
print("\n"*2)

def is_prime(num):
    for i in range (2, num):
        if num % i == 0:
            return False
    return True
    

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

##PASAR DE LITRO A LOS CIEN -- A MILLAS POR GALON
def liters_100km_to_miles_gallon(liters):
    miles = 100000 / 1609.344 #en cien km hay x millas
    gallon = liters /3.785411784 # en x litros hay tantos galones
    result = miles * gallon
    return result

   
