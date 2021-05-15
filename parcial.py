
from random import randint, random
from consumo_api import get_charter_by_id, get_all_sw_characters

personaje1 = get_charter_by_id(randint(1, 83))
personaje2 = get_charter_by_id(randint(1, 83))

# COMPARAR LA ALTURA DE 2 PERSONAJES
def height(item):
    if(item["height"].isdecimal()):
        return int(item["height"])
    else:
        return -1

if(personaje1["height"]) > (personaje2["height"]):
        print(personaje1["name"]),
else: print(personaje2["name"])


# COMPARAR EL PESO DE 2 PERSONAJES
def mass(item):
    if(item["mass"].isdecimal()):
        return int(item["mass"])
    else:
        return -1

if(personaje1["mass"]) > (personaje2["mass"]):
        print(personaje1["name"]),
else: print(personaje2["name"])

# COMPARAR LA PARTICIPACION EN PELICULA DE 2 PERSONAJES
MoreMovies = personaje1 if len(personaje1["films"]) > len(personaje2["films"]) else personaje2
print("Quien participo en mas peliculas es: " + str(MoreMovies.get("name")))


# COMPARAR SI ALGUNO DE LOS 2 PERSONAJES ES YODA O GRIEVOUS
if((personaje1["name"]) == "Yoda"):
    print (personaje1["name"], "es Yoda"),
elif((personaje1["name"]) == "Grievous"):
    print (personaje1["name"], "es Grievous"),
else: print(personaje1["name"], "no es Yoda o Grievous")

if((personaje2["name"]) == "Yoda"):
    print (personaje2["name"], "es Yoda"),
elif((personaje2["name"]) == "Grievous"):
    print (personaje2["name"], "es Grievous"),
else: print(personaje2["name"], "no es Yoda o Grievous")


# ORDENAR PERSONAJES POR NOMBRE

sw_nombres = get_all_sw_characters()

def name(item):
    return item["name"]

sw_nombres.sort(key=name)

for index, character in enumerate(sw_nombres):
    print(character["name"],"es de la especie:", character["species"],"y es del planeta:", character["homeworld"])

# LEN para sacar la cantidad de peliculas
for index, character in enumerate(sw_nombres):
    if(len(character["films"])) == 7:
        print(character["name"])


# LISTA DE 77 NUMEROS ALEATORIOS
randomlist = []
for i in range(0, 77):
    numbers = randint(1,100)
    if numbers % 2 != 0:
        randomlist.append(numbers)

# VALOR MENOR
print(min(randomlist))

# VALOR MAYOR
print(max(randomlist))

# LISTA ORDENADA
randomlist.sort()
print(randomlist)
