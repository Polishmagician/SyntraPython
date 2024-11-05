honden = {
    "hond1": {
        "ras": "Golden Retriever",
        "geslacht": "Mannelijk",
        "leeftijd": 5
    },
    "hond2": {
        "ras": "Duitse Herder",
        "geslacht": "Vrouwelijk",
        "leeftijd": 3
    },
    "hond3": {
        "ras": "Labrador",
        "geslacht": "Mannelijk",
        "leeftijd": 4
    },
    "hond4": {
        "ras": "Beagle",
        "geslacht": "Vrouwelijk",
        "leeftijd": 2
    },
    "hond5": {
        "ras": "Bulldog",
        "geslacht": "Mannelijk",
        "leeftijd": 6
    },
    "hond6": {
        "ras": "Poedel",
        "geslacht": "Vrouwelijk",
        "leeftijd": 3
    },
    "hond7": {
        "ras": "Shih Tzu",
        "geslacht": "Vrouwelijk",
        "leeftijd": 5
    },
    "hond8": {
        "ras": "Boxer",
        "geslacht": "Mannelijk",
        "leeftijd": 4
    },
    "hond9": {
        "ras": "Border Collie",
        "geslacht": "Vrouwelijk",
        "leeftijd": 2
    },
    "hond10": {
        "ras": "Jack Russell Terriër",
        "geslacht": "Mannelijk",
        "leeftijd": 7
    }
}

for hond in honden.values():
    if hond["geslacht"] == "Mannelijk" and hond["leeftijd"] > 5:
        print(hond)
    elif hond["ras"] == "Poedel":
        print(hond)