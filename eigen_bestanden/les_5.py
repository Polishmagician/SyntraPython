# def som_van_getallen(*args): #vangt onbepaald aantal argumenten op
#     return sum(args)
# print(som_van_getallen(5,8))
#
# #grootste getal van een onbepaalde reeks variabelen
#
# def grootste_getal(*args):
#     return max(args)
# print(grootste_getal(1,5,3,7,77,1,2))

#voeg een naam toe
# namen = ["Ben", "Benny", "Bart", "Bert"]
# namen.remove("Ben") #removen op naam
# namen.pop(0) #removen op index
# print(namen)

# lijst = ["Hasselt", "Genk", "Bilzen", "Zutendaal", "Hoeselt", "Lanaken"]
# keuze = ""
#
# while keuze.upper() != "STOP":
#     lf.toon_overzicht_functies()
#     keuze = input("Geef je keuze in: ")
#     if keuze == "1":
#         lf.toon_inhoud_lijst(lijst)
#     elif keuze == "2":
#         lf.voeg_item_toe(lijst)
#     elif keuze == "3":
#         lf.verwijder_uit_lijst(lijst)
#     elif keuze == "4":
#         lf.sorteer_lijst(lijst)
#     else:
#         print("Foute Invoer")
from colorama import Fore
print(Fore.RED + "red text")
print(Fore.GREEN + "green text")
