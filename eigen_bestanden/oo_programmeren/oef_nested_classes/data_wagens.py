from Classes import *

data_inputs_wagens = [
    {"id": 1, "merk": "Volkswagen", "model": "Golf", "bouwjaar": 2020, "eigenaar": 1},
    {"id": 2, "merk": "Audi", "model": "A4", "bouwjaar": 2019, "eigenaar": 3},
    {"id": 3, "merk": "BMW", "model": "1 Series", "bouwjaar": 2021, "eigenaar": 5},
    {"id": 4, "merk": "Tesla", "model": "Model 3", "bouwjaar": 2022, "eigenaar": 8},
    {"id": 5, "merk": "Mercedes", "model": "A-Class", "bouwjaar": 2018, "eigenaar": 10},
    {"id": 6, "merk": "Volkswagen", "model": "ID.3", "bouwjaar": 2023, "eigenaar": 13},
    {"id": 7, "merk": "Volvo", "model": "XC40", "bouwjaar": 2020, "eigenaar": 17},
    {"id": 8, "merk": "Ford", "model": "Focus", "bouwjaar": 2017, "eigenaar": 19},
    {"id": 9, "merk": "Renault", "model": "Clio", "bouwjaar": 2021, "eigenaar": None},
    {"id": 10, "merk": "Peugeot", "model": "208", "bouwjaar": 2019, "eigenaar": None},
    {"id": 11, "merk": "BMW", "model": "X1", "bouwjaar": 2022, "eigenaar": None},
    {"id": 12, "merk": "Toyota", "model": "Corolla", "bouwjaar": 2020, "eigenaar": None},
    {"id": 13, "merk": "Honda", "model": "Civic", "bouwjaar": 2018, "eigenaar": None},
    {"id": 14, "merk": "Opel", "model": "Corsa", "bouwjaar": 2021, "eigenaar": None},
    {"id": 15, "merk": "Hyundai", "model": "i30", "bouwjaar": 2019, "eigenaar": None},
    {"id": 16, "merk": "Kia", "model": "Ceed", "bouwjaar": 2023, "eigenaar": None},
    {"id": 17, "merk": "Mazda", "model": "3", "bouwjaar": 2020, "eigenaar": None},
    {"id": 18, "merk": "Skoda", "model": "Octavia", "bouwjaar": 2022, "eigenaar": None},
    {"id": 19, "merk": "Nissan", "model": "Qashqai", "bouwjaar": 2021, "eigenaar": None},
    {"id": 20, "merk": "Seat", "model": "Leon", "bouwjaar": 2019, "eigenaar": None},
]


wagens = []
for auto in data_inputs_wagens:
    new_wagen = bedrijfswagen(auto['id'],auto["merk"],auto["model"],auto["bouwjaar"],auto["eigenaar"])
    wagens.append(new_wagen)
