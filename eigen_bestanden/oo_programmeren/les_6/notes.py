#list comprehension:

maandlonen = [2500, 3200, 4000, 2800, 3600, 4100, 2900, 3400, 3700, 3300, 3900, 4200,4231,2555,2375]
woorden = [
    "zon",
    "regenbui",
    "maan",
    "zandkorrel",
    "ster",
    "oceaan",
    "wind",
    "bergenketen",
    "boom",
    "waterdruppel",
    "dag",
    "nachtvlinder",
    "ijs",
    "woestijn",
    "vuur",
    "continent",
    "blad",
    "regenwoud",
    "bos",
    "hemellichaam"
]

jaarloon = [sum(maandlonen)]
# print(jaarloon)

deelbaar_door_drie = [x for x in maandlonen if x%3==0]
# print(deelbaar_door_drie)
deelbaar_door_twee_of_5 = [x for x in maandlonen if x%2==0 or x%5==0]
# print(deelbaar_door_twee_of_5)

def woord_langer_dan_5_tekens(woord):
    x = 5
    return_list = []
    if len(woord) >= x:
        return woord

print(list(map(woord_langer_dan_5_tekens,woorden)))