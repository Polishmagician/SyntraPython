import csv

#Read CSV
bestand = 'film.csv'

# Open het CSV-bestand en lees het in
with open(bestand, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    # Elke rij (record) afdrukken
    for row in reader:
        for item in row:
            print(item,end="\t")
        print("")

#Read to tabulate
from tabulate import tabulate

data = []
# Open het CSV-bestand en lees het in
with open(bestand, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    # Lees de header (kolomnamen) in
    headers = next(reader)

# Voeg de rijen toe aan de data lijst
    for row in reader:
        data.append(row)

# Toon de gegevens in een nette tabel met tabulate
print(tabulate(data, headers=headers, tablefmt='grid'))