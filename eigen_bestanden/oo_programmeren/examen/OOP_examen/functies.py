from data import *
from tabulate import tabulate


#Data is een lijst met objecten
data = classes_data

def toon_wagen(data):
    filter_list = []
    for d in data:
        new = [d.id, d.merk, d.model, d.bouwjaar, d.brandstof, d.huurprijs]
        filter_list.append(new)

    print(tabulate(filter_list, headers=Wagen.column_headers()))


def voeg_wagen_toe(data):
    ids = []
    for row in data:
        ids.append(int(row.id))
    new_data = tuple([input(f"Geef {i} ")for i in Wagen.column_headers()[1:]])
    data.append(Wagen(max(ids)+1,*new_data))
    print("Wagen toegevoegd")
    return data


def verwijder_wagen(data):
    toon_wagen(data)
    keuze = input("Welke ID wil je verwijderen? ")
    for row in data:
        if str(row.id) == keuze:
            data.remove(row)
            print( "ID verwijderd!")
            return data
    print("id niet in lijst")

def toon_wagen_met_brandstof(data):
    brandstof_list = []
    for row in data:
        brandstof_list.append(row.brandstof)
    brandstof_set = set(brandstof_list)
    print(brandstof_set)
    keuze = input("Op welke brandstof wil je filteren? ")
    if keuze not in brandstof_set:
        print("Brandstof niet in lijst")
        return
    else:
        filter_data = []
        for row in data:
            if row.brandstof == keuze:
                filter_data.append(row)
    toon_wagen(filter_data)

#Schrijf de huidige dataset weg naar een huidige csv
def update_data(data):
    headers = Wagen.column_headers() #Headers halen uit class
    data_list = [] #Data omvormen van objecten naar strings
    for d in data:
        new = [d.id, d.merk, d.model, d.bouwjaar, d.brandstof, d.huurprijs]
        data_list.append(new)
    with open(datafile, mode = 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data_list)
        print("\nDe bijgewerkte gegevens zijn succesvol bijgewerkt in het bestand.")

dict_functies = {"1":toon_wagen,"2":voeg_wagen_toe, "3":verwijder_wagen,"4":toon_wagen_met_brandstof, "5": update_data}