import random 
from random import randint

moeda_possibilidades = ["cara", "coroa", "1", "2"]

moeda = random.choice(moeda_possibilidades)
print(f"O valor da moeda foi: {moeda}")

numero_aleatorio = randint(1,10)
print(f"O valor do número aleatório foi: {numero_aleatorio}")

cartas = ["rei", "dama", "valete"]

random.shuffle(cartas)
print(f"Cartas embaralhadas: {cartas}")