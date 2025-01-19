from proefexamen_class import *
import csv

datafile = 'personeel_data.csv'
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

for row in data[1:]:
    if row[0] == "Freelance":
        classes_data.append(Freelance(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
    else:
        classes_data.append(Bediende(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
