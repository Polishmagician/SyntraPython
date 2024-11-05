# # lijst dieren
# # dier toevoegen append insert
# # pop & remove
# # sorteer Z-A
#
# lijst_dieren = ["Kat", "Hond", "Ezel", "Aap"]
#
# lijst_dieren.append("Leeuw")
# lijst_dieren.insert(2,"Haai")
# print(lijst_dieren)
#
# lijst_dieren.pop(2)
# lijst_dieren.remove("Leeuw")
# print(lijst_dieren)
#
# lijst_dieren.sort(reverse=True)
# print(lijst_dieren)

# GITHUB SYNC OP AF

# lijst = [[0,1,2,3],[4,5,6,7],[8,9,10,11]]
# for i in range(len(lijst)): #Aparte kolom afdrukken
#     print(lijst[i][0])
# print(lijst)
# for rij in lijst:
#     print(rij) #rijen onder elkaar
# for rij in lijst: #Zonder haakjes, met som van de rij op het eind
#     som = sum(rij)
#     rij.append(som)
#     for item in rij:
#         print(item, end = "\t")
#     print()

#Gemiddelde rijen:

tabel = [["k1", "k2", "k3"], [1, 2, 3], [4, 5, 6], [7, 8, 9]]
tabel[0].append("Gemiddelde")

for rij in tabel[1:]:
    som = sum(rij)
    gem = som/len(rij)
    rij.append(gem)
for rij in tabel:
    for item in rij:
        print(item, end="\t")
    print()