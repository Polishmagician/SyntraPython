from data import *

def toon_data():
    filter_csv_keuze = input("Welk overzicht wil je hebben? (A,B,L,U) ").upper()
    filter_csv_dict_data= {"A": data_auteur, "B": data_boeken, "L": data_lezer, "U": data_uitleningen}
    filter_csv_dict_class = {"A": auteur, "B": boek, "L": lezer, "U": uitleningen}
    headers = filter_csv_dict_class[filter_csv_keuze].headers
    print(headers)
    for item in filter_csv_dict_data[filter_csv_keuze]:
        print(item)


def voeg_data_toe():
    filter_csv_keuze = input("Aan welk overzicht wil je data toevoegen? (A,B,L,U) ").upper()
    filter_csv_dict_data= {"A": data_auteur, "B": data_boeken, "L": data_lezer, "U": data_uitleningen}
    filter_csv_dict_class = {"A": auteur, "B": boek, "L": lezer, "U": uitleningen}
    headers = filter_csv_dict_class[filter_csv_keuze].headers
    data_toevoeging = (input(f"Geef {i}") for i in headers)
    filter_csv_dict_data[filter_csv_keuze].append(filter_csv_dict_class[filter_csv_keuze](data_toevoeging))
    return filter_csv_dict_data[filter_csv_keuze]



functies_dict = {"1" : toon_data,"2": voeg_data_toe}
