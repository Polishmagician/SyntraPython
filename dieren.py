from tabulate import tabulate

dieren = {1 : {"naam" : "Leo", "soort": "Leeuw", "leeftijd": 8},
          2 : {"naam" : "Binky", "soort": "olifant", "leeftijd": 32},
          3 : {"naam" : "Lola", "soort": "kangoeroe", "leeftijd": 5},
          4 : {"naam" : "Sly", "soort": "vos", "leeftijd": 4},
          5 : {"naam" : "Tara", "soort": "schildpad", "leeftijd": 75},
          6 : {"naam" : "Zephyr", "soort": "adelaar", "leeftijd": 18},
          7 : {"naam" : "Max", "soort": "wolf", "leeftijd": 6}}
kolom = ["ID","Naam","Soort","Leeftijd"]

dieren_list = []

for key, inner in dieren.items():
    row = [key]
    for k,v in inner.items():
        row.append(v)
    dieren_list.append(row)
print(tabulate(dieren_list,headers=kolom))