# program.py (extracto de program.py)
sum = 1 + 2
print(sum)

print('Hola desde la consola')

sum = 1 + 2 # 3
product = sum * 2
print(product)

planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367 # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11" #string

# Declaramos la variable
distancia_a_alfa_centauri = 4.367

# Descubrimos su tipo de dato
print(type(distancia_a_alfa_centauri))

left_side = 10
right_side = 5
left_side / right_side # 2

# Importamos la biblioteca 
from datetime import date

# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
print(date.today())

# Tu turno ejecuta el siguiente comando: print("Today's date is: " + str(date.today()))
print("Today's date is: " + str(date.today()))

# Escribe tu código aquí
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)


# Escribe tu código aquí
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(int(first_number) + int(second_number))
