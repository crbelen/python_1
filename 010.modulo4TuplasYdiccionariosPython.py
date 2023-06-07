##TUPLAS (INMUTABLES Y ENTRE PARENTESIS)
#Las Tuplas son colecciones de datos ordenadas e inmutables. Se puede pensar en ellas
# como listas inmutables. Se definen con paréntesis
my_tuple = (1, 2, True, "una cadena", (3, 4), [5, 6], None)
print(my_tuple)
 
my_list = [1, 2, True, "una cadena", (3, 4), [5, 6], None]
print(my_list)

print("\n"*2)
# tupla vacía
empty_tuple = ()
print(type(empty_tuple))


print("\n"*2)
#La tupla de un solo elemento se define de la siguiente manera:
one_elem_tuple_1 = ("uno", ) # Paréntesis y una coma.
one_elem_tuple_2 = "uno", # Sin paréntesis, solo la coma.

print("\n"*2)

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)


print("\n"*2)
##También se puede crear una tupla utilizando la función integrada de Python tuple(). 
# Esto es particularmente útil cuando se desea convertir un iterable (por ejemplo, una lista, rango, cadena, etcétera) en una tupla:
my_tuple = tuple((1, 2, "cadena"))
print(my_tuple)
 
my_list = [2, 4, 6]
print(my_list) # salida: [2, 4, 6]
print(type(my_list)) # salida: <class 'list'>
tup = tuple(my_list)
print(tup) # salida: (2, 4, 6)
print(type(tup)) # salida: <class 'tuple'>

print("\n"*2)
##DICCIONARIO
#un diccionario es un conjunto de pares de key y value (ES MUTABLE)
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

# Imprimir valores aquí.
print(dictionary)
print(phone_numbers)
print(empty_dictionary)

"""si una clave es una cadena, se tiene que especificar como una cadena;
las claves son sensibles a las mayúsculas y minúsculas """
print(dictionary['gato'])
print(phone_numbers['Suzy'])

print("\n"*2)
##El método keys()
"""
¿Pueden los diccionarios ser examinados utilizando el bucle for, como las listas o tuplas?

No, porque un diccionario no es un tipo de dato secuencial - el bucle for no es útil aquí.

Si, porque hay herramientas simples y muy efectivas que pueden adaptar cualquier diccionario 
a los requerimientos del bucle for (en otras palabras, se construye un enlace intermedio entre 
el diccionario y una entidad secuencial temporal).

El primero de ellos es un método denominado keys(), el cual es parte de todo diccionario. 
El método retorna o regresa una lista de todas las claves dentro del diccionario. Al tener una
lista de claves se puede acceder a todo el diccionario de una manera fácil y útil.
"""
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for key in dictionary.keys():
    print(key, "->", dictionary[key])
 
 
 
print("\n"*2)
##el método items()
"""
Este método retorna una lista de tuplasdonde cada tupla es
un par de cada clave con su valor.
"""
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for spanish, french in dictionary.items():
    print(spanish, "->", french)


print("\n"*2)
##Modificar, agregar y eliminar valores
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary['gato'] = 'minou'
print(dictionary)


print("\n"*2)
##La función sorted() para que la salida este ordenada
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
for key in sorted(dictionary.keys()):    
    print(key, "->", dictionary[key])
    


print("\n"*2)   
##Agregando nuevas claves
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary.update({"pato": "canard"})
print(dictionary)

#otra forma:
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary['cisne'] = 'cygne'
print(dictionary)


print("\n"*2)
##Eliminado una clave
#al eliminar la clave también se removerá el valor asociado. Los valores no pueden existir sin sus claves.
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
del dictionary['perro']
print(dictionary)

#para eliminar el ultimo elemento de un diccionario
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary.popitem()
print(dictionary)

print("\n"*2)
##Para eliminar todos los elementos de un diccionario se debe emplear el método clear():
pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
    }
 
print(len(pol_esp_dictionary)) # salida: 3
del pol_esp_dictionary["zamek"] # eliminar un elemento
print(len(pol_esp_dictionary)) # salida: 2
 
pol_esp_dictionary.clear() # eliminar todos los elementos
print(len(pol_esp_dictionary)) # salida: 0
 
del pol_esp_dictionary # elimina el diccionario

print("\n"*2)
# #Para copiar un diccionario, emplea el método copy():
pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
    }
 
copy_dictionary = pol_esp_dictionary.copy()

print("\n"*2)
##trabajando juntos TUPLAS Y DICCIONARIOS
#NOTAS DE UNA CLASE
""" línea 1: crea un diccionario vacío para ingresar los datos; el nombre del alumno es empleado como clave, mientras que todas las calificaciones asociadas son almacenadas en una tupla (la tupla puede ser el valor de un diccionario, esto no es un problema)
línea 3: se ingresa a un bucle "infinito" (no te preocupes, saldrémos de el en el momento indicado)
línea 4: se lee el nombre del alumno aquí;
línea 5-6: si el nombre es una cadena vacía (), salimos del bucle;
línea 8: se pide la calificación del estudiante (un valor entero en el rango del 0-10)
línea 9-10: si la puntuación ingresada no está dentro del rango de 0 a 10, se abandona el bucle;
línea 12-13: si el nombre del estudiante ya se encuentra en el diccionario, se alarga la tupla asociada con la nueva calificación (observa el operador +=)
línea 14-15: si el estudiante es nuevo (desconocido para el diccionario), se crea una entrada nueva, su valor es una tupla de un solo elemento la cual contiene la calificación ingresada;
línea 17: se itera a través de los nombres ordenados de los estudiantes;
línea 18-19: inicializa los datos necesarios para calcular el promedio (sum y counter).
línea 20-22: se itera a través de la tupla, tomado todas las calificaciones subsecuentes y actualizando la suma junto con el contador.
línea 23: se calcula e imprime el promedio del alumno junto con su nombre."""
school_class = {}
while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break
    
    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
        break
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)
  
 
print("\n"*2) 
##convertir la tupla colors en un diccionario.
colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)
print(colors_dictionary)
  

