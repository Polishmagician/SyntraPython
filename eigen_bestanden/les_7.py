# lijst_namen = ["Bart","Bert","Bjorn","Frank"]
# plaats = lijst_namen.index("Bart")
# lijst_namen[plaats] = "Henk"
# print(lijst_namen)
from tabulate import tabulate

# nummers = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for rij in nummers:
#     for item in rij:
#         print(item, end = "\t")
#     print()

heading = ["Dag 1","Dag 2","Dag 3","Dag 4","Dag 5","Gemiddelde"]
temp = [[12,9,6,3,3],[16,16,16,14,16]]

def weer():
    for row in temp:
        average = sum(row)/len(row)
        row.append(average)
    temp[0].insert(0,"Min Temp")
    temp[1].insert(0,"Max Temp")
    tabel = tabulate(temp, headers=heading)
    print(tabel)