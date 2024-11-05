# Toon alle studenten met geslacht x van woonplaats y

from tabulate import tabulate
studenten = [
    [1,"Sophie", "De Smet", "Vrouw", "Gent"],
    [2,"Lukas","Verhoeven","Man","Antwerpen"],
    [3,"Elise","Vandenberghe","Vrouw","Brugge"],
    [4,"Thomas","Dupont","Man","Luik"],
    [5,"Annelies","Peeters","Vrouw","Leuven"]
]
kolom = ["ID", "Voornaam", "Achternaam", "Geslacht", "Woonplaats"]


def toon_studenten(studenten):
    print(tabulate(studenten, headers=kolom))


def zoek_student(studenten):
    id = int(input("Geef de ID van de student: "))
    for student in studenten:
        if student[0] == id:
            print(tabulate([student],headers=kolom))
            return
    print(f"{id} is geen geldig ID")


def voeg_student_toe(studenten):
    new_student = [studenten[-1][0]+1]
    new_student.append(input("Geef de voornaam in: "))
    new_student.append(input("Geef de achternaam in: "))
    new_student.append(input("Geef het geslacht in: "))
    new_student.append(input("Geef de woonplaats in: "))
    studenten.append(new_student)
    return studenten


def verwijder_student(studenten):
    stud_to_remove = int(input("Geef de ID van de student die je wil verwijderen: "))
    if stud_to_remove > studenten[-1][0]:
        print(f"{stud_to_remove} is niet in de lijst")
        return
    for i,student in enumerate(studenten):
        if student[0] == stud_to_remove:
            del studenten[i]
            return studenten


def geslacht_filter(studenten):
    gefilterde_student = []
    geslacht = input("Op welk geslacht wil je filteren? ")
    for student in studenten:
        if student[3] == geslacht:
            gefilterde_student.append(student)
    if gefilterde_student:
        print(tabulate(gefilterde_student, headers=kolom))
        return
    else:
        return


def woonplaats_filter(studenten):
    gefilterde_student = []
    woonplaats = input("Op welke woonplaats wil je filteren? ")
    for student in studenten:
        if student[4] == woonplaats:
            gefilterde_student.append(student)
    if gefilterde_student:
        print(tabulate(gefilterde_student, headers=kolom))
        return
    else:
        return

def woonplaats_geslacht_filter(studenten):
    gefilterde_student = []
    woonplaats = input("Op welke woonplaats wil je filteren? ")
    geslacht = input("Op welk geslacht wil je filteren? ")
    for student in studenten:
        if student[4] == woonplaats and student[3] == geslacht:
            gefilterde_student.append(student)
    if gefilterde_student:
        print(tabulate(gefilterde_student, headers=kolom))
        return
    else:
        return


def kiezer(studenten):
    while True:
        print("1: Toon studenten",
              "2: Zoek student op ID",
              "3: Voeg student toe",
              "4: Verwijder student",
              "5: Filter op geslacht",
              "6: Filter op woonplaats",
              "7: Filter op woonplaats en geslacht",
              "8: STOP", sep="\n")
        keuze = input("Kies een optie: ")
        if keuze == "8":
            break
        elif keuze == "1":
            toon_studenten(studenten)
        elif keuze == "2":
            zoek_student(studenten)
        elif keuze == "3":
            voeg_student_toe(studenten)
        elif keuze == "4":
            verwijder_student(studenten)
        elif keuze == "5":
            geslacht_filter(studenten)
        elif keuze == "6":
            woonplaats_filter(studenten)
        elif keuze == "7":
            woonplaats_geslacht_filter(studenten)
        else:
            print("Foutieve invoer, 8 to STOP")
    print(tabulate(studenten, headers=kolom))

# toon_studenten(studenten)
# verwijder_student(studenten)
# toon_studenten(studenten)
#voeg_student_toe(studenten)
#toon_studenten(studenten)
#zoek_student(studenten)
# geslacht_filter(studenten)
# woonplaats_geslacht_filter(studenten)
kiezer(studenten)