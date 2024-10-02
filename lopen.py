# Een persoon gaat 3 keer per week lopen, en houd deze data bij
# Bereken hoeveel elk persoon in totaal heeft gelopen
# Bereken onderaan het totaal dat er per dag gelopen is.
# Maak een functie alle totalen. Die berekent hoeveel er in totaal door alle lopers gelopen is.
# Zorg ervoor dat je een loper kan toevoegen
# Zorg ervoor dat je een loper kan verwijderen
# Maak een datatabel(nieuwe tabel), som,max,min,gemiddelde van de dagen toon deze met een functie.
from tabulate import tabulate
personen = ["Jan","Bart"]
gelopen = [[10,7,15],[15,10,11]]
data = gelopen[:]
for f in range(len(personen)):
    data[f].insert(0,personen[f])
data = data


def new_person():
    new_name = [input("Give a new name: ")]
    new_gelopen = []
    for f in range(3):
        km = int(input(f"Hoeveel km heeft {new_name[0]} gelopen op dag {f+1}? "))
        new_gelopen.append(km)
    for j in new_gelopen:
        new_name.append(j)
    data.insert(2,new_name)

#Totaal per loper
for r in range(len(data)):
    tot_gelopen = sum(data[r][1:])
    data[r].append(tot_gelopen)
#Totaal per dag
daily_run = ["Totaal per dag"]
dag_sum = 0
for d in range(3):
    for e in range(2):
        dag_gelopen = data[e][d+1]
        dag_sum += dag_gelopen
    daily_run.append(dag_sum)
    dag_sum = 0
data.append(daily_run)


#Visualize
heading = ["Naam", "Dag 1", "Dag 2", "Dag 3", "Totaal"]

tabel = tabulate(data, headers = heading)
print(tabel)