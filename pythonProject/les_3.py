import math
import numpy as np #alias
import random as rnd

# for _ in range(50):
#     print(round(rnd.uniform(1,10),2))

# eten = ["frieten","pizza","kebab"]
# print(rnd.choice(eten))

#While loops: kies een willekeurig getal tussen 1 en 7. Het programma stopt wanneer je het getal raadt.


# a = int(input("Geef het kleinste getal: "))
# b = int(input("Geef het grootste getal: "))
# if a > b:
#     a,b = b,a # PRO TIP!!
# getal = rnd.randint(a,b)
# # try: TRY EXCEPT METHODE (niet de beste denk ik)
# #     getal = rnd.randint(a,b)
# # except ValueError:
# #     getal = rnd.randint(b,a)
# guess = 0
# attempts = 0
# while guess != getal:
#     guess = int(input(f"Raad het getal tussen {a} en {b}: "))
#     attempts += 1
# print(f"Proficiat, je hebt het getal geraden in {attempts} pogingen")

#tafelkaart

for i in range(1,11):
    for j in range(1,11):
        print(i*j, end = " ") #\t kan ook, dat is tab
    print(" ")

#fibo

fibo_prev = 0
fibo = 0
fibo_new = 1

while fibo_new < 200:
    print(fibo_new)
    fibo = fibo_new
    fibo_new += fibo_prev
    fibo_prev = fibo

name = "Jorden"
for i in name:
    print(i, end = " ")

