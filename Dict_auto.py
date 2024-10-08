#Merk, model, Bouwjaar, brandstof, km stand, en functie verander km stand
from tabulate import tabulate

auto = {"merk": "Ford",
        "model": "Focus",
        "bouwjaar": 2003,
        "brandstof": "diesel",
        "km_stand":200000}

for k,v in auto.items():
    print(k,v)

def change_km(auto):
    km_new = int(input("hoeveel km heeft de auto? "))
    auto["km_stand"] = km_new
    for k, v in auto.items():
        print(k, v)
change_km(auto)