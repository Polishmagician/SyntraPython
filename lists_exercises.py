# Matrix
def matrix_creator():
    matrix = [[6,8,5,2,4],[5,1,5,2,9],[7,2,7,2,6],[3,4,8,2,1]]

    for row in matrix:
        for item in row:
            print(item, end ="\t")
        print()
def weer():
    min_temp = ["Min temp",12,9,6,3,3]
    max_temp = ["Max temp",16,16,16,14,16]
    avg_min = sum(min_temp[1:])/len(min_temp[1:])
    avg_max = sum(max_temp[1:])/len(max_temp[1:])
    min_temp.append(avg_min)
    max_temp.append(avg_max)

    weer = [["","Dag 1","Dag 2","Dag 3","Dag 4","Dag 5","Gemiddelde"],min_temp,max_temp]
    for row in weer:
        for item in row:
            print(item, end="\t")
        print()
weer()

