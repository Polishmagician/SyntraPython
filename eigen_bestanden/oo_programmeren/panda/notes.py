import pandas as pd

headers = ["Naam","Km","Tijd in Min"]
data = pd.DataFrame({"Naam" : ["Alex","Maxim","Pauline"],
                     "Km": [8,12,9],
                     "Tijd in Min": [55,74,60]})

print(data)