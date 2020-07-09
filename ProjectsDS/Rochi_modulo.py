def suma_2(a, b):
    return a + b

def resta_2(a, b):
    return a - b


Bonus: ¿Cómo meterías estos dos elementos en una lista llamada missing
missing = []

for titulo in biblioteca:
    if titulo[1] == 0:
        faltante = titulo[0]
        print(faltante)
        missing.append(faltante)

c. Crea una variable que sea una lista llamada nuevo_libro en el que su primer elemento sea libro_1 y el segundo uds_1.

d. Convierte a nuevo_libro a tupla. (muestra qué tipo es ahora esta variable)

e. Añade nuevo_libro a la lista biblioteca


Acaban de traer una unidad más de El mal de Corcira, añade una unidad más al segundo elemento del primer elemento de la lista biblioteca.
t[1] = t[1]+1
t

biblioteca.append(nuevo_libro)
biblioteca

----------------------------------------------

def gusto(lista):

    input("Le gusta la montania? ")
    
    if == "No":
        funcion_zona(z)
    else:
        print("ok")

gusto(lista=lista_informacion)

----------------------------------------------


lista = ["alex", "begoña", "gabriel", "sara", "ataulfo"]

for k in lista:
    if k == "gabriel":
        continue
    print(k)

    for k, v in diccionario.items():
    print("k", k)
    print("v", v)
    if k == "dict":
        for x, y in v.items():
            print("x", x)
            print("y", y)
    print("-------------")

    # This file represents your module.
# Write the code...
----------------------------------------------

def mean_visualization():
    """ Draw the mean in a plot """
    return None
    pd.libraries

def open_file(path_file):
    """

    Args:
        path_file ([str]): Path where the file is.
    """
    #TODO (@rochilandia) This function must open a file

import numpy as np

x = np.arange(1, 6)
np.add.reduce(x)


----------------------------------------------

class Humano:
    def __init__(self, edad, altura, nombre):
        """Constructor de la clase"""
        self.edad = edad
        self.altura = altura
        self.nombre = nombre

    def cumplir_edad(self):
        self.edad += 1

    def registro_nombre(self):
        self.nombre = nuevo_nombre

wolfram = Humano(nombre="Wolfram", edad=23, altura=173)
print("Nombre antes del cambio:",wolfram.nombre)
print(wolfram.edad)
print(wolfram.altura, "cm")

wolfram.registro_nombre(nuevo_nombre="Benacio")
wolfram.cumplir_edad()
print("Benacio edad despues de hoy:\n", wolfram.edad)

----------------------------------------------

k = [0,1,2,3,4,5,6,7,8,9]
v = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

d = dict(zip(k,v))
d

for k,v in d.items():
    print(str(k) + ":" + str(v))

##imprime el diccionario sin llaves

----------------------------------------------
stops = [(9,0), (4,4), (7,3), (8,2), (3,4)]
print("1 Numero de paradas: ", len(stops))

lista_pasajeros = []

for pos, elem in enumerate(stops):
    if pos == 0:
        lista_pasajeros.append(elem[0])
    else:
        pasajeros_parada_anterior = lista_pasajeros[pos-1]
        lista_pasajeros.append(pasajeros_parada_anterior + elem[0] - elem[1])

print("2.Lista pasajeros por parada: ", lista_pasajeros)
print("3. Maximo ocupacion: ", max(lista_pasajeros))

--------------------------------------------------

l = [2,2,4,3,7,7,7,8,6,7,3,1,22,2,4,3,7,7,7,8,6,7,3,1,2]

def elementosrepetidos(lista):
    no_repetidos = []
    repetidos = []
    for elem in lista:
        if elem not in no_repetidos:
            no_repetidos.append(elem)
        else:
            repetidos.append(elem)
    repetidos = list(set(repetidos))

    print("No repetidos: ", no_repetidos)
    return repetidos

e=elementosrepetidos(lista=l)
e

----------------------------------------------

s = "Elefante"
n = 4

def n_gram(string, n):
    for pos, letter in enumerate(string):
        if pos+n <= len(string):
            print(string[pos:pos+n])

n_gram(string=s, n=n)

----------------------------------------------
pos va en orden. 
pos+n = tiene que ser igual o menor al largo de la cadena

def pregunta_recurrente():
    while True:
        x = input("Quiere parar?")
        if x == "STOP":
            break
        
pregunta_recurrente()

----------------------------------------------

stops = [(9,0), (4,4), (7,3), (8,2), (3,4)]
print("1 Numero de paradas: ", len(stops))

lista_pasajeros = []

for pos, elem in enumerate(stops):
    if pos == 0:
        lista_pasajeros.append(elem[0])
    else:
        pasajeros_parada_anterior = lista_pasajeros[pos-1]
        lista_pasajeros.append(pasajeros_parada_anterior + elem[0] - elem[1])

print("2.Lista pasajeros por parada: ", lista_pasajeros)
print("3. Maximo ocupacion: ", max(lista_pasajeros))

##OTRA MANERA DE HACERLO:

number_ocupants = 0
occupancy = []

for i,o in stops:
    number_ocupants += i
    number_ocupants -= o
    occupancy.append(number_ocupants)

print(occupancy)

----------------------------------------------
number_ocupants = 0
occupancy = []

for i in stops:
    number_ocupants = number_ocupants + i[0]-i[1]
    occupancy.append(number_ocupants)

print(occupancy)

----------------------------------------------

PANDAS

MASK
vendidos['item_name'] == 761
__________________________

First, we can add a formatted column that shows each type:

df['Sales_Type'] = df['Sales'].apply(lambda x: type(x).__name__)


___________________________

s = chipo['item_price'].astype(str)
chipo['item_price'] = s.str[0] + s.str[1:]
print (chipo)


chipo.apply(pd.to_numeric, downcast="float", errors="ignore")