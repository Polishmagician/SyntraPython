from classes import *
import csv

datafile = 'autoverhuur_data.csv' #Basis CSV

def lees_csv_bestand(data_file):
    """Leest het CSV-bestand in en retourneert de inhoud als een lijst van rijen."""
    try:
        with open(data_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
        return data
    except FileNotFoundError:
        print("Fout: Het opgegeven bestand bestaat niet.")
        return []
    except Exception as e:
        print(f"Fout bij het lezen van het bestand: {e}")
        return []

data = lees_csv_bestand(datafile)
classes_data = []
#lijst_wagens_model
for row in data[1:]:
    classes_data.append(Wagen(*row))