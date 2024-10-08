# Maak een 2d lijst personeel met 5  rijen aan data.
# Naam, Leeftijd, Woonplaats, Functie, Afdeling
# Toon deze data in een tabulate tabel
# Zorg ervoor dat een rij toegevoegd kan worden
# Zorg ervoor dat een rij verwijderd kan worden
# Maak een functie sorteren op naam en sorteren op leeftijd

from tabulate import tabulate

personeelsleden =  {
    1:{
        "Naam": "Jeroen van Dijk",
        "Leeftijd": 34,
        "Woonplaats": "Amsterdam",
        "Functie": "Projectmanager",
        "Afdeling": "ICT"
    },
    2:{
        "Naam": "Sanne de Vries",
        "Leeftijd": 29,
        "Woonplaats": "Rotterdam",
        "Functie": "HR-Adviseur",
        "Afdeling": "HR"
    },
    3:{
        "Naam": "Mark Jansen",
        "Leeftijd": 45,
        "Woonplaats": "Utrecht",
        "Functie": "Financieel Analist",
        "Afdeling": "Financiën"
    },
    4:{
        "Naam": "Nina Bakker",
        "Leeftijd": 38,
        "Woonplaats": "Den Haag",
        "Functie": "Marketing Coördinator",
        "Afdeling": "Marketing"
    },
    5:{
        "Naam": "Thomas Willems",
        "Leeftijd": 50,
        "Woonplaats": "Eindhoven",
        "Functie": "Technisch Ingenieur",
        "Afdeling": "Productie"
    }}


kolom = ["ID", "Naam", "Leeftijd", "Woonplaats", "Functie", "Afdeling"]

def create_list(personeel):
    personeel_list = []
    for key, inner in personeel.items():
        row = [key]
        for k,v in inner.items():
            row.append(v)
        personeel_list.append(row)
    print(tabulate(personeel_list, headers=kolom))
    return personeel_list


def add_personnel(personeel,personeel_list):
    new_personnel = [max(personeel.keys())+1,
                     input("Geef de naam: "),
                     int(input("Geef de leeftijd: ")),
                     input("Geef de woonplaats: "),
                     input("Geef de functie: "),
                     input("Geef de afdeling: ")]
    personeel_list.append(new_personnel)
    print(tabulate(personeel_list, headers=kolom))
    return personeel_list

def remove_personnel(personeelsleden,personeel_list):
    print(tabulate(personeel_list,headers=kolom))
    id_to_remove = int(input("Geef het ID dat je wilt verwijderen: "))
    if id_to_remove in personeelsleden.keys():
        del personeelsleden[id_to_remove]
        create_list(personeelsleden)
        return
    else:
        print(f"{id_to_remove} is geen geldige ID")


# create_list(personeelsleden)
# add_personnel(personeelsleden,create_list(personeelsleden))
remove_personnel(personeelsleden,create_list(personeelsleden))

