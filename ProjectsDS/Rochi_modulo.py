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


---------------------------------

Rock, Paper, Scissors


rock = 1
paper = 2
scissor = 3

def get_inputs():
    player1 = int(input("Choose 1[rock], 2[paper], 3[scissor]:"))
    player2 = int(input("Choose 1[rock], 2[paper], 3[scissor]:"))
    if (player1 != 1 and player1 != 2 and player1 != 3) or (player2 != 1 and player2 != 2 and player2 != 3):
        print("Only there are 3 possibilities: [1, 2, 3]")
        player1, player2 = get_inputs()
        return player1, player2    
    else:
        return player1, player2

def p1_is_rock(p2):
    if p2 == rock:
        print("Draw")
    elif p2 == paper:
        print("Player 2 wins")
    elif p2 == scissor:
        print("Player 1 wins")

def p1_is_paper(p2):
    if p2 == rock:
        print("Player 1 wins")
    elif p2 == paper:
        print("Draw")
    elif p2 == scissor:
        print("Player 2 wins")

def p1_is_scissor(p2):
    if p2 == rock:
        print("Player 2 wins")
    elif p2 == paper:
        print("Player 1 wins")
    elif p2 == scissor:
        print("Draw")

def check_winner(player1_choose, player2_choose):
    print("player1_choose:", player1_choose)
    print("player2_choose:", player2_choose)
    if player1_choose == rock:
        p1_is_rock(p2=player2_choose)
    elif player1_choose == paper:
        p1_is_paper(p2=player2_choose)
    elif player1_choose == scissor:
        p1_is_scissor(p2=player2_choose)

g, h = get_inputs()
check_winner(player1_choose=g, player2_choose=h)


________________________________

Cows & Bulls

Say the number generated by the computer is 1038. An example interaction could look like this:

Welcome to the Cows and Bulls Game!

Enter a number:

1234

2 cows, 0 bulls

1253

1 cow, 1 bull

... Until the user guesses the number.

from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

number = str(random_with_N_digits(n=4))

cows_acum = 0

attemps = 0
while cows_acum < 4:
    answer = input("Insert a number: (Write 'STOP' to end the game)")
    cows_acum = 0
    bulls_acum = 0
    
    if answer.isnumeric() and len(answer) == 4:  # Is numeric? and has 4 digits?
        for pos, num in enumerate(number):
            if num == answer[pos]:  # Is a cow?
                cows_acum += 1
            elif num in answer: # Is a bull?
                bulls_acum += 1

        print("----------------")
        print("Your number:", answer)
        print("Cows:", cows_acum)
        print("Bulls:", bulls_acum)

    elif answer == "STOP":
        print("Cobarde")
        print("This was the number:", number)
        break
    
    attemps += 1
    if cows_acum == 4:
        print("You win")
        print("Number of attemps:", attemps)


__________________________
JSON

covid = json_readed["standard"]

with open('data_indented.json', 'w+') as outfile:
    json.dump(json_readed, outfile, indent=4)

df_json = pd.read_json("covid")