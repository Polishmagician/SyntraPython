def figuur(teken, rijen, kolommen):
    for i in range(rijen):
        for j in range(kolommen):
            print(teken, end = "\t")
        print()

def figuur_aflopend(teken, rijen):
    for i in range(rijen):
        for j in range(rijen-i):
            print(teken, end="\t")
        print()

figuur("*",3,4)
figuur_aflopend("*",4)