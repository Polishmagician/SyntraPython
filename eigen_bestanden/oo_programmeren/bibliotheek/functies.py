from data import *
from classes_tkinter import *
import tkinter as tk
from tkinter import Tk, Text,ttk
from ctypes import windll


def toon_data():
    window = tk.Tk()
    console = TkinterConsole(window)
    custom_input = console.custom_input
    filter_csv_keuze = custom_input("Welke groep wil je hebben?").upper()
    print(filter_csv_keuze)
    # filter_csv_keuze = input("Welk overzicht wil je hebben? (A,B,L,U) ").upper()
    filter_csv_dict_data = {"A": data_auteur, "B": data_boeken, "L": data_lezer, "U": data_uitleningen}
    filter_csv_dict_class = {"A": auteur, "B": boek, "L": lezer, "U": uitleningen}
    headers = filter_csv_dict_class[filter_csv_keuze].headers
    show_data_tkinter(headers,filter_csv_dict_data[filter_csv_keuze])
    # print(headers)
    # for item in filter_csv_dict_data[filter_csv_keuze]:
    #     print(item)

def voeg_data_toe():
    filter_csv_keuze = input("Aan welk overzicht wil je data toevoegen? (A,B,L,U) ").upper()
    filter_csv_dict_data = {"A": data_auteur, "B": data_boeken, "L": data_lezer, "U": data_uitleningen}
    filter_csv_dict_class = {"A": auteur, "B": boek, "L": lezer, "U": uitleningen}
    headers = filter_csv_dict_class[filter_csv_keuze].headers
    data_toevoeging = tuple([input(f"Geef {i}") for i in headers])
    filter_csv_dict_data[filter_csv_keuze].append(filter_csv_dict_class[filter_csv_keuze](*data_toevoeging))
    return filter_csv_dict_data[filter_csv_keuze]


def pas_aan():
    filter_csv_keuze = input("In welke lijst wil je iets wijzigen? (A,B,L,U) ").upper()
    filter_csv_dict_data = {"A": data_auteur, "B": data_boeken, "L": data_lezer, "U": data_uitleningen}
    filter_csv_dict_class = {"A": auteur, "B": boek, "L": lezer, "U": uitleningen}
    headers = filter_csv_dict_class[filter_csv_keuze].headers
    print(headers)  # Geef de mogelijkheid om te kiezen uit de headers van de class
    keus = input("Wat wil je aanpassen? ") #Welk attribute wil je aanpassen
    veranderende_id = input(f"Geef het id waarvan je {keus} wilt veranderen: ")
    for item in filter_csv_dict_data[filter_csv_keuze]:
        if item.id == veranderende_id:
            print(item) #te wijzigen lijn weergeven
            inp = input("Waarin wil je het veranderen? ")
            setattr(filter_csv_dict_data[filter_csv_keuze][int(veranderende_id) - 1], keus, inp) #attribute van veranderende_id wijzigen naar inp
    return filter_csv_dict_data[filter_csv_keuze]

def show_data_tkinter(headers,data):
    import tkinter as tk
    from tkinter import Tk, Text
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
    root = tk.Tk()  # Call root class
    root.title('Demo mode')

    root.geometry('600x400+50+50')  # widthxheight±x±y

    # Text boxes
    text = Text(root, height=8)
    text.pack()
    for h in headers:
        text.insert('end',h+',')
    text.insert(2.0,'\n')
    for index,item in enumerate(data):
        text.insert(3.0+index,str(item)+'\n')
    text['state'] = 'disabled'
    root.mainloop()


functies_dict = {"1": toon_data, "2": voeg_data_toe, "3": pas_aan}
