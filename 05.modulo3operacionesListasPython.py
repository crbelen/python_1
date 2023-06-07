##Una REBANADA es un elemento de la sintaxis de Python que permite hacer una copia nueva de una lista, o partes de una lista.
#my_list[inicio:fin]


# Copiando la lista completa.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)


print("\n"*3)
# Copiando parte de la lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)


print("\n"*3)

##Si omites el start en tu rebanada, se supone que deseas obtener un segmento que comienza en el elemento con índice 0.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)


##Del mismo modo, si omites el end en tu rebanada, se supone que deseas que el segmento termine en el elemento con el índice len(my_list)
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)


print("\n"*3)

##el omitir el inicio y fin crea una copia de toda la lista:
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)

print("\n"*3)

##La instrucción DEL descrita anteriormente puede eliminar más de un elemento de la lista a la vez - también puede eliminar rebanadas:

my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

print("\n"*3)

my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)


print("\n"*3)

##Los operadores in y not in
"""
El primero de ellos (in) verifica si un elemento dado (el argumento izquierdo) está actualmente almacenado en algún lugar dentro de la lista
(el argumento derecho) - el operador devuelve True en este caso.

El segundo (not in) comprueba si un elemento dado (el argumento izquierdo) está ausente en una lista - el operador devuelve True en este caso.
"""
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)


print("\n"*3)


##ENCONTRAR EL VALOR MAYOR EN LA LISTA

#asumimos temporalmente que el primer elemento es el más grande y comparamos la hipótesis con todos los elementos restantes de la lista.
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list:
    if i > largest:
        largest = i
 
print(largest)


print("\n"*3)
#podemos usar una rebanada
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list[1:]:
    if i > largest:
        largest = i
 
print(largest)

print("\n"*3)


my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

print("\n"*3)


## encontremos la ubicación de un elemento dado dentro de una lista:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5 #aquí almacenamos el valor buscado
found = False #el estado actual de la busqueda se almacena en la variable found (True/False)
 
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:#cuando found se convierte en True, se sale del bucle
        break
 
if found:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")

print("\n"*3)


"""
Supongamos que has elegido los siguientes números en la lotería: 3, 7, 11, 42, 34, 49.

Los números que han salido sorteados son: 5, 11, 9, 42, 3, y 49.

La pregunta es: ¿A cuántos números le has atinado?
"""
drawn = [5, 11, 9, 42, 3, 49]#almacena todos los numeros sorteados
bets = [3, 7, 11, 42, 34, 49]#almacena los números con que se juega
hits = 0#cuenta los aciertos
 
for number in bets:
    if number in drawn:
        hits += 1
 
print(hits)

print("\n"*3)



##HACER UN PROGRAMA QUE ME ELIMINE LOS NUMEROS REPETIDOS EN LA LISTA

#crear una nueva lista como área de trabajo (my_list2)
#eliminar todas las repeticiones de numeros de la lista
# 
#
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

#clono en una lista nueva para manipularla

my_list2 =  my_list[:]
my_list2.sort()
print(my_list2)
listaResultante=[]
# ahora tengo que eliminar los elementos de la lista que se repiten

for i in my_list2:
    if i not in listaResultante:
        listaResultante.append(i)
    
print("La lista con elementos únicos:")
print(listaResultante)




