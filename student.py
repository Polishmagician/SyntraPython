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
def zoek_student(id):
    for student in studenten:
        if student[0] == id:
            print(tabulate(student))
            return
    print(f"{id} is geen geldig ID")
toon_studenten(studenten)
zoek_student(int(input("Geef de ID van de student: ")))