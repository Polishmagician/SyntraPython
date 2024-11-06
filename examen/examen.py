import csv
from tabulate import tabulate

bestand = 'muzikanten_data.csv'

#Lege lijst voor data en headers
data = []
headers = []

#Open CSV bestand en lees in:
with open(bestand, mode = 'r', newline='', encoding='utf-8') as  file:
    reader = csv.reader(file)

    try:
        #Lees de header in:
        headers = next(reader)
    except StopIteration:
        print("Het CSV-bestand is leeg. Voeg een nieuwe dokter toe om te beginnen")

    #Voeg de bestaande gegevens
    for row in reader:
        data.append(row)

#Voeg een muzikant toe
def nieuwe_muzikant():
    nieuwe_id = str(int(data[-1][0])+1)
    nieuw_muzikant = [nieuwe_id]
    print("Voer onder deze lijn de gegevens in voor een nieuwe muzikant:")
    for header in headers[1:]:
        waarde = input(f"Voer {header} in: ")
        nieuw_muzikant.append(waarde)
    data.append(nieuw_muzikant)
    print(tabulate(data, headers= headers))

#Verwijder een muzikant
def verwijder_muzikant():
    id = input("Voer het id in dat je wilt verwijderen: ")
    for index, row in enumerate(data):
        if id in row:
            data.pop(index)
            print(tabulate(data, headers=headers))

#Toon alle muzikanten in tabulate
def toon_muzikanten():
    print(tabulate(data, headers=headers))


#Toon alle muzikanten van genre(x) in tabulate
def toon_muzikanten_genre():
    gefilterde_data = []
    keuze = input(f"Geef het genre waarop je wilt filteren: ")
    for row in data:
        if keuze in row:
            gefilterde_data.append(row)
    print(tabulate(gefilterde_data, headers = headers))

#Pas het instrument aan van de muzikant
def pas_instrument_aan():
    id = input("Geef het id waarvan je het instrument wilt aanpassen: ")
    for row in data:
        if id in row:
            instrument = input(f"Wat is het instrument van dokter met id {id}? ")
            row[2] = instrument
            print(tabulate(data, headers= headers))


#Sorteer alle muzikanten op naam a-z
def sort_naam():
    sorted_data = sorted(data, key = lambda x : x[1])
    print(tabulate(sorted_data, headers=headers))

#Schrijf huidige data weg naar een nieuw csv bestand
def wegschrijven():
    with open("muzikanten_data_update.csv", mode = 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)
        print("\nDe bijgewerkte gegevens zijn succesvol opgeslagen in het bestand.")

# nieuwe_muzikant()
# verwijder_muzikant()
# toon_muzikanten()
# toon_muzikanten_genre()
# pas_instrument_aan()
# sort_naam()
# wegschrijven()

