import random as rd
from colorama import Fore
from tabulate import  tabulate

#Input
subjects = ["Wiskunde", "Geschiedenis", "Engels", "Nederlands", "Biologie"]
students = ["Bart", "Marie", "Stef", "Aaron"]
heading = subjects[:]
heading.insert(0,"Naam")
heading.append("Totaal")
gem = ["Gemiddelde"]
avg = 0
saved_punten = []
test = 0
tot = 0

#randomizing scores

for s in range(len(students)):
    punten = [students[s]]
    for i in range(len(subjects)):
        score = rd.randint(1,10)
        punten.append(score)
    saved_punten.append(punten)
saved_punten.insert(0,heading)

#Calculate average
for i in range(len(subjects)):
    for j in range(len(saved_punten)-1):
        test += saved_punten[j+1][i+1]
    avg = test / len(students)
    gem.append(avg)
    test = 0
saved_punten.append(gem)

#Calculate total
for i in range(len(students)+1):
    tot = sum(saved_punten[i+1][1:])*2
    saved_punten[i+1].append(tot)



#Visualisatie
# for rij in saved_punten:
#     for item in rij:
#         if type(item) is int and item <5:
#             print(Fore.RED + str(item) + Fore.RESET, end= "\t")
#         else:
#             print(item, end = "\t")
#     print()
tabel = tabulate(saved_punten[1:], headers = heading)
print(tabel)
