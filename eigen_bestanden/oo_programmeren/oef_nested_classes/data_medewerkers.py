from Classes import *
# Data lijst

personeel_data_input = [
    {"id": 1, "naam": "Anna Vermeulen", "leeftijd": 29, "geslacht": "V", "functie": "bediende"},
    {"id": 2, "naam": "Bart Jansen", "leeftijd": 34, "geslacht": "M", "functie": "bediende"},
    {"id": 3, "naam": "Chris De Smet", "leeftijd": 26, "geslacht": "X", "functie": "bediende"},
    {"id": 4, "naam": "Diana Claes", "leeftijd": 31, "geslacht": "V", "functie": "bediende"},
    {"id": 5, "naam": "Erik Peeters", "leeftijd": 25, "geslacht": "M", "functie": "bediende"},
    {"id": 6, "naam": "Fiona De Jong", "leeftijd": 38, "geslacht": "V", "functie": "bediende"},
    {"id": 7, "naam": "Gertjan Van Loon", "leeftijd": 33, "geslacht": "M", "functie": "bediende"},
    {"id": 8, "naam": "Hanne De Bruin", "leeftijd": 28, "geslacht": "V", "functie": "bediende"},
    {"id": 9, "naam": "Ivan Meeuwis", "leeftijd": 30, "geslacht": "M", "functie": "bediende"},
    {"id": 10, "naam": "Julie Maes", "leeftijd": 35, "geslacht": "V", "functie": "bediende"},
    {"id": 11, "naam": "Koenraad Luyten", "leeftijd": 29, "geslacht": "M", "functie": "bediende"},
    {"id": 12, "naam": "Liesbeth Opdenbosch", "leeftijd": 37, "geslacht": "V", "functie": "bediende"},
    {"id": 13, "naam": "Mark De Vries", "leeftijd": 24, "geslacht": "M", "functie": "bediende"},
    {"id": 14, "naam": "Nina van Dijk", "leeftijd": 27, "geslacht": "V", "functie": "bediende"},
    {"id": 15, "naam": "Oscar Janssens", "leeftijd": 32, "geslacht": "M", "functie": "bediende"},
    {"id": 16, "naam": "Pauline De Winter", "leeftijd": 36, "geslacht": "V", "functie": "bediende"},
    {"id": 17, "naam": "Quinten Bosmans", "leeftijd": 23, "geslacht": "M", "functie": "bediende"},
    {"id": 18, "naam": "Rita Claes", "leeftijd": 31, "geslacht": "V", "functie": "bediende"},
    {"id": 19, "naam": "Stefan Timmermans", "leeftijd": 34, "geslacht": "M", "functie": "bediende"},
    {"id": 20, "naam": "Tessa Verhoeven", "leeftijd": 26, "geslacht": "V", "functie": "bediende"},
    {"id": 21, "naam": "Jan Peeters", "leeftijd": 40, "geslacht": "M", "functie": "arbeider"},
    {"id": 22, "naam": "Lisa Jansen", "leeftijd": 28, "geslacht": "V", "functie": "arbeider"},
    {"id": 23, "naam": "Tom Willems", "leeftijd": 35, "geslacht": "M", "functie": "arbeider"},
    {"id": 24, "naam": "Evi Vermeulen", "leeftijd": 30, "geslacht": "V", "functie": "arbeider"},
    {"id": 25, "naam": "Sam De Groot", "leeftijd": 24, "geslacht": "X", "functie": "arbeider"},
    {"id": 26, "naam": "Karin De Smet", "leeftijd": 32, "geslacht": "V", "functie": "arbeider"},
    {"id": 27, "naam": "Peter Janssens", "leeftijd": 45, "geslacht": "M", "functie": "arbeider"},
    {"id": 28, "naam": "Nina Van Loon", "leeftijd": 27, "geslacht": "V", "functie": "arbeider"},
    {"id": 29, "naam": "Wim Claes", "leeftijd": 33, "geslacht": "M", "functie": "arbeider"},
    {"id": 30, "naam": "Sofie Luyten", "leeftijd": 29, "geslacht": "V", "functie": "arbeider"},
    {"id": 31, "naam": "Erik Opdenbosch", "leeftijd": 50, "geslacht": "M", "functie": "arbeider"},
    {"id": 32, "naam": "Anke Bosmans", "leeftijd": 31, "geslacht": "V", "functie": "arbeider"},
    {"id": 33, "naam": "Tobias De Winter", "leeftijd": 36, "geslacht": "M", "functie": "arbeider"},
    {"id": 34, "naam": "Emma Meeuwis", "leeftijd": 26, "geslacht": "V", "functie": "arbeider"},
    {"id": 35, "naam": "Bart De Jong", "leeftijd": 34, "geslacht": "M", "functie": "arbeider"},
    {"id": 36, "naam": "Laura Timmermans", "leeftijd": 30, "geslacht": "V", "functie": "arbeider"},
    {"id": 37, "naam": "Geert Van Dijk", "leeftijd": 42, "geslacht": "M", "functie": "arbeider"},
    {"id": 38, "naam": "Liesbeth Verhoeven", "leeftijd": 25, "geslacht": "V", "functie": "arbeider"},
    {"id": 39, "naam": "Oscar Jansen", "leeftijd": 39, "geslacht": "M", "functie": "arbeider"},
    {"id": 40, "naam": "Tessa Claes", "leeftijd": 29, "geslacht": "V", "functie": "arbeider"}
]



bedienden_data_input =[
    {"id": 1, 'naam': 'Anna Vermeulen', 'leeftijd': 29, 'geslacht': 'V', 'functie': 'bediende', 'maandloon': 3874, 'afdeling': 'IT', 'bedrijfswagen': 1},
    {"id": 2, 'naam': 'Bart Jansen', 'leeftijd': 34, 'geslacht': 'M', 'functie': 'bediende', 'maandloon': 3101, 'afdeling': 'Marketing', 'bedrijfswagen': None},
    {"id": 3, 'naam': 'Chris De Smet', 'leeftijd': 26, 'geslacht': 'X', 'functie': 'bediende', 'maandloon': 2468, 'afdeling': 'HR', 'bedrijfswagen': 2},
    {"id": 4, 'naam': 'Diana Claes', 'leeftijd': 31, 'geslacht': 'V', 'functie': 'bediende', 'maandloon': 2186, 'afdeling': 'IT', 'bedrijfswagen': None},
    {"id": 5, 'naam': 'Erik Peeters', 'leeftijd': 25, 'geslacht': 'M', 'functie': 'bediende', 'maandloon': 3942, 'afdeling': 'Marketing', 'bedrijfswagen': 3},
    {"id": 6, 'naam': 'Fiona De Jong', 'leeftijd': 38, 'geslacht': 'V', 'functie': 'bediende', 'maandloon': 2400, 'afdeling': 'HR', 'bedrijfswagen': None},
    {"id": 7, 'naam': 'Gertjan Van Loon', 'leeftijd': 33, 'geslacht': 'M', 'functie': 'bediende', 'maandloon': 2810, 'afdeling': 'IT', 'bedrijfswagen': None},
    {"id": 8, 'naam': 'Hanne De Bruin', 'leeftijd': 28, 'geslacht': 'V', 'functie': 'bediende', 'maandloon': 2817, 'afdeling': 'HR', 'bedrijfswagen': 4},
    {"id": 9, 'naam': 'Ivan Meeuwis', 'leeftijd': 30, 'geslacht': 'M', 'functie': 'bediende', 'maandloon': 2490, 'afdeling': 'IT', 'bedrijfswagen': None},
    {"id": 10, 'naam': 'Julie Maes', 'leeftijd': 35, 'geslacht': 'V', 'functie': 'bediende', 'maandloon': 3276, 'afdeling': 'IT', 'bedrijfswagen': 5},
    {"id": 11, 'naam': 'Koenraad Luyten', 'leeftijd': 29, 'geslacht': 'M', 'functie': 'bediende', 'maandloon': 2455, 'afdeling': 'HR', 'bedrijfswagen': None},
    {"id": 12, 'naam': 'Liesbeth Opdenbosch', 'leeftijd': 37, 'geslacht': 'V', 'functie': 'bediende', 'maandloon': 3017, 'afdeling': 'Marketing', 'bedrijfswagen': None},
    {"id": 13, 'naam': 'Mark De Vries', 'leeftijd': 24, 'geslacht': 'M', 'functie': 'bediende', 'maandloon': 2218, 'afdeling': 'HR', 'bedrijfswagen': 6},
    {"id": 14, 'naam': 'Nina van Dijk', 'leeftijd': 27, 'geslacht': 'V', 'functie': 'bediende', 'maandloon': 2212, 'afdeling': 'IT', 'bedrijfswagen': None},
    {"id": 15, 'naam': 'Oscar Janssens', 'leeftijd': 32, 'geslacht': 'M', 'functie': 'bediende', 'maandloon': 3438, 'afdeling': 'Marketing', 'bedrijfswagen': None},
    {"id": 16, 'naam': 'Pauline De Winter', 'leeftijd': 36, 'geslacht': 'V', 'functie': 'bediende', 'maandloon': 2651, 'afdeling': 'Marketing', 'bedrijfswagen': None},
    {"id": 17, 'naam': 'Quinten Bosmans', 'leeftijd': 23, 'geslacht': 'M', 'functie': 'bediende', 'maandloon': 2034, 'afdeling': 'Marketing', 'bedrijfswagen': 7},
    {"id": 18, 'naam': 'Rita Claes', 'leeftijd': 31, 'geslacht': 'V', 'functie': 'bediende', 'maandloon': 2199, 'afdeling': 'Marketing', 'bedrijfswagen': None},
    {"id": 19, 'naam': 'Stefan Timmermans', 'leeftijd': 34, 'geslacht': 'M', 'functie': 'bediende', 'maandloon': 3236, 'afdeling': 'Marketing', 'bedrijfswagen': 8},
    {"id": 20, 'naam': 'Tessa Verhoeven', 'leeftijd': 26, 'geslacht': 'V', 'functie': 'bediende', 'maandloon': 3402, 'afdeling': 'IT', 'bedrijfswagen': None}
]

arbeiders_data_input = [
    {"id": 21, 'naam': 'Jan Peeters', 'leeftijd': 40, 'geslacht': 'M', 'functie': 'arbeider', 'uurloon': 17.51, 'uren_gewerkt': 37},
    {"id": 22, 'naam': 'Lisa Jansen', 'leeftijd': 28, 'geslacht': 'V', 'functie': 'arbeider', 'uurloon': 28.10, 'uren_gewerkt': 21},
    {"id": 23, 'naam': 'Tom Willems', 'leeftijd': 35, 'geslacht': 'M', 'functie': 'arbeider', 'uurloon': 28.10, 'uren_gewerkt': 27},
    {"id": 24, 'naam': 'Evi Vermeulen', 'leeftijd': 30, 'geslacht': 'V', 'functie': 'arbeider', 'uurloon': 21.48, 'uren_gewerkt': 28},
    {"id": 25, 'naam': 'Sam De Groot', 'leeftijd': 24, 'geslacht': 'X', 'functie': 'arbeider', 'uurloon': 18.39, 'uren_gewerkt': 23},
    {"id": 26, 'naam': 'Karin De Smet', 'leeftijd': 32, 'geslacht': 'V', 'functie': 'arbeider', 'uurloon': 19.78, 'uren_gewerkt': 36},
    {"id": 27, 'naam': 'Peter Janssens', 'leeftijd': 45, 'geslacht': 'M', 'functie': 'arbeider', 'uurloon': 15.66, 'uren_gewerkt': 29},
    {"id": 28, 'naam': 'Nina Van Loon', 'leeftijd': 27, 'geslacht': 'V', 'functie': 'arbeider', 'uurloon': 27.94, 'uren_gewerkt': 24},
    {"id": 29, 'naam': 'Wim Claes', 'leeftijd': 33, 'geslacht': 'M', 'functie': 'arbeider', 'uurloon': 20.73, 'uren_gewerkt': 24},
    {"id": 30, 'naam': 'Sofie Luyten', 'leeftijd': 29, 'geslacht': 'V', 'functie': 'arbeider', 'uurloon': 19.50, 'uren_gewerkt': 26},
    {"id": 31, 'naam': 'Erik Opdenbosch', 'leeftijd': 50, 'geslacht': 'M', 'functie': 'arbeider', 'uurloon': 24.24, 'uren_gewerkt': 21},
    {"id": 32, 'naam': 'Anke Bosmans', 'leeftijd': 31, 'geslacht': 'V', 'functie': 'arbeider', 'uurloon': 23.59, 'uren_gewerkt': 21},
    {"id": 33, 'naam': 'Tobias De Winter', 'leeftijd': 36, 'geslacht': 'M', 'functie': 'arbeider', 'uurloon': 17.41, 'uren_gewerkt': 20},
    {"id": 34, 'naam': 'Emma Meeuwis', 'leeftijd': 26, 'geslacht': 'V', 'functie': 'arbeider', 'uurloon': 26.79, 'uren_gewerkt': 29},
    {"id": 35, 'naam': 'Bart De Jong', 'leeftijd': 34, 'geslacht': 'M', 'functie': 'arbeider', 'uurloon': 16.37, 'uren_gewerkt': 20},
    {"id": 36, 'naam': 'Laura Timmermans', 'leeftijd': 30, 'geslacht': 'V', 'functie': 'arbeider', 'uurloon': 27.43, 'uren_gewerkt': 27},
    {"id": 37, 'naam': 'Geert Van Dijk', 'leeftijd': 42, 'geslacht': 'M', 'functie': 'arbeider', 'uurloon': 27.83, 'uren_gewerkt': 40},
    {"id": 38, 'naam': 'Liesbeth Verhoeven', 'leeftijd': 25, 'geslacht': 'V', 'functie': 'arbeider', 'uurloon': 21.45, 'uren_gewerkt': 29},
    {"id": 39, 'naam': 'Oscar Jansen', 'leeftijd': 39, 'geslacht': 'M', 'functie': 'arbeider', 'uurloon': 18.15, 'uren_gewerkt': 29},
    {"id": 40, 'naam': 'Tessa Claes', 'leeftijd': 29, 'geslacht': 'V', 'functie': 'arbeider', 'uurloon': 20.28, 'uren_gewerkt': 27}
]

personeel_data_class = []
bedienden_data_class = []
arbeiders_data_class = []

for item in personeel_data_input:
    new_personeel = personeel(item['id'],item['naam'],item['leeftijd'],item['geslacht'],item['functie'])
    personeel_data_class.append(new_personeel)
for item in bedienden_data_input:
    new_personeel = bediende(item['id'],item['naam'],item['leeftijd'],item['geslacht'],item['functie'],item['maandloon'],item['afdeling'],item['bedrijfswagen'])
    bedienden_data_class.append(new_personeel)
for item in arbeiders_data_input:
    new_personeel = arbeider(item['id'],item['naam'],item['leeftijd'],item['geslacht'],item['functie'],item['uurloon'],item['uren_gewerkt'])
    arbeiders_data_class.append(new_personeel)

