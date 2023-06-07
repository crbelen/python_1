"""
una variable que existe fuera de una función tiene alcance dentro del cuerpo de la función.
Esta regla tiene una excepción muy importante:

Una variable que existe fuera de una función tiene un alcance dentro del cuerpo de la función, excluyendo a aquellas que tienen el mismo nombre.
"""
def my_function():
    print("¿Conozco a la variable?", var)


var = 1
my_function()
print(var)

print("\n"*2)


def my_function_Excepcion():
    var = 2
    print("¿Conozco a la variable?", var)
 
 
var = 1
my_function_Excepcion()
print(var)


print("\n"*2)
##la palabra clave global
#puede extender el alcance de una variable incluyendo el cuerpo de las funciones (para poder no solo leer los valores de las variables sino también modificarlos).

#Este efecto es causado por la palabra clave reservada llamada global:
"""
global name
global name1, name2, ...
"""
def my_function_global():
    global var
    var = 2
    print("¿Conozco a aquella variable?", var)


var = 1
my_function_global()
print(var)

print("\n"*2)

""" si el argumento es una lista, el cambiar el valor del parámetro correspondiente no afecta la lista (recuerda: las variables que contienen listas son almacenadas de manera diferente que las escalares)
pero si se modifica la lista identificada por el parámetro (nota: ¡la lista, no el parámetro!), la lista reflejará el cambio."""

#no modifica la lista
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)
 
 
my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)
 
print("\n"*2)
#modifica la lista identificada por el parametro
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0] # Presta atención a esta línea.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)
 
 
my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

print("\n"*2)
