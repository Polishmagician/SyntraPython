import csv

from tabulate import tabulate

bestand = 'leerkrachten.csv'

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
        print("Het CSV-bestand is leeg. Voeg een nieuw personeelslid toe om te beginnen")

    #Voeg de bestaande gegevens, als die er zijn
    for row in reader:
        data.append(row)

#Toon de bestaande gegevens, als die er zijn
if data:
    print("Huidige lerarenlijst:")
    print(tabulate(data, headers=headers, tablefmt='grid'))

def nieuw_leerkracht():
    nieuw_personeelslid = []
    print("Voer de gegevens in voor een nieuw personeelslid:")
    for header in headers:
        waarde = input(f"Voer {header} in: ")
        nieuw_personeelslid.append(waarde)
    data.append(nieuw_personeelslid)
    return data


def verwijder_leerkracht():
    keuze = input(f"Voer de naam in die je wilt verwijderen: ")
    for index, row in enumerate(data):
        if keuze in row:
            data.pop(index)
            return data
    print(f"{keuze} niet in lijst")


def pas_vak_aan():
    leerkracht = input("Geef de naam van de leerkracht voor wie je het vak wilt aanpassen: ")
    for row in data:
        if leerkracht in row:
            vak = input(f"Welk vak geeft {leerkracht} ? ")
            row[4] = vak
            return data
    print(f"{leerkracht} niet in lijst")

def pas_woonplaats_aan():
    leerkracht = input("Geef de naam van de leerkracht voor wie je de woonplaats wilt aanpassen: ")
    for row in data:
        if leerkracht in row:
            woonplaats = input(f"Waar woont {leerkracht} ? ")
            row[2] = woonplaats
            return data
    print(f"{leerkracht} niet in lijst")


def sort_woonplaats():
    sorted_data = sorted(data, key = lambda x : x[2])
    print(tabulate(sorted_data, headers=headers, tablefmt="grid"))
    return sorted_data

def wegschrijven():
    with open(bestand, mode = 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)
        print("\nDe bijgewerkte gegevens zijn succesvol opgeslagen in het bestand.")
def controller():
    bestand = 'leerkrachten.csv'

    # Lege lijst voor data en headers
    data = []
    headers = []

    # Open CSV bestand en lees in:
    with open(bestand, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        try:
            # Lees de header in:
            headers = next(reader)
        except StopIteration:
            print("Het CSV-bestand is leeg. Voeg een nieuw personeelslid toe om te beginnen")

        # Voeg de bestaande gegevens, als die er zijn
        for row in reader:
            data.append(row)

    # Toon de bestaande gegevens, als die er zijn
    if data:
        print("Huidige lerarenlijst:")
        print(tabulate(data, headers=headers, tablefmt='grid'))
    keuze = 0
    while keuze != "8":
        print("1: Toon lijst",
              "2: Voeg leerkracht toe",
              "3: Verwijder leerkracht",
              "4: Pas vak aan",
              "5: Pas woonplaats aan",
              "6: Sorteer op woonplaats (A-Z)",
              "7: STOP en SAVE"
              "8: STOP")
        keuze = input("Wat wil je doen? ")
        if keuze == "1":
            pass
        elif keuze == "2":
            data = nieuw_leerkracht()
        elif keuze == "3":
            data = verwijder_leerkracht()
        elif keuze == "4":
            data = pas_vak_aan()
        elif keuze == "5":
            data = pas_woonplaats_aan()
        elif keuze == "6":
            data = sort_woonplaats()
        elif keuze == "7":
            wegschrijven()
            keuze = "8"
        print("Bijgewerkte personeelslijst:")
        print(tabulate(data, headers=headers, tablefmt="grid"))
controller()