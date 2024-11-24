from data_medewerkers import *
from data_wagens import *
from tabulate import tabulate
import csv


def toon_personeel():
    headers = ["ID", "Naam", "Leeftijd", "Geslacht", "Functie"]
    data = []
    for p in personeel_data_class:
        new_data = [p.id, p.naam, p.leeftijd, p.geslacht, p.functie]
        data.append(new_data)
    print(tabulate(data, headers=headers))


def toon_bediendes():
    headers = ["ID", "Naam", "Leeftijd", "Geslacht", "Functie", "Maandloon", "Afdeling", "Bedrijfswagen"]
    data = []
    for p in bedienden_data_class:
        new_data = [p.id, p.naam, p.leeftijd, p.geslacht, p.functie, p.maandloon, p.afdeling, p.bedrijfswagen]
        data.append(new_data)
    print(tabulate(data, headers=headers))


def toon_arbeiders():
    headers = ["ID", "Naam", "Leeftijd", "Geslacht", "Functie", "Uurloon", "Uren gewerkt"]
    data = []
    for p in arbeiders_data_class:
        new_data = [p.id, p.naam, p.leeftijd, p.geslacht, p.functie, p.uurloon, p.aantal_uur]
        data.append(new_data)
    print(tabulate(data, headers=headers))

def toon_wagens():
    headers = ["ID", "Merk", "Model", "Bouwjaar", "Eigenaar"]
    data = []
    for p in wagens:
        new_data = [p.id, p.merk, p.model, p.bouwjaar, p.eigenaar]
        data.append(new_data)
    print(tabulate(data, headers=headers))

def voeg_personeel_toe():
    new_personeel = {'id': personeel.id_personeel+1,
                     'naam': input("Wat is de naam?"),
                     'leeftijd': int(input("Wat is de leeftijd?")),
                     'geslacht': input("Geef het geslacht").upper(),
                     'functie': input("Arbeider of bediende? ").lower()}
    if new_personeel['geslacht'] == 'MAN':
        new_personeel['geslacht'] = 'M'
    elif new_personeel['geslacht'] == 'VROUW':
        new_personeel['geslacht'] = 'V'
    else:
        new_personeel['geslacht'] = 'X'
    personeel_data_class.append(personeel(new_personeel['id'],
                                          new_personeel['naam'],
                                          new_personeel['leeftijd'],
                                          new_personeel['geslacht'],
                                          new_personeel['functie']))
    if new_personeel['functie'] == 'bediende':
        new_personeel["maandloon"] = input("Wat is het maandloon?")
        new_personeel['afdeling'] = input("Wat is de afdeling? ")
        bw = input("Bedrijfswagen? (Ja/Nee) ").lower()
        if bw == "nee":
            new_personeel['bedrijfswagen'] = None
        else:
            new_personeel['bedrijfswagen'] = int(input("Wat is het id nummer van de bedrijfswagen? "))
        bedienden_data_class.append(bediende(new_personeel['id'],
                                             new_personeel['naam'],
                                             new_personeel['leeftijd'],
                                             new_personeel['geslacht'],
                                             new_personeel['functie'],
                                             new_personeel['maandloon'],
                                             new_personeel['afdeling'],
                                             new_personeel['bedrijfswagen']))
        return bedienden_data_class
    else:
        new_personeel["uurloon"] = input("Wat is het uurloon ?")
        new_personeel['uren_gewerkt'] = input("Hoeveel uren gewerkt ? ")
        arbeiders_data_class.append(arbeider(new_personeel['id'],
                                             new_personeel['naam'],
                                             new_personeel['leeftijd'],
                                             new_personeel['geslacht'],
                                             new_personeel['functie'],
                                             new_personeel['uurloon'],
                                             new_personeel['uren_gewerkt']))
        return arbeiders_data_class

def voeg_wagen_toe():
    new_auto = {"id": bedrijfswagen.id_wagen+1, "merk": input("Welk merk: "), "model": input("Welk model: "), "bouwjaar": int(input("Welk bouwjaar: "))}
    eigenaar = input("Is er een eigenaar? (Ja/Nee) ").lower()
    if eigenaar == "ja":
        eigenaar = int(input("Geef ID: "))
        new_auto["eigenaar"] = eigenaar
        for item in bedienden_data_class:
            if item.id == eigenaar:
                item.bedrijfswagen = new_auto['id']
    else:
        new_auto["eigenaar"] = None
    wagens.append(bedrijfswagen(new_auto['id'],
                                new_auto['merk'],
                                new_auto['model'],
                                new_auto['bouwjaar'],
                                new_auto['eigenaar']))
    return wagens

def ken_wagen_toe_aan_bediende():
    toon_bediendes()
    bed = int(input("Welke bediende wil je een auto aan toevoegen? (ID) "))
    auto_id = int(input("Geef me het ID van de auto om toe te voegen: "))
    for item in bedienden_data_class:
        if item.id == bed:
            item.bedrijfswagen = auto_id
            break
    for item in wagens:
        if item.id == auto_id:
            item.eigenaar = bed
            break
    return bedienden_data_class, wagens

def verwijder_personeelslid():
    toon_personeel()
    per = int(input("Geef me het ID dat je wilt verwijderen? "))
    for index, item in enumerate(personeel_data_class):
        if item.id == per:
            del personeel_data_class[index]
    return personeel_data_class

def verander_loon():
    toon_personeel()
    keuze = input("Gaat het om een bediende of arbeider? ").lower()
    if keuze == 'bediende':
        toon_bediendes()
        id = int(input("Geef het ID: "))
        loon = int(input("Geef het nieuwe maandloon: "))
        for item in bedienden_data_class:
            if item.id == id:
                item.maandloon = loon
                break
        return bedienden_data_class
    else:
        toon_arbeiders()
        id = int(input("Geef het ID: "))
        loon = int(input("Geef het nieuwe maandloon: "))
        for item in arbeiders_data_class:
            if item.id == id:
                item.uurloon = loon
                break
        return arbeiders_data_class

def toon_bedienden_maandloon_meer_dan():
    toon_bediendes()
    gefilterde_bedienden = []
    maandloon = int(input("Geef het maandloon om op te filteren? "))
    for item in bedienden_data_class:
        if item.maandloon > maandloon:
            gefilterde_bedienden.append(item)
    headers = ["ID", "Naam", "Leeftijd", "Geslacht", "Functie", "Maandloon", "Afdeling", "Bedrijfswagen"]
    data = []
    for p in gefilterde_bedienden:
        new_data = [p.id, p.naam, p.leeftijd, p.geslacht, p.functie, p.maandloon, p.afdeling, p.bedrijfswagen]
        data.append(new_data)
    print(tabulate(data, headers=headers))
    return gefilterde_bedienden

def toon_bedienden_bedrijfswagen():
    gefilterde_bedienden = []
    for item in bedienden_data_class:
        if item.bedrijfswagen is not None:
            gefilterde_bedienden.append(item)
    headers = ["ID", "Naam", "Leeftijd", "Geslacht", "Functie", "Maandloon", "Afdeling", "Bedrijfswagen"]
    data = []
    for p in gefilterde_bedienden:
        new_data = [p.id, p.naam, p.leeftijd, p.geslacht, p.functie, p.maandloon, p.afdeling, p.bedrijfswagen]
        data.append(new_data)
    print(tabulate(data, headers=headers))
    return gefilterde_bedienden

def wegschrijven(data):
    with open("data.csv", mode = 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        count = 0
        while count == 0:
            for item in data:
                writer.writerow(item.toHeader())
                count = 1
                break
        for item in data:
            writer.writerow(item.toIterable())
        print("\nDe bijgewerkte gegevens zijn succesvol opgeslagen in het bestand.")


#Alle functies in een dict
functies = [toon_personeel,toon_bediendes,toon_arbeiders,toon_wagens,voeg_personeel_toe,voeg_wagen_toe,ken_wagen_toe_aan_bediende,verwijder_personeelslid,verander_loon,toon_bedienden_maandloon_meer_dan,toon_bedienden_bedrijfswagen]
functie_dict = {}
for index, functie in enumerate(functies):
    functie_dict[index+1] = functie

