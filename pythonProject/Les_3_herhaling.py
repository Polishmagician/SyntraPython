import random as rnd

# rnd.randint(1,10) #Int
# rnd.uniform(1.5,10.2) #Float
#
# for i in range(100):
#     print(i)
# for i in range(1,101):
#     print(i)
# for i in range(1,101,5): #steps
#     print(i)

#Balk voor 70% gevuld, hoeveel m3 is dat
# b = float(input("Wat is de breedte: "))
# h = float(input("Wat is de hoogte: "))
# l = float(input("Wat is de lengte: "))
# procent = float(input("Wat is het percentage?: "))/100
# volume = b*h*l*procent
# print(f"Als de balk voor {procent*100}% gevuld is, dan is dat {volume} m3")
# print("Als de balk voor {}% gevuld is, dan is dat {} m3".format(procent*100,volume))

#Opdracht: schrijf een programma dat zegt dat een getal deelbaar is door 2,3,5,7 en 10

getal = int(input("Geef me een getal: "))
delers = [2,3,5,7,10]

for d in delers:
    if getal%d ==0:
        print(d, end = " ")