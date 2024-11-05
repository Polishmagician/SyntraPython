import random as rd
from os import remove

#Lambda functies

f1 = lambda a,b : a*2+b
f2 = lambda a,b : a**2+b**2
f3 = lambda a,b : (a+b)**2
f4 = lambda a : a/3 if a%3 == 0 else a*2
f5 = lambda a,b : a/2 if a>b**2 else a*2
f6 = lambda a,b,c : c-(a+b) if (a+b) < c else a + b + c

# print(f1(4,2))
# print(f2(5,3))
# print(f3(4,3))
# print(f4(6))
# print(f4(5))
# print(f5(10,2))
# print(f6(2,5,3))

vierkant = lambda b : b**2
rechthoek = lambda b,h : b*h
driehoek = lambda b,h : b*h/2
kubus = lambda b : b**3
balk = lambda l,b,h : l*b*h
cilinder = lambda r,h : 3.14*r**2*h

def interface():
    functie = ""
    while functie != "Stop":
        print("1: vierkant", "2: rechthoek", "3: driehoek", "4: kubus", "5: balk", "6: cilinder", "'Stop': end")
        functie = input("Welke functie wil je gebruiken?")
        if functie == "1":
            print(vierkant(int(input("Geef b: "))))
        elif functie == "2":
            print(rechthoek(int(input("Geef b: ")),int(input("Geef h: "))))
        elif functie == "3":
            print(driehoek(int(input("Geef b: ")),int(input("Geef h: "))))
        elif functie == "4":
            print(kubus(int(input("Geef b: "))))
        elif functie == "5":
            print(balk(int(input("Geef l: ")),int(input("Geef b: ")),int(input("Geef h: "))))
        elif functie == "6":
            print(cilinder(int(input("Geef r: ")),int(input("Geef h: "))))
# interface()

euro_d = lambda e : e*1.1
pond_d = lambda p : p*1.3
euro_p = lambda e : e*0.83
pond_e = lambda p : p*1.2

#genereer 100 getallen van 10,200 en steek ze in 4 lijsten
def lijst_random():
    lijst1 = []
    lijst2 = []
    lijst3 = []
    lijst4 = []
    for f in range(100):
        getal = rd.randint(10,200)
        if f%4 ==0:
            lijst1.append(getal)
        elif f%4 ==1:
            lijst2.append(getal)
        elif f%4 ==2:
            lijst3.append(getal)
        else:
            lijst4.append(getal)
    lijst_tot = [lijst1, lijst2, lijst3, lijst4]
    for rij in lijst_tot:
        for item in rij:
            print(item, end = "\t")
        print()
lijst_random()

autos = ["BMW", "Mercedes", "Audi", "Ford"]
def verwijder_auto(autos):
    while True:
        print(autos)
        car_to_remove = input("Geef de auto die ik moet verwijderen: ")
        if car_to_remove == "stop":
            break
        elif car_to_remove in autos:
            autos.remove(car_to_remove)
        else:
            print("Auto niet in lijst")
    print(autos)
def voeg_auto_toe(autos):
    while True:
        print(autos)
        car_to_add = input("Geef de auto die ik moet toevoegen: ")
        if car_to_add == "stop":
            break
        elif car_to_add not in autos:
            autos.append(car_to_add)
            break
        else:
            print("Auto reeds in lijst")
    print(autos)

#verwijder_auto(autos)
#voeg_auto_toe(autos)


