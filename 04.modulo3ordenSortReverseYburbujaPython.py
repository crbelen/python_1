##ORDENAMIENTO BURBUJA INTERACTIVO

#Creamos una variable llamada swapped, y le asignamos un valor de False para indicar que no hay intercambios. De lo contrario, se le asignará True.
# su tarea es observar si se ha realizado algún intercambio durante el pase o no

my_list = []
swapped = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nOrdenada:")
print(my_list)

print("\n"*3)
##ORDENAMIENTO LISTA RAPIDO METODO SORT()

my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)


print("\n"*3)
#También hay un método de lista llamado REVERSE(), que puedes usar para invertir la lista, por ejemplo:
lst = [5, 3, 1, 2, 4]
print(lst)
 
lst.reverse()
print(lst)

print("\n"*3)
