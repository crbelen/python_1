##LA RAMA TRY-EXCEPT
""" try:
	# Es un lugar donde
	# tu puedes hacer algo 
    # sin pedir permiso.
except:
	# Es un espacio dedicado  
    # exclusivamente para pedir perdón."""
    
"""
Puedes ver dos bloques aquí:

el primero, comienza con la palabra clave reservada try este es el lugar
donde se coloca el código que se sospecha que es riesgoso y puede terminar en
caso de un error; nota: este tipo de error lleva por nombre excepción, mientras que
la ocurrencia de la excepción se le denomina generar - podemos decir que se genera
(o se generó) una excepción;

el segundo, la parte del código que comienza con la palabra clave reservada except 
esta parte fue diseñada para manejar la excepción; depende de ti lo que quieras hacer aquí: 
puedes limpiar el desorden o simplemente puede barrer el problema debajo de 
la alfombra (aunque se prefiere la primera solución) 
"""
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except:
    print('No se que hacer con', value)

print("\n"*2)
##DOS EXCEPCIONES DESPUES DE UN TRY
""" ambos except tienen nombres de excepción específicos. En esta variante, 
cada una de las excepciones esperadas tiene su propia forma de manejar el error, 
pero debe enfatizarse en que solo una de todas puede interceptar el 
control - si se ejecuta una, todas las demás permanecen inactivas."""

try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except ValueError:
    print('No se que hacer con', value)    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.') 

print("\n"*2)
##LA EXCEPCION PREDETERMINADA
#Puedes esperar que cuando se 
# genere una excepción y no haya un except dedicado a esa excepción,
# esta será manejada por la excepción por defecto.
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except ValueError:
    ('No se que hacer con.')    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')    
except:
    print('Ha sucedido algo extraño, ¡lo siento!')
    
##el except por defecto debe ser el último except

print("\n"*2)
##EXCEPCIONES MAS COMUNES

#ZeroDivisionError
""" operador de Python que puede hacer que se genere esta excepción: /, //, y %."""

#ValueError
"""En general, esta excepción se genera cuando una función (como int() o 
float()) recibe un argumento de un tipo adecuado, pero su valor es inaceptable. """

#TypeError
""" cuando intentas aplicar un dato cuyo tipo no se puede aceptar en el contexto actual"""
short_list = [1]
one_value = short_list[0.5]

print("\n"*2)
#AttributeError
"""La tercera línea de nuestro ejemplo intenta hacer uso de un método que no está incluido
en las listas. Este es el lugar donde se genera la excepción """
short_list = [1]
short_list.append(2)
short_list.depend(3)

print("\n"*2)
#SyntaxError
""" Es una mala idea manejar este tipo de excepciones en tus programas. Deberías
producir código sin errores de sintaxis, en lugar de enmascarar las fallas que has causado."""

print("\n"*2)
#KeyboardInterrupt
#se genera cuando el usuario presiona la tecla de interrupción (CTRL-C o Eliminar)

