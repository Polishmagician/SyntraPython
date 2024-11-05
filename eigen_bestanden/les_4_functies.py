

def is_palindroom():
    woord = input("Geef me een woord: ")
    test = ""
    for l in woord:
        test = l + test
    print(test)
    if woord != test:
        print(f"{woord} is geen palindroom")
    else:
        print(f"{woord} is een palindroom")

def is_deelbaar():
    delers = [2,3,5,7,10,100]
    getal = int(input("Geef me een getal: "))
    for d in delers:
        if getal % d == 0:
            print(d, end=" ")
def volume_balk():
    b = float(input("Wat is de breedte: "))
    h = float(input("Wat is de hoogte: "))
    l = float(input("Wat is de lengte: "))
    procent = float(input("Wat is het percentage?: ")) / 100
    volume = b*h*l*procent
    print(f"Als de balk voor {procent*100}% gevuld is, dan is dat {volume} m3")
def willekeurig_geheel_tussen():
    import random as rnd
    x = int(input("Geef me het startpunt: "))
    y = int(input("Geef me het eindpunt: "))
    if x > y:
        x,y = y,x
    print(rnd.randint(x,y))
def tussen_10_100():
    getal = int(input("Geef een getal: "))
    if 10 <= getal <= 100:
        return True
    else:
        return False
def random_list():
    import random as rnd
    for i in range(10):
        print(rnd.randint(10,100))
def oppervlakte_formule():
    nummer = int(input("Geef het nummer van uw gewenste oppervlakteform: "))
    if nummer == 5:
        stop()
    if nummer == 1: #Vierkant
        vierkant()
    if nummer == 2: # Rechthoek
        rechthoek()
    if nummer == 3: # Driehoek
        driehoek()
    if nummer == 4: # Cirkel
        cirkel()
def vierkant():
    x = int(input("Geef de lengte van een zijde: "))
    opp = x*x
    print(opp)
def rechthoek():
    x = int(input("Geef de lengte van de korte zijde: "))
    y = int(input("Geef de lengte van de lange zijde: "))
    opp = x * y
    print(opp)
def driehoek():
    x = int(input("Geef de lengte van de basis zijde: "))
    y = int(input("Geef de hoogte: "))
    opp = x*(y/2)
    print(opp)
def cirkel():
    import math
    x = int(input("Geef de lengte van de straal: "))
    opp = math.pi * x*x
def stop():
    return



def keuze():
    keuze = int(input("Geef me uw keuze: "))
    if keuze == 1:
        is_palindroom()
    elif keuze ==2:
        is_deelbaar()
    elif keuze ==3:
        volume_balk()
    elif keuze ==4:
        willekeurig_geheel_tussen()
    elif keuze ==5:
        print(tussen_10_100())
    elif keuze ==6:
        random_list()
    elif keuze ==7:
        oppervlakte_formule()

# from les_4 import * # zo kan je functies van overal halen