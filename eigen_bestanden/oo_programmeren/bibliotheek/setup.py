from faker import Faker
import random
import pandas as pd
fake = Faker()
# Generate realistic Boeken data
boeken_titles = [
    "The Silent Forest", "Journey to the Stars", "The Hidden Truth", "Ocean Whispers",
    "Beyond the Horizon", "Shadows of the Past", "City of Dreams", "The Timekeeper's Tale",
    "Whispers of the Night", "Legacy of Fire", "Chronicles of Hope", "A Song for Tomorrow",
    "Echoes of Eternity", "The Lost Kingdom", "Mystery of the Lake", "Guardians of the Light",
    "Threads of Fate", "The Winter Rose", "The Eternal Quest", "Secrets of the Sands"
]
boeken_data = []
for i, title in enumerate(boeken_titles, start=1):
    boeken_data.append({
        "id": i,
        "titel": title,
        "aantal_paginas": random.randint(200, 600),
        "auteur": random.randint(1, 10)  # Match authors
    })
boeken_df = pd.DataFrame(boeken_data)

# Generate more consistent Auteur data
auteur_data = []
nationalities = ["Dutch", "Belgian", "German", "French", "British", "American", "Italian", "Spanish", "Canadian", "Australian"]
for i in range(1, 11):  # 10 authors
    auteur_data.append({
        "id": i,
        "voornaam": fake.first_name(),
        "achternaam": fake.last_name(),
        "nationaliteit": random.choice(nationalities)
    })
auteur_df = pd.DataFrame(auteur_data)

# Generate realistic Lezer data
lezer_data = []
for i in range(1, 31):  # 30 readers
    lezer_data.append({
        "id": i,
        "voornaam": fake.first_name(),
        "achternaam": fake.last_name(),
        "gemeente": fake.city(),
        "geslacht": random.choices(["M", "F", "X"], weights=[45, 45, 10])[0]  # More M and F, fewer X
    })
lezer_df = pd.DataFrame(lezer_data)

# Generate realistic Uitleningen data
uitleningen_data = []
for i in range(1, 41):  # 40 loans
    uitleningen_data.append({
        "id": i,
        "boek": random.randint(1, 20),  # Reference to Boeken
        "lezer": random.randint(1, 30)  # Reference to Lezer
    })
uitleningen_df = pd.DataFrame(uitleningen_data)

boeken_file = "Boeken.csv"
auteur_file = "Auteur.csv"
lezer_file = "Lezer.csv"
uitleningen_file = "Uitleningen.csv"

# Save refined data to CSV
boeken_df.to_csv(boeken_file, index=False)
auteur_df.to_csv(auteur_file, index=False)
lezer_df.to_csv(lezer_file, index=False)
uitleningen_df.to_csv(uitleningen_file, index=False)

