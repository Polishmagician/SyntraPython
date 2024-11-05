def honderd_veelvouden():
    getal = int(input("Geef een getal: "))
    lijst = []
    for i in range(1,101):
        lijst.append(i*getal)
    print(lijst)
#honderd_veelvouden()

def even_oneven():
    lijst = []
    for i in range(10):
        element = int(input("Geef een getal: "))
        lijst.append(element)
    even = []
    oneven = []
    for item in lijst:
        if item%2 == 0:
            even.append(item)
        else:
            oneven.append(item)
    print(f"Dit zijn even getallen: {even}")
    print(f"Dit zijn oneven getallen: {oneven}")
# even_oneven()

def som_tien_getallen():
    lijst = []
    sum = 0
    for i in range(10):
        element = int(input("Geef een getal: "))
        lijst.append(element)
        sum += element
    print(sum)
# som_tien_getallen()

def gemiddelde_lijst(lijst: list):
    gemiddelde = sum(lijst)/len(lijst)
    print(gemiddelde)
# gemiddelde_lijst([1,5,7,8,3])

def string_to_list():
    woord = input("Geef een woord in: ")
    lijst = []
    for letter in woord:
        lijst.append(letter)
    print(lijst)
# string_to_list()