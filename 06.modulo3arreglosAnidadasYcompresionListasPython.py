
##COMPRENSION DE LISTA: sintaxis especial para completar listas masivas

#El fragmento de código genera una lista de diez elementos y la rellena con cuadrados de diez números enteros que comienzan desde cero
squares = [x ** 2 for x in range(10)]
print(squares)

print("\n"*3)

##MATRIZ O ARREGLO DE DOS DIMENSIONES

#Creamos tablero de ajedred de 8*8


board = []
 
for i in range(8):
    row = [i for i in range(8)]
    board.append(row)
    
print(board)
 
print("\n"*2)

##LAS LISTAS DE COMPRENSION PUEDEN SER ANIDADAS, ACORTANDO EL CODIGO

board = [[i for i in range(8)] for j in range(8)]#La parte interna crea una fila, y la parte externa crea una lista de filas.
print(board)


print("\n"*2)

   
