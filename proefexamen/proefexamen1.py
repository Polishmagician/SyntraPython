import csv
from tabulate import tabulate

bestand = 'dokters.csv'

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

    #Voeg de bestaande gegevens, als die er zijn
    for row in reader:
        data.append(row)


def nieuwe_dokter():
    nieuw_personeelslid = []
    print("Voer de gegevens in voor een nieuw personeelslid:")
    for header in headers:
        waarde = input(f"Voer {header} in: ")
        nieuw_personeelslid.append(waarde)
    data.append(nieuw_personeelslid)
    return data


def verwijder_dokter():
    voornaam = input(f"Voer de voornaam in die je wilt verwijderen: ")
    achternaam = input(f"Voer de achternaam in die je wilt verwijderen: ")
    for index, row in enumerate(data):
        if voornaam in row and achternaam in row:
            data.pop(index)
            return data
    print(f"Combinatie {voornaam} {achternaam} niet in lijst")

def toon_dokters():
    return data


def toon_dokters_ziekenhuis():
    gefilterde_data = []
    keuze = input(f"Geef het ziekenhuis waarop je wilt filteren: ")
    for row in data:
        if keuze in row:
            gefilterde_data.append(row)
    return gefilterde_data

def pas_ziekenhuis_aan():
    dokter_voornaam = input("Geef de voornaam van de dokter voor wie je het ziekenhuis wilt aanpassen: ")
    dokter_achternaam = input("Geef de achternaam van de dokter voor wie je het ziekenhuis wilt aanpassen: ")
    for row in data:
        if dokter_voornaam in row and dokter_achternaam in row:
            ziekenhuis = input(f"Waar werkt {dokter_voornaam} {dokter_achternaam} ? ")
            row[3] = ziekenhuis
            return data
    print(f"{dokter_voornaam} {dokter_achternaam} niet in lijst")


def pas_woonplaats_aan():
    dokter_voornaam = input("Geef de voornaam van de dokter voor wie je de woonplaats wilt aanpassen: ")
    dokter_achternaam = input("Geef de achternaam van de dokter voor wie je de woonplaats wilt aanpassen: ")
    for row in data:
        if dokter_voornaam in row and dokter_achternaam in row:
            woonplaats = input(f"Waar woont {dokter_voornaam} {dokter_achternaam} ? ")
            row[2] = woonplaats
            return data
    print(f"{dokter_voornaam} {dokter_achternaam} niet in lijst")


def pas_loon_aan():
    voornaam_dokter = input("Geef de voornaam van de dokter voor wie je het loon wilt aanpassen: ")
    achternaam_dokter = input("Geef de achternaam van de dokter voor wie je het loon wilt aanpassen: ")
    for row in data:
        if voornaam_dokter in row and achternaam_dokter in row:
            loon = input(f"Welk loon heeft {voornaam_dokter} {achternaam_dokter} ? ")
            row[4] = loon
            return data
    print(f"{voornaam_dokter} {achternaam_dokter} niet in lijst")


def sort_naam():
    sorted_data = sorted(data, key = lambda x : x[1])
    return sorted_data


def sort_ereloon():
    sorted_data = sorted(data, key = lambda x : x[4], reverse=True)
    return sorted_data


def wegschrijven():
    with open(bestand, mode = 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)
        print("\nDe bijgewerkte gegevens zijn succesvol opgeslagen in het bestand.")


def controller():
    keuze = 0
    while keuze != "11":
        print("1: Voeg een dokter toe",
              "2: Verwijder een dokter",
              "3: Toon alle dokters",
              "4: Toon alle dokters van ziekenhuis x",
              "5: Pas ziekenhuis aan",
              "6: Wijzig woonplaats",
              "7: Wijzig ereloon",
              "8: Sorteer alle dokters op naam (A-Z)",
              "9: Sorteer alle dokters op ereloon (hoog-laag)",
              "10: STOP",
              "11: STOP & SAVE")
        keuze = input("Wat wil je doen? ")
        if keuze == "1":
            data=nieuwe_dokter()
        elif keuze == "2":
            data = verwijder_dokter()
        elif keuze == "3":
            data = toon_dokters()
        elif keuze == "4":
            data = toon_dokters_ziekenhuis()
        elif keuze == "5":
            data = pas_ziekenhuis_aan()
        elif keuze == "6":
            data = pas_woonplaats_aan()
        elif keuze == "7":
            data =pas_loon_aan()
        elif keuze == "8":
            data = sort_naam()
        elif keuze == "9":
            data = sort_ereloon()
        elif keuze == "10":
            print(tabulate(data, headers=headers, tablefmt="grid"))
            break
        elif keuze == "11":
            wegschrijven()
        print("Bijgewerkte personeelslijst:")
        print(tabulate(data, headers=headers, tablefmt="grid"))
controller()