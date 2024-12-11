import csv
from classes import *
def csv_to_class_boek(bestand,klas):
    data_classes = []
    with open(bestand, mode = 'r', newline='', encoding='utf-8') as  file:
        reader = csv.reader(file)
        headers = next(reader)

    with open(bestand, mode='r', newline='', encoding='utf-8') as file:
        dictreader = csv.DictReader(file)
        for index, row in enumerate(dictreader):
            m = klas(id = row[f"{headers[0]}"],
                     titel = row[f"{headers[1]}"],
                     aantal_paginas = row[f"{headers[2]}"],
                     auteur = row[f"{headers[3]}"],
            )
            data_classes.append(m)
    return data_classes,headers

def csv_to_class_auteur(bestand,klas):
    data_classes = []
    with open(bestand, mode = 'r', newline='', encoding='utf-8') as  file:
        reader = csv.reader(file)
        headers = next(reader)

    with open(bestand, mode='r', newline='', encoding='utf-8') as file:
        dictreader = csv.DictReader(file)
        for index, row in enumerate(dictreader):
            m = klas(id = row[f"{headers[0]}"],
                     voornaam = row[f"{headers[1]}"],
                     achternaam = row[f"{headers[2]}"],
                     nationaliteit = row[f"{headers[3]}"],
            )
            data_classes.append(m)
    return data_classes,headers

def csv_to_class_lezer(bestand,klas):
    data_classes = []
    with open(bestand, mode = 'r', newline='', encoding='utf-8') as  file:
        reader = csv.reader(file)
        headers = next(reader)

    with open(bestand, mode='r', newline='', encoding='utf-8') as file:
        dictreader = csv.DictReader(file)
        for index, row in enumerate(dictreader):
            m = klas(id = row[f"{headers[0]}"],
                     voornaam = row[f"{headers[1]}"],
                     achternaam = row[f"{headers[2]}"],
                     gemeente = row[f"{headers[3]}"],
                     geslacht=row[f"{headers[4]}"],
            )
            data_classes.append(m)
    return data_classes,headers

def csv_to_class_uitleningen(bestand,klas):
    data_classes = []
    with open(bestand, mode = 'r', newline='', encoding='utf-8') as  file:
        reader = csv.reader(file)
        headers = next(reader)

    with open(bestand, mode='r', newline='', encoding='utf-8') as file:
        dictreader = csv.DictReader(file)
        for index, row in enumerate(dictreader):
            m = klas(id = row[f"{headers[0]}"],
                     boek = row[f"{headers[1]}"],
                     lezer = row[f"{headers[2]}"],
            )
            data_classes.append(m)
    return data_classes,headers

data_boeken, headers_boeken = csv_to_class_boek("Boeken.csv",boek)
data_auteur, headers_auteur = csv_to_class_auteur("Auteur.csv",auteur)
data_lezer, headers_lezer = csv_to_class_lezer("Lezer.csv",lezer)
data_uitleningen, headers_uitleningen = csv_to_class_uitleningen("Uitleningen.csv",uitleningen)