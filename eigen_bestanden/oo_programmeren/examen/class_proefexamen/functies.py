from data import *
from tabulate import tabulate


data = classes_data

def toon_data(data):
    filter_data = data[:]
    filter_list = []
    for d in filter_data:
        if isinstance(d, Bediende):
            new = ["Bediende"]
            new.append(d.id)
            new.append(d.voornaam)
            new.append(d.achternaam)
            new.append(d.leeftijd)
            new.append(d.geslacht)
            new.append(d.functie)
            new.append(d.maandloon)
            filter_list.append(new)
        else:
            new = ["Freelance"]
            new.append(d.id)
            new.append(d.voornaam)
            new.append(d.achternaam)
            new.append(d.leeftijd)
            new.append(d.geslacht)
            new.append(d.functie)
            new.append(d.uurloon)
            filter_list.append(new)
    print(tabulate(filter_list, headers=Personeel.column_headers()))
def toon_data_keuze(data):
    keuze = input("Wat wil je zien? Alles, Bedienden of Freelance? (A,B,F)").upper()
    if keuze == "A":
        toon_data(data)
        return
    elif keuze == "B":
        filter_data = [x for x in data if isinstance(x,Bediende)]
        filter_list = []
        for d in filter_data:
            new = ["Bediende"]
            new.append(d.id)
            new.append(d.voornaam)
            new.append(d.achternaam)
            new.append(d.leeftijd)
            new.append(d.geslacht)
            new.append(d.functie)
            new.append(d.maandloon)
            filter_list.append(new)
    else:
        filter_data = [x for x in data if isinstance(x, Freelance)]
        filter_list = []
        for d in filter_data:
            new = ["Freelance"]
            new.append(d.id)
            new.append(d.voornaam)
            new.append(d.achternaam)
            new.append(d.leeftijd)
            new.append(d.geslacht)
            new.append(d.functie)
            new.append(d.uurloon)
            filter_list.append(new)
    print(tabulate(filter_list,headers=Personeel.column_headers()))



def voeg_data_toe(data):
    soort = input("Is het een bediende of een Freelancer? (B/F)").upper()
    ids = []
    for row in data:
        ids.append(int(row.id))
    if soort == "B":
        new_data = tuple([input(f"Geef {i}")for i in Personeel.column_headers()[2:]])
        data.append(Bediende(max(ids)+1,*new_data))
        print("Personeelslid toegevoegd")
    elif soort == "F":
        new_data = tuple([input( f"Geef {i}")for i in Personeel.column_headers()[2:]])
        data.append(Freelance(max(ids)+1,*new_data))
        print("Personeelslid toegevoegd")
    else:
        print("Wrong input")
    return data


def verwijder_id(data):
    toon_data(data)
    keuze = input("Welke ID wil je verwijderen?")
    for row in data:
        if row.id == keuze:
            data.remove(row)
            print( "ID verwijderd!")
            return data
    print("id niet in lijst")

def toon_maandloon_hoger_dan(data):
    keuze = input( "Hoger dan x?")
    filter_data = [x for x in data if isinstance(x, Bediende)]
    filter_list = []
    for d in filter_data:
        if int(d.maandloon) > keuze:
            new = ["Bediende"]
            new.append(d.id)
            new.append(d.voornaam)
            new.append(d.achternaam)
            new.append(d.leeftijd)
            new.append(d.geslacht)
            new.append(d.functie)
            new.append(d.maandloon)
            filter_list.append(new)
    if not filter_list:
        print( "Lijst is leeg")
        return
    print(tabulate(filter_list, headers=Personeel.column_headers()))

def toon_iedereen_met_functie(data):
    functies_list = []
    for row in data:
        functies_list.append(row.functie)
    functies_set = set(functies_list)
    print(functies_set)
    keuze = input("Op welke functie wil je filteren?")
    if keuze not in functies_set:
        messagebox.showinfo("Verkoop Gesorteerd", "Functie niet in lijst")
        return
    else:
        filter_data = []
        for row in data:
            if row.functie == keuze:
                filter_data.append(row)
    toon_data(filter_data)

dict_functies = {"1":toon_data_keuze,"2":voeg_data_toe,"3":verwijder_id,"4":toon_maandloon_hoger_dan,"5":toon_iedereen_met_functie}